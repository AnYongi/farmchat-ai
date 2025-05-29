"""NIAST Soil API client for FarmChat.

This module implements the client for the National Institute of Agricultural
Science and Technology (NIAST) Soil API.
"""

import requests
from .api_base import BaseAPIClient
from main.config import NIAST_API_KEY, NIAST_API_URL

class NIASTClient(BaseAPIClient):
    def __init__(self):
        super().__init__(NIAST_API_KEY, NIAST_API_URL)

    def get_data(self, parcel_id: str) -> dict:
        """Call NIAST soil API with parcel ID."""
        params = {
            "serviceKey": self.api_key,
            "numOfRows": 1,
            "pageNo": 1,
            "dataType": "JSON",
            "farmId": parcel_id  # 예시 파라미터
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
