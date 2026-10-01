import sys
import os
import json
import random

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

BOT_DIR = os.path.dirname(__file__)
HISTORICO_CINEMA_FILE = os.path.join(BOT_DIR, "historico_posts_cinema.json")
DB_CINEMA_FILE = os.path.join(BOT_DIR, "database_cinema_100.json")

def carregar_pacote_cinema():
    if os.path.exists(DB_CINEMA_FILE):
        try:
            with open(DB_CINEMA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                if data and isinstance(data, list):
                    return data
        except Exception as e:
            print(f"⚠️ Erro ao carregar database_cinema_100.json: {e}")
    return []

PACOTE_POSTS_CINEMA = carregar_pacote_cinema()

def carregar_historico_cinema():
    if os.path.exists(HISTORICO_CINEMA_FILE):
        try:
            with open(HISTORICO_CINEMA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    return []

def salvar_historico_cinema(historico):
    try:
        with open(HISTORICO_CINEMA_FILE, "w", encoding="utf-8") as f:
            json.dump(historico, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"⚠️ Erro ao salvar histórico cinema: {e}")

def obter_proximo_post_cinema():
    """
    Garante que CADA publicação seja um FILME/SÉRIE DIFERENTE com IMAGEM e LEGENDA 100% SINCRONIZADAS.
    Nunca repete até que todos os 104 filmes do catálogo tenham sido postados (mais de 26 dias sem repetição)!
    """
    global PACOTE_POSTS_CINEMA
    if not PACOTE_POSTS_CINEMA:
        PACOTE_POSTS_CINEMA = carregar_pacote_cinema()
        
    historico = carregar_historico_cinema()
    
    # Filtra posts que ainda não foram publicados no ciclo atual
    posts_disponiveis = [p for p in PACOTE_POSTS_CINEMA if p["id"] not in historico]
    
    if not posts_disponiveis:
        print("🔄 Todos os 104 filmes do catálogo foram publicados! Reiniciando ciclo de rotação...")
        ultimo_id = historico[-1] if historico else None
        candidatos = [p for p in PACOTE_POSTS_CINEMA if p["id"] != ultimo_id] or PACOTE_POSTS_CINEMA
        post_escolhido = random.choice(candidatos)
        historico = [post_escolhido["id"]]
    else:
        post_escolhido = posts_disponiveis[0] # Segue fila sequencial ordenada
        historico.append(post_escolhido["id"])

    salvar_historico_cinema(historico)
    
    pos = len(historico)
    total = len(PACOTE_POSTS_CINEMA)
    print(f"🎬 [Fila Cinema 100+ Anti-Repetição] Filme: {post_escolhido['filme']} (Post {pos}/{total} do ciclo)")
    
    return post_escolhido

def gerar_post_e_prompt(tema=None):
    post = obter_proximo_post_cinema()
    return post
