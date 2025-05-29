"""FarmChat Streamlit UI application.

This module implements the main Streamlit interface for the FarmChat application,
handling user input for parcel IDs and questions, and displaying responses.
"""

import streamlit as st
from utils import classify_question
from api.niast_client import NIASTClient
from api.kma_client import KMAClient
from models.response import ChatResponse
from main.utils import save_api_response
from datetime import datetime

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
            client = KMAClient()
            data_source = "KMA"
        else:
            st.warning("Sorry, I couldn’t classify your question.")
            return

        # API 호출
        response_data = client.get_data(parcel_id)

        # 응답 저장
        save_api_response(parcel_id, response_data)

        # 응답 메시지 구성
        message = f"Here is the {topic} data for your parcel:\n\n{str(response_data)[:500]}"
        response = ChatResponse(
            message=message,
            data_source=data_source,
            timestamp=datetime.now(),
            raw_data=response_data
        )

        st.markdown(response.format_message())

if __name__ == "__main__":
    main()
