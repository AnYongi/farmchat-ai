"""Utility functions for FarmChat.

This module contains helper functions used throughout the application,
including logging, validation, and data processing utilities.
"""

import json
import os
from datetime import datetime
from pathlib import Path

def save_api_response(parcel_id: str, response_data: dict) -> str:
    """Save API response to a JSON file.
    
    Args:
        parcel_id: The parcel identifier
        response_data: The API response data to save
        
    Returns:
        str: Path to the saved file
    """
    # TODO: Implement response saving logic
    pass

def validate_parcel_id(parcel_id: str) -> bool:
    """Validate the format of a parcel ID.
    
    Args:
        parcel_id: The parcel identifier to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    # TODO: Implement parcel ID validation
    pass

def classify_question(question: str) -> str:
    """Classify user question into data type: soil / weather-short / weather-agri.
    
    Args:
        question: User question in Korean
        
    Returns:
        str: One of 'soil', 'weather-short', 'weather-agri'
    """
    lower_q = question.lower()

    soil_keywords = ["토양", "ph", "산도", "ec", "유기물"]
    short_weather_keywords = ["기온", "날씨", "강수", "강수량", "단기", "지금", "오늘"]
    agri_weather_keywords = ["농업기상", "관측", "기상관측", "센서", "지점"]

    if any(kw in lower_q for kw in soil_keywords):
        return "soil"
    elif any(kw in lower_q for kw in agri_weather_keywords):
        return "weather-agri"
    elif any(kw in lower_q for kw in short_weather_keywords):
        return "weather-short"
    else:
        return "unknown"

# utils.py 내부에 추가할 함수 (기상청 공식 DFS 좌표 변환)
def latlon_to_grid(lat, lon):
    import math
    RE = 6371.00877  # 지구 반경(km)
    GRID = 5.0       # 격자 간격(km)
    SLAT1 = 30.0     # 투영 위도1(degree)
    SLAT2 = 60.0     # 투영 위도2(degree)
    OLON = 126.0     # 기준점 경도(degree)
    OLAT = 38.0      # 기준점 위도(degree)
    XO = 43          # 기준점 X좌표(GRID)
    YO = 136         # 기준점 Y좌표(GRID)

    DEGRAD = math.pi / 180.0
    re = RE / GRID
    slat1 = SLAT1 * DEGRAD
    slat2 = SLAT2 * DEGRAD
    olon = OLON * DEGRAD
    olat = OLAT * DEGRAD

    sn = math.tan(math.pi * 0.25 + slat2 * 0.5) / math.tan(math.pi * 0.25 + slat1 * 0.5)
    sn = math.log(math.cos(slat1) / math.cos(slat2)) / math.log(sn)
    sf = math.tan(math.pi * 0.25 + slat1 * 0.5)
    sf = math.pow(sf, sn) * math.cos(slat1) / sn
    ro = math.tan(math.pi * 0.25 + olat * 0.5)
    ro = re * sf / math.pow(ro, sn)

    ra = math.tan(math.pi * 0.25 + lat * DEGRAD * 0.5)
    ra = re * sf / math.pow(ra, sn)
    theta = lon * DEGRAD - olon
    if theta > math.pi:
        theta -= 2.0 * math.pi
    if theta < -math.pi:
        theta += 2.0 * math.pi
    theta *= sn

    x = ra * math.sin(theta) + XO + 0.5
    y = ro - ra * math.cos(theta) + YO + 0.5
    return int(x), int(y)

def parse_niast_response(response_data):
    try:
        item = response_data.get("body", {}).get("items", {}).get("item", [])[0]
        return {
            "pH": item.get("ph"),
            "EC": item.get("ec"),
            "유기물": item.get("oc"),
            "CEC": item.get("cec")
        }
    except:
        return {"error": "Failed to parse NIAST response"}

def parse_kma_response(response_data):
    try:
        items = response_data.get("response", {}).get("body", {}).get("items", {}).get("item", [])
        result = {}
        for item in items:
            category = item.get("category")
            value = item.get("obsrValue")
            if category and value:
                result[category] = value
        return result
    except:
        return {"error": "Failed to parse KMA response"}