"""
FarmChat Streamlit UI 연결 예시 - GPT 응답 생성 포함 + 위경도 → 격자 변환기 포함 + 응답 파싱 요약
"""

import streamlit as st
from main.utils import classify_question, latlon_to_grid, parse_niast_response, parse_kma_response
from api.niast_client import NIASTClient
from api.kma_client import KMAClient
from models.response import ChatResponse
from main.utils import save_api_response
from main.generate_gpt_response import build_response_chain, FARMCHAT_PROMPT_TEMPLATE
from datetime import datetime

# GPT 체인 준비
gpt_chain = build_response_chain(FARMCHAT_PROMPT_TEMPLATE)

def main():
    st.title("FarmChat v0.1")

    parcel_id = st.text_input("Parcel ID", placeholder="Enter farm or plot ID")
    question = st.text_area("Question", placeholder="Ask about soil or weather...")

    if st.button("Submit"):
        if not parcel_id or not question:
            st.error("Please fill in both fields")
            return

        st.info("Processing your request...")

        topic = classify_question(question)

        if topic == "soil":
            client = NIASTClient()
            data_source = "NIAST"
        elif topic == "weather-short":
            lat, lon = 36.123, 128.456
            nx, ny = latlon_to_grid(lat, lon)
            st.write(f"🔹 격자 좌표: nx={nx}, ny={ny}")
            client = KMAClient()
            client.set_grid_coordinates(nx, ny)
            data_source = "KMA"
        else:
            st.warning("Sorry, I couldn’t classify your question.")
            return

        response_data = client.get_data(parcel_id)
        save_api_response(parcel_id, response_data)

        # 핵심 정보만 추출
        if topic == "soil":
            parsed_data = parse_niast_response(response_data)
        elif topic == "weather-short":
            parsed_data = parse_kma_response(response_data)
        else:
            parsed_data = response_data

        gpt_input = {
            "question": question,
            "data": str(parsed_data)
        }
        answer = gpt_chain.invoke(gpt_input)

        response = ChatResponse(
            message=answer,
            data_source=data_source,
            timestamp=datetime.now(),
            raw_data=response_data
        )

        st.markdown(response.format_message())

if __name__ == "__main__":
    main()
