import os
import sys
import json
import requests
import random
import time

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

BOT_DIR = os.path.dirname(__file__)
POSTS_DIR = os.path.join(BOT_DIR, "posts_gerados")
HISTORICO_FILE = os.path.join(BOT_DIR, "historico_fotos_postadas.json")

os.makedirs(POSTS_DIR, exist_ok=True)

# Catálogo de Curiosidades do Cinema & Séries com a Apresentadora Oficial e Pôsteres
FOTOS_CINEMA_CATALOGO = [
    # 🎬 BASTIDORES & CURIOSIDADES COM A APRESENTADORA E CENAS CLÁSSICAS
    "cinema_star_trek_apresentadora.jpg",  # Star Trek - O Beijo Histórico que desafiou a censura
    "cinema_interestelar.jpg",             # Interestelar - A física real do buraco negro
    
    # 🏃‍♀️ GALERIA FITNESS & LIFESTYLE DA APRESENTADORA
    "aline_selfie_espelho_academia.jpg",
    "aline_pose_orla_lifestyle.jpg",
    "aline_corrida_orla.jpg",
    "aline_prato_saudavel_almoco.jpg",
    "aline_smoothie_preparacao.jpg",
    "aline_esteira_academia.jpg",
    "aline_cafe_da_manha_panqueca.jpg",
    "aline_musculacao_leg_press.jpg",
    "aline_medalha_corrida.jpg",
    "aline_remada_baixa_costas.jpg",
    "aline_prancha_abdominal.jpg",
    "aline_smartwatch_pace.jpg",
    "aline_pose_calcadao_fit.jpg",
    "aline_pos_treino_relax.jpg",
]

def carregar_historico():
    """Carrega o histórico de fotos já publicadas."""
    if os.path.exists(HISTORICO_FILE):
        try:
            with open(HISTORICO_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    return []

def salvar_historico(historico):
    """Salva a lista atualizada de fotos publicadas."""
    try:
        with open(HISTORICO_FILE, "w", encoding="utf-8") as f:
            json.dump(historico, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"⚠️ Erro ao salvar histórico de fotos: {e}")

def obter_proxima_foto_aline():
    """
    Sistema inteligente de rotação anti-repetição para Cinema & Séries.
    Garante que CADA post use uma foto/pôster DIFERENTE da apresentadora e das curiosidades.
    """
    historico = carregar_historico()
    
    # Filtra fotos que existem fisicamente no disco
    fotos_existentes = [
        f for f in FOTOS_CINEMA_CATALOGO 
        if os.path.exists(os.path.join(POSTS_DIR, f))
    ]
    
    if not fotos_existentes:
        print("⚠️ Nenhuma foto do catálogo encontrada localmente em posts_gerados.")
        return None

    # Fotos que ainda não foram postadas no ciclo atual
    fotos_nao_postadas = [f for f in fotos_existentes if f not in historico]

    # Se todas as fotos do catálogo já foram postadas, reinicia o ciclo
    if not fotos_nao_postadas:
        ultima_postada = historico[-1] if historico else None
        print("🔄 Todas as fotos do catálogo foram publicadas! Reiniciando ciclo de rotação...")
        candidatas = [f for f in fotos_existentes if f != ultima_postada] or fotos_existentes
        foto_escolhida = random.choice(candidatas)
        historico = [foto_escolhida]
    else:
        # Se for o início, prioriza as novas de cinema
        if "cinema_star_trek_apresentadora.jpg" in fotos_nao_postadas:
            foto_escolhida = "cinema_star_trek_apresentadora.jpg"
        else:
            foto_escolhida = random.choice(fotos_nao_postadas)
        historico.append(foto_escolhida)

    salvar_historico(historico)
    
    posicao = len(historico)
    total = len(fotos_existentes)
    print(f"📸 [Rotação Anti-Repetição Cinema] Foto selecionada: {foto_escolhida} (Post {posicao}/{total} do ciclo)")
    
    return os.path.join(POSTS_DIR, foto_escolhida)

def fazer_upload_cdn(caminho_imagem):
    """
    Entrega a URL pública direta da imagem via GitHub Raw CDN.
    """
    nome_arquivo = os.path.basename(caminho_imagem)
    url_github = f"https://raw.githubusercontent.com/juarezbruschijunior/bot-instagram-corrida/main/posts_gerados/{nome_arquivo}"
    return url_github

def gerar_imagem_persona(image_prompt=None, filename="post_imagem.jpg"):
    """
    Ponto de entrada chamado pelo publicador:
    Seleciona a próxima foto inédita de cinema/apresentadora, envia para CDN e retorna a URL pronta.
    """
    foto_local = obter_proxima_foto_aline()
    
    if not foto_local or not os.path.exists(foto_local):
        fallback_url = "https://raw.githubusercontent.com/juarezbruschijunior/bot-instagram-corrida/main/posts_gerados/cinema_star_trek_apresentadora.jpg"
        return fallback_url, None

    print("☁️ Preparando link em alta definição para publicação...")
    cdn_url = fazer_upload_cdn(foto_local)
    
    if cdn_url:
        print(f"✅ Foto pronta e validada: {cdn_url}")
        return cdn_url, foto_local
    
    return None, foto_local
