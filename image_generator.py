import os
import requests
import random
import time

POSTS_DIR = os.path.join(os.path.dirname(__file__), "posts_gerados")
os.makedirs(POSTS_DIR, exist_ok=True)

# Galeria Exclusiva da Aline em Porto Alegre (100% Real, Físico Atlético, Alta Definição)
FOTOS_ALINE_POA = [
    os.path.join(POSTS_DIR, "poa_orla_fit.jpg"),        # Orla do Guaíba - Treino Fit
    os.path.join(POSTS_DIR, "poa_redencao.jpg"),        # Redenção / Açorianos - Alongando pós-treino
    os.path.join(POSTS_DIR, "poa_pontal_sunset.jpg"),   # Pontal do Guaíba - Pôr do Sol
]

def fazer_upload_cdn(caminho_imagem):
    """
    Faz upload temporário da imagem local para gerar link direto .jpg exigido pelo Instagram.
    """
    try:
        url = "https://catbox.moe/user/api.php"
        with open(caminho_imagem, "rb") as f:
            files = {"fileToUpload": f}
            data = {"reqtype": "fileupload"}
            resp = requests.post(url, files=files, data=data, timeout=30)
            if resp.status_code == 200 and resp.text.startswith("http"):
                return resp.text.strip()
    except Exception as e:
        print(f"⚠️ Erro ao enviar foto para o servidor: {e}")
    return None

def gerar_imagem_persona(image_prompt=None, filename="post_imagem.jpg"):
    """
    Seleciona uma foto exclusiva da Aline correndo em Porto Alegre (Orla, Redenção, Pontal),
    faz o upload seguro e entrega a URL pronta para a API do Instagram.
    """
    # Escolhe uma das fotos da Aline em Porto Alegre
    fotos_disponiveis = [f for f in FOTOS_ALINE_POA if os.path.exists(f)]
    if not fotos_disponiveis:
        # Fallback caso os arquivos locais não existam
        fotos_disponiveis = [
            "https://images.unsplash.com/photo-1594882645126-14020914d58d?q=80&w=1080&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1461896836934-ffe607ba8211?q=80&w=1080&auto=format&fit=crop"
        ]
        escolhida = random.choice(fotos_disponiveis)
        return escolhida, None

    foto_escolhida = random.choice(fotos_disponiveis)
    print(f"📸 Selecionada foto da Aline em Porto Alegre: {os.path.basename(foto_escolhida)}")
    
    print("☁️ Preparando link em alta definição para o Instagram...")
    cdn_url = fazer_upload_cdn(foto_escolhida)
    if cdn_url:
        print(f"✅ Foto pronta para publicação: {cdn_url}")
        return cdn_url, foto_escolhida
    
    return None, foto_escolhida
