# FarmChat

FarmChat는 농부들을 위한 토양 및 날씨 정보를 쿼리할 수 있는 챗봇 애플리케이션입니다.

## 프로젝트 구조

```
PG01/
├── .venv/           # Python 가상 환경
├── main/            # 메인 애플리케이션 코드
├── models/          # 데이터 모델 정의
├── api/             # API 관련 코드
├── resources/       # 리소스 파일
├── pyproject.toml   # 프로젝트 설정 및 의존성 관리
└── requirements.txt # Python 패키지 의존성
```

## 기술 스택

- Python 3.11 이상
- Streamlit
- OpenAI API
- Pydantic
- LangChain (향후 사용 예정)
- MongoDB (향후 사용 예정)

## 설치 방법

1. Python 3.11 이상이 설치되어 있어야 합니다.

2. Poetry를 사용하여 의존성 설치:
```bash
poetry install
```

3. 가상 환경 활성화:
```bash
poetry shell
```

## 실행 방법

```bash
streamlit run main/app.py
```

## 개발 환경 설정

1. `.env` 파일을 프로젝트 루트 디렉토리에 생성하고 필요한 환경 변수를 설정합니다:
```
OPENAI_API_KEY=your_api_key_here
```

## 테스트

테스트를 실행하려면:
```bash
pytest
```

## 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다.

## 작성자

- Anjung Tan (ctan0722@gmail.com) 