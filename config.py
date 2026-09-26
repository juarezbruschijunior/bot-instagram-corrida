import os
from dotenv import load_dotenv

# Carrega variáveis do arquivo .env
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
INSTAGRAM_ACCOUNT_ID = os.getenv("INSTAGRAM_ACCOUNT_ID", "17841476601172484")
INSTAGRAM_ACCESS_TOKEN = os.getenv("INSTAGRAM_ACCESS_TOKEN", "")
LINK_PLANILHA = os.getenv("LINK_PLANILHA", "https://biotoolspremium.com.br/#physiological-tools-section")

# Configuração da Persona da Corredora
PERSONA_NAME = "Aline Manuela"
PERSONA_PROMPT_BASE = (
    "photorealistic 8k portrait of an athletic smiling young Brazilian woman runner, fit physique, "
    "wearing high performance running clothes (sports bra, running shorts, sport smartwatch on wrist), "
    "sweaty post-run glow, holding smartphone showing workout data, sunrise urban park background, cinematic lighting, 35mm lens"
)
