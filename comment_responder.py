import sys
import os
import json
import requests
import config

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

REPLIED_FILE = os.path.join(os.path.dirname(__file__), "comentarios_respondidos.json")

def carregar_comentarios_respondidos():
    if os.path.exists(REPLIED_FILE):
        try:
            with open(REPLIED_FILE, "r", encoding="utf-8") as f:
                return set(json.load(f))
        except Exception:
            return set()
    return set()

def salvar_comentarios_respondidos(respondidos):
    try:
        with open(REPLIED_FILE, "w", encoding="utf-8") as f:
            json.dump(list(respondidos), f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"⚠️ Erro ao salvar histórico de comentários: {e}")

def gerar_resposta_ia(texto_comentario, autor):
    """
    Usa o Google Gemini para criar uma resposta natural, amigável e esportiva.
    """
    if config.GEMINI_API_KEY and "AIza" in config.GEMINI_API_KEY:
        try:
            from google import genai
            client = genai.Client(api_key=config.GEMINI_API_KEY)
            
            prompt = f"""
            Você é {config.PERSONA_NAME}, uma corredora de rua brasileira simpática, motivadora e parceira da BioTools.
            Um seguidor chamado @{autor} acabou de comentar no seu post:
            "{texto_comentario}"
            
            Crie uma resposta curta (1 a 3 frases) com emojis:
            - Seja calorosa e atenciosa.
            - Responda à dúvida ou agradeça o carinho.
            - Se fizer sentido, faça uma pergunta sobre a rotina de corrida dele(a) ou mencione a planilha BioTools (link na bio).
            - Retorne APENAS o texto da resposta.
            """
            
            resp = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt
            )
            if resp and resp.text:
                return resp.text.strip()
        except Exception as e:
            print(f"⚠️ Erro no Gemini ao gerar resposta: {e}")

    # Respostas padrões inteligentes
    respostas_padrao = [
        f"Obrigada pelo carinho, @{autor}! 🏃‍♀️✨ Já treinou hoje ou vai mais tarde? Se precisar de planilha, o link tá na bio!",
        f"Valeu demais, @{autor}! 🔥 Foco nos treinos! Se quiser estruturar suas 4 semanas, dá uma olhada no link da bio!",
        f"Tamo junto na corrida, @{autor}! 👟💨 Bons treinos e qualquer dúvida sobre a planilha me chama!"
    ]
    import random
    return random.choice(respostas_padrao)

def verificar_e_responder_comentarios():
    """
    Busca os posts recentes no Instagram, verifica novos comentários
    e responde usando IA (executado 2 vezes ao dia).
    """
    print("\n💬 [Auto-Responder] Verificando novos comentários nos posts...")
    
    if not config.INSTAGRAM_ACCOUNT_ID or not config.INSTAGRAM_ACCESS_TOKEN:
        print("⚠️ Credenciais do Instagram não configuradas.")
        return

    base_url = "https://graph.instagram.com/v19.0" if config.INSTAGRAM_ACCESS_TOKEN.startswith("IG") else "https://graph.facebook.com/v19.0"
    respondidos = carregar_comentarios_respondidos()
    
    # 1. Buscar os últimos posts da conta
    url_media = f"{base_url}/{config.INSTAGRAM_ACCOUNT_ID}/media"
    params_media = {
        "fields": "id,caption",
        "access_token": config.INSTAGRAM_ACCESS_TOKEN,
        "limit": 5
    }
    
    try:
        resp_media = requests.get(url_media, params=params_media, timeout=20).json()
        posts = resp_media.get("data", [])
        
        if not posts:
            print("ℹ️ Nenhum post recente encontrado.")
            return

        novos_respondidos = 0
        
        for post in posts:
            post_id = post["id"]
            # 2. Buscar comentários de cada post
            url_comments = f"{base_url}/{post_id}/comments"
            params_comments = {
                "fields": "id,text,username,timestamp",
                "access_token": config.INSTAGRAM_ACCESS_TOKEN
            }
            
            resp_comments = requests.get(url_comments, params=params_comments, timeout=20).json()
            comentarios = resp_comments.get("data", [])
            
            for c in comentarios:
                c_id = c["id"]
                c_text = c.get("text", "")
                c_user = c.get("username", "")
                
                # Não responder a si mesmo nem comentários já respondidos
                if c_user == "alin_emanuela" or c_id in respondidos:
                    continue
                
                print(f"📝 Novo comentário de @{c_user}: '{c_text}'")
                texto_resposta = gerar_resposta_ia(c_text, c_user)
                
                # 3. Enviar resposta oficial via API
                url_reply = f"{base_url}/{c_id}/replies"
                params_reply = {
                    "message": texto_resposta,
                    "access_token": config.INSTAGRAM_ACCESS_TOKEN
                }
                
                resp_reply = requests.post(url_reply, data=params_reply, timeout=20).json()
                
                if "id" in resp_reply:
                    print(f"✅ Resposta enviada para @{c_user}: '{texto_resposta}'")
                    respondidos.add(c_id)
                    novos_respondidos += 1
                else:
                    print(f"❌ Erro ao enviar resposta: {resp_reply}")
        
        salvar_comentarios_respondidos(respondidos)
        print(f"💬 [Auto-Responder] Concluído! {novos_respondidos} novo(s) comentário(s) respondido(s).\n")

    except Exception as e:
        print(f"❌ Exceção ao checar comentários: {e}")

if __name__ == "__main__":
    verificar_e_responder_comentarios()
