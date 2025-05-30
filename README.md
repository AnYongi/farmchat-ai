# FarmChat-AI

FarmChat-AI는 농업 현장의 데이터 기반 의사결정을 돕는 대화형 챗봇 서비스입니다.
사용자는 필지의 토양 상태나 날씨 정보를 질문하면, AI가 실시간 데이터를 조회해 쉽게 설명해줍니다.

본 서비스는 스마트팜 환경에서 수집되는 토양 및 기상 데이터를 기반으로 질의응답(QA)을 수행합니다.
Streamlit UI와 OpenAI GPT 모델을 활용한 자연어 이해·응답 시스템 위에 구축되었으며,
향후 LangChain 및 MongoDB를 통한 컨텍스트 유지 및 문서 기반 QA 강화를 목표로 합니다.
실시간 필지 환경 인사이트 제공 및 도메인 특화 AI 챗봇 구조 설계를 검증하는 MVP입니다.
<br><br>
## 📁 프로젝트 구조

```
farmchat-ai/
├── main/            # 메인 애플리케이션 코드
├── models/          # 데이터 모델 정의
├── api/             # API 관련 코드
├── resources/       # 리소스 파일
├── pyproject.toml   # 프로젝트 설정 및 의존성 관리
└── requirements.txt # Python 패키지 의존성
```
<br>
## 🛠️ 기술 스택

- Python 3.11 이상
- Streamlit
- OpenAI API
- Pydantic
- LangChain (향후 사용 예정)
- MongoDB (향후 사용 예정)
<br>
## 📦 설치 방법

1. Python 3.11 이상이 설치되어 있어야 합니다.

2. Poetry를 사용하여 의존성 설치:
```bash
poetry install
```

3. 가상 환경 활성화:
```bash
poetry shell
```
<br>
## ▶️ 실행 방법

```bash
streamlit run main/app.py
```
<br>
## ⚙️ 개발 환경 설정

1. `.env` 파일을 프로젝트 루트 디렉토리에 생성하고 필요한 환경 변수를 설정합니다:
```
OPENAI_API_KEY=your_api_key_here
```
<br>
## ✅ 테스트

테스트를 실행하려면:
```bash
pytest
```
<br>
## 📄 라이선스

이 프로젝트는 GNU General Public License v3.0 (GPL-3.0) 라이선스 하에 배포됩니다. 이 라이선스는 상업적 사용을 제한하며, 이 소프트웨어를 사용하여 만든 모든 파생작품도 동일한 라이선스로 공개되어야 합니다.

자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.
<br>
## 👤 작성자

- Anjung Tan (ctan0722@gmail.com) 


© 2025 Anjung Tan. Licensed under the GNU GPL v3.0.
