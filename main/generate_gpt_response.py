"""
LangChain 기반 GPT 응답 생성기 (Farm챗용)
사용자가 쉽게 프롬프트 템플릿을 교체하거나 수정할 수 있도록 구조화함
"""

from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough

def build_response_chain(prompt_template: str, model_name: str = "gpt-4o", temperature: float = 0.3):
    """
    LangChain RunnableChain 구성

    Args:
        prompt_template (str): 사용자 지정 프롬프트 템플릿
        model_name (str): 사용할 OpenAI 모델 이름
        temperature (float): 생성 온도

    Returns:
        RunnableChain: 실행 가능한 체인
    """
    prompt = ChatPromptTemplate.from_template(prompt_template)
    model = ChatOpenAI(model=model_name, temperature=temperature)
    parser = StrOutputParser()

    chain = (
        {"question": RunnablePassthrough(), "data": RunnablePassthrough()} |
        prompt |
        model |
        parser
    )
    return chain

# 기본 프롬프트 템플릿 (사용자가 교체 가능)
FARMCHAT_PROMPT_TEMPLATE = """
너는 작물 생육 및 환경에 대한 전문 AI 상담사야. 아래 정보를 참고해 사용자 질문에 친절하고 정확하게 답변해줘.

[질문]
{question}

[환경 데이터]
{data}

[답변 작성 조건]
- 한국어로 답변할 것
- 수치를 설명하고 기준치와 비교해줄 것
- 필요한 경우 작물 재배 팁을 제안할 것
- 농민이 이해하기 쉽게 말해줄 것

[출력 형식]
📌 요약
- [한 줄 요약]

🌱 세부 설명
- [지표별 설명 및 영향]

📋 데이터 출처
- [API 이름 또는 제공기관]
"""

# 예시 사용
# chain = build_response_chain(FARMCHAT_PROMPT_TEMPLATE)
# result = chain.invoke({"question": "우리 밭 토양 산도 어때?", "data": "{pH: 6.4, EC: 0.5}"})
# print(result)
