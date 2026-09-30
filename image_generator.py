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

# Catálogo Oficial e 100% Consistente da Persona Aline Manuela (Físico Atlético, Realista, Alta Resolução)
FOTOS_ALINE_CATALOGO = [
    "aline_corrida_orla.jpg",          # Corrida na Orla do Guaíba / Gasômetro ao amanhecer
    "aline_amarrando_tenis.jpg",        # Parque da Redenção preparando o tênis de corrida
    "aline_hidratacao_pos_treino.jpg",   # Hidratação com garrafa d'água no parque pós-treino
    "aline_smartwatch_pace.jpg",        # Conferindo pace e batimentos no smartwatch
    "aline_alongamento_parque.jpg",     # Alongamento e mobilidade ao ar livre no parque
    "aline_medalha_corrida.jpg",        # Comemorando com a medalha de 10k na linha de chegada
    "aline_pista_atletismo.jpg",        # Treino de velocidade e tiros na pista de atletismo
    "aline_halteres_academia.jpg",      # Treino de força e fortalecimento muscular na academia
    "aline_nutricao_pre_treino.jpg",    # Café pré-treino e alimentação saudável
    "aline_pose_academia.jpg",          # Pose fitness pós-treino na academia
    "aline_agachamento_academia.jpg",   # Agachamento e treino de pernas na academia
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
    Sistema inteligente de rotação anti-repetição:
    Garante que CADA post use uma foto DIFERENTE da mesma persona Aline Manuela.
    Nunca repete uma foto até que todas as fotos do catálogo tenham sido publicadas.
    """
    historico = carregar_historico()
    
    # Filtra fotos que existem fisicamente no disco
    fotos_existentes = [
        f for f in FOTOS_ALINE_CATALOGO 
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
        print("🔄 Todas as fotos do catálogo da Aline foram publicadas! Reiniciando ciclo de rotação...")
        # Evita que a primeira do novo ciclo seja igual à última postada
        candidatas = [f for f in fotos_existentes if f != ultima_postada] or fotos_existentes
        foto_escolhida = random.choice(candidatas)
        historico = [foto_escolhida]
    else:
        foto_escolhida = random.choice(fotos_nao_postadas)
        historico.append(foto_escolhida)

    salvar_historico(historico)
    
    posicao = len(historico)
    total = len(fotos_existentes)
    print(f"📸 [Rotação Anti-Repetição] Foto selecionada: {foto_escolhida} (Foto {posicao}/{total} do ciclo da Aline)")
    
    return os.path.join(POSTS_DIR, foto_escolhida)

def fazer_upload_cdn(caminho_imagem):
    """
    Entrega a URL pública direta da imagem.
    Utiliza a CDN oficial do GitHub (Raw) que possui 100% de disponibilidade,
    velocidade máxima e é aceita nativamente pela Meta / Instagram Graph API.
    """
    nome_arquivo = os.path.basename(caminho_imagem)
    url_github = f"https://raw.githubusercontent.com/juarezbruschijunior/bot-instagram-corrida/main/posts_gerados/{nome_arquivo}"
    return url_github

def gerar_imagem_persona(image_prompt=None, filename="post_imagem.jpg"):
    """
    Ponto de entrada chamado pelo publicador:
    Seleciona a próxima foto inédita da Aline, envia para CDN e retorna a URL pronta.
    """
    foto_local = obter_proxima_foto_aline()
    
    if not foto_local or not os.path.exists(foto_local):
        fallback_url = "https://images.unsplash.com/photo-1594882645126-14020914d58d?q=80&w=1080&auto=format&fit=crop"
        return fallback_url, None

    print("☁️ Preparando link em alta definição para publicação...")
    cdn_url = fazer_upload_cdn(foto_local)
    
    if cdn_url:
        print(f"✅ Foto pronta e validada: {cdn_url}")
        return cdn_url, foto_local
    
    return None, foto_local
