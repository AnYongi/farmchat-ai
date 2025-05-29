"""KMA Weather API client for FarmChat.

This module implements the client for the Korea Meteorological Administration (KMA)
Weather API.
"""

import requests
from .api_base import BaseAPIClient
from main.config import KMA_SHORT_TERM_API_KEY, KMA_SHORT_TERM_API_URL

class KMAClient(BaseAPIClient):
    def __init__(self):
        super().__init__(KMA_SHORT_TERM_API_KEY, KMA_SHORT_TERM_API_URL)

    def get_data(self, parcel_id: str) -> dict:
        """Call KMA short-term forecast API."""
        # 여기는 위경도 좌표값이 필요할 수 있음
        params = {
            "serviceKey": self.api_key,
            "dataType": "JSON",
            "numOfRows": 10,
            "pageNo": 1,
            "base_date": "20240527",  # 테스트용
            "base_time": "0600",
            "nx": 60,  # 예시 격자좌표
            "ny": 127
        }
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()  # HTTP 오류 발생 시 예외 발생
            
            # 응답이 비어있는지 확인
            if not response.text.strip():
                return {"error": "Empty response from API"}
            
            # JSON 파싱 시도
            try:
                return response.json()
            except requests.exceptions.JSONDecodeError as e:
                return {
                    "error": f"Failed to parse JSON response: {str(e)}",
                    "raw_response": response.text[:200]  # 원본 응답의 일부를 포함
                }
                
        except requests.exceptions.RequestException as e:
            return {"error": f"API request failed: {str(e)}"}
