"""Configuration settings for FarmChat."""

import os
from dotenv import load_dotenv

load_dotenv()

# --- Core API Keys ---
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")

# --- NIAST (Soil Data) ---
NIAST_API_KEY = os.getenv("NIAST_API_KEY")
NIAST_API_URL = os.getenv("NIAST_API_URL")

# --- KMA Short-Term Forecast (동네예보) ---
KMA_SHORT_TERM_API_KEY = os.getenv("KMA_SHORT_TERM_API_KEY")
KMA_SHORT_TERM_API_URL = os.getenv("KMA_SHORT_TERM_API_URL")

# --- KMA AgriWeather (농업기상 관측데이터) ---
KMA_AGRI_OBSR_API_KEY = os.getenv("KMA_AGRI_OBSR_API_KEY")
KMA_AGRI_OBSR_API_URL = os.getenv("KMA_AGRI_OBSR_API_URL")

# --- MongoDB (optional) ---
MONGODB_URI = os.getenv("MONGODB_URI")
MONGODB_DB_NAME = os.getenv("MONGODB_DB_NAME")
MONGODB_COLLECTION_NAME = os.getenv("MONGODB_COLLECTION_NAME")

# --- General App Settings ---
APP_NAME = "FarmChat"
VERSION = "0.1"
LOG_DIR = "resources/api_logs"
