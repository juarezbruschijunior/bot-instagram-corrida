import os
from dotenv import load_dotenv

# Carrega variáveis do arquivo .env
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
INSTAGRAM_ACCOUNT_ID = os.getenv("INSTAGRAM_ACCOUNT_ID", "17841476601172484")
INSTAGRAM_ACCESS_TOKEN = os.getenv("INSTAGRAM_ACCESS_TOKEN", "")

# Configuração da Apresentadora do Canal de Cinema & Séries
PERSONA_NAME = "Aline Manuela"
NICHO = "Curiosidades de Cinema, Séries & Bastidores de Hollywood"
