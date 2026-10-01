import sys
import os
import time
import datetime
import json
import threading
import requests
from http.server import HTTPServer, BaseHTTPRequestHandler

# Garante envio imediato de logs para a tela do Render e suporte UTF-8
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', line_buffering=True)

# Desativa o modo de seleção do Windows que congela o script ao clicar no console
try:
    import ctypes
    kernel32 = ctypes.windll.kernel32
    h_in = kernel32.GetStdHandle(-10) # STD_INPUT_HANDLE
    mode = ctypes.c_ulong()
    kernel32.GetConsoleMode(h_in, ctypes.byref(mode))
    mode.value = (mode.value & ~0x0040) | 0x0080
    kernel32.SetConsoleMode(h_in, mode)
except Exception:
    pass

BOT_DIR = os.path.dirname(__file__)
SLOTS_FILE = os.path.join(BOT_DIR, "historico_slots_postagens.json")

def obter_hora_brasilia():
    """Retorna o horário atual exato de Brasília (UTC-3) independente do fuso do servidor."""
    try:
        from zoneinfo import ZoneInfo
        return datetime.datetime.now(ZoneInfo('America/Sao_Paulo'))
    except Exception:
        tz_br = datetime.timezone(datetime.timedelta(hours=-3))
        return datetime.datetime.now(tz_br)

def carregar_slots_executados():
    if os.path.exists(SLOTS_FILE):
        try:
            with open(SLOTS_FILE, "r", encoding="utf-8") as f:
                return set(json.load(f))
        except Exception:
            return set()
    return set()

def salvar_slots_executados(slots):
    try:
        # Mantém apenas os últimos 50 slots no histórico para não crescer indefinidamente
        slots_lista = list(slots)[-50:]
        with open(SLOTS_FILE, "w", encoding="utf-8") as f:
            json.dump(slots_lista, f, indent=2)
    except Exception as e:
        print(f"⚠️ Erro ao salvar histórico de slots: {e}")

class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/media/"):
            filename = self.path[len("/media/"):].split("?")[0]
            path_posts = os.path.join(BOT_DIR, "posts_gerados", filename)
            path_reels = os.path.join(BOT_DIR, "reels_gerados", filename)
            
            target_path = None
            if os.path.exists(path_posts):
                target_path = path_posts
            elif os.path.exists(path_reels):
                target_path = path_reels
                
            if target_path and os.path.isfile(target_path):
                self.send_response(200)
                if filename.lower().endswith((".jpg", ".jpeg")):
                    self.send_header('Content-type', 'image/jpeg')
                elif filename.lower().endswith(".png"):
                    self.send_header('Content-type', 'image/png')
                elif filename.lower().endswith(".mp4"):
                    self.send_header('Content-type', 'video/mp4')
                else:
                    self.send_header('Content-type', 'application/octet-stream')
                self.send_header('Content-Length', str(os.path.getsize(target_path)))
                self.end_headers()
                with open(target_path, "rb") as f:
                    self.wfile.write(f.read())
                return
            else:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b"Arquivo nao encontrado")
                return

        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        hora_atual = obter_hora_brasilia().strftime('%d/%m/%Y %H:%M:%S')
        self.wfile.write(f"Bot Cinema 24/7 Ativo e Rodando! Horario Brasilia: {hora_atual}".encode('utf-8'))

    def log_message(self, format, *args):
        return # Silencia logs de requisicoes HTTP rotineiras

def iniciar_servidor_web():
    porta = int(os.environ.get("PORT", 10000))
    try:
        server = HTTPServer(("0.0.0.0", porta), HealthCheckHandler)
        print(f"🌐 Servidor Web ativo na porta {porta}!")
        server.serve_forever()
    except Exception as e:
        print(f"⚠️ Aviso servidor web: {e}")

def keep_alive_worker():
    """Envia auto-ping a cada 8 minutos para evitar que o servidor no Render entre em modo de suspensão."""
    render_url = os.environ.get("RENDER_EXTERNAL_URL", "https://bot-instagram-corrida.onrender.com")
    while True:
        time.sleep(480) # 8 minutos
        try:
            requests.get(render_url, timeout=10)
        except Exception:
            pass

from content_generator import gerar_post_e_prompt
from image_generator import gerar_imagem_persona
from reels_generator import gerar_reels_com_musica
from multi_publisher import MultiPlatformBot
from comment_responder import verificar_e_responder_comentarios

def executar_ciclo_postagem(forcar_reels=False):
    agora_br = obter_hora_brasilia().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n[{agora_br}] 🎬 Iniciando ciclo de publicação de Cinema & Séries...")
    
    # 1. Seleciona o Próximo Filme Inédito da Fila (Anti-Repetição)
    post_pacote = gerar_post_e_prompt()
    legenda = post_pacote["caption"]
    nome_imagem = post_pacote.get("imagem", "cinema_star_trek_apresentadora.jpg")
    
    image_url = f"https://raw.githubusercontent.com/juarezbruschijunior/bot-instagram-corrida/main/posts_gerados/{nome_imagem}"
    
    print(f"🎬 [Cinema Selecionado] {post_pacote.get('filme', 'Filme')} | Imagem: {nome_imagem}")
    print(f"☁️ Link CDN em Alta Definição: {image_url}")
    
    bot = MultiPlatformBot()
    sucesso = bot.publicar_todas(image_url, legenda, is_video=False)
    
    if sucesso:
        print(f"[{agora_br}] ✅ Publicação de Cinema concluída com sucesso no Instagram!\n")
    else:
        print(f"[{agora_br}] ❌ Falha no ciclo de postagem.\n")
    return sucesso

HORARIOS_POSTAGEM = ["08:30", "12:30", "17:30", "21:15"]

def loop_agendamento_brasilia():
    slots_executados = carregar_slots_executados()
    ultimo_check_comentarios = 0
    
    print("\n🚀 [Scheduler Brasília] Mecanismo de Agendamento Ativo e Monitorando...")
    
    while True:
        try:
            agora = obter_hora_brasilia()
            hoje_str = agora.strftime("%Y-%m-%d")
            hora_min_str = agora.strftime("%H:%M")
            minutos_agora = agora.hour * 60 + agora.minute
            
            # 1. Checa Horários de Postagens (4x ao dia)
            for h_str in HORARIOS_POSTAGEM:
                slot_id = f"{hoje_str}_{h_str}"
                
                if slot_id not in slots_executados:
                    alvo_h, alvo_m = map(int, h_str.split(":"))
                    minutos_alvo = alvo_h * 60 + alvo_m
                    diferenca = minutos_agora - minutos_alvo
                    
                    # Se atingiu o horário exato ou está dentro da janela de até 20 minutos após o horário
                    if 0 <= diferenca <= 20:
                        print(f"\n⏰ [HORÁRIO ATINGIDO: {h_str} BRT] Disparando postagem agendada de Cinema!")
                        slots_executados.add(slot_id)
                        salvar_slots_executados(slots_executados)
                        executar_ciclo_postagem()
            
            # 2. Checa Auto-Resposta de Comentários a cada 30 minutos
            tempo_atual = time.time()
            if tempo_atual - ultimo_check_comentarios >= 1800: # 30 min
                ultimo_check_comentarios = tempo_atual
                print(f"\n🔍 [{agora.strftime('%H:%M:%S')}] Verificando comentários para responder...")
                try:
                    verificar_e_responder_comentarios()
                except Exception as e:
                    print(f"⚠️ Erro ao verificar comentários: {e}")
                    
        except Exception as e:
            print(f"⚠️ Erro no loop de agendamento: {e}")
            
        time.sleep(20) # Checa a cada 20 segundos

def main():
    print("="*65)
    print(" 🎬 BOT DE CURIOSIDADES DO CINEMA & SÉRIES (4X AO DIA)")
    print("="*65)
    
    # Flags de teste manual
    if "--reels" in sys.argv:
        print("🔍 Modo de teste de REELS selecionado.")
        executar_ciclo_postagem(forcar_reels=True)
        return

    if "--test" in sys.argv or "-t" in sys.argv:
        print("🔍 Modo de teste imediato de postagem selecionado.")
        executar_ciclo_postagem()
        return

    if "--cron" in sys.argv:
        print("🔍 Modo CRON / GitHub Actions selecionado.")
        agora = obter_hora_brasilia()
        hoje_str = agora.strftime("%Y-%m-%d")
        minutos_agora = agora.hour * 60 + agora.minute
        slots_executados = carregar_slots_executados()
        
        postou = False
        for h_str in HORARIOS_POSTAGEM:
            slot_id = f"{hoje_str}_{h_str}"
            if slot_id not in slots_executados:
                alvo_h, alvo_m = map(int, h_str.split(":"))
                minutos_alvo = alvo_h * 60 + alvo_m
                diferenca = minutos_agora - minutos_alvo
                if 0 <= diferenca <= 35: # Janela de 35 minutos para o cron
                    print(f"⏰ [CRON Horário: {h_str} BRT] Disparando postagem agendada!")
                    slots_executados.add(slot_id)
                    salvar_slots_executados(slots_executados)
                    executar_ciclo_postagem()
                    postou = True
                    break
                    
        print("🔍 [CRON] Verificando comentários...")
        try:
            verificar_e_responder_comentarios()
        except Exception as e:
            print(f"⚠️ Erro comentários: {e}")
        return

    # Inicia servidor web em segundo plano para o Render
    threading.Thread(target=iniciar_servidor_web, daemon=True).start()
    # Inicia thread de auto-ping para manter acordado
    threading.Thread(target=keep_alive_worker, daemon=True).start()

    agora_br = obter_hora_brasilia().strftime("%d/%m/%Y %H:%M:%S")
    print(f"\n⏰ [Relógio Sincronizado] Horário de Brasília atual: {agora_br}")
    print("🗓️ Grade de Automações Agendadas (4x ao Dia):")
    print("   🎬 Postagens de Cinema, Séries & Bastidores:")
    print("      👉 08:30 (Café da Manhã / Dica do Dia)")
    print("      👉 12:30 (Pico do Almoço / Curiosidade Rápida)")
    print("      👉 17:30 (Fim de Tarde / Estreias & Bastidores)")
    print("      👉 21:15 (Horário Nobre da Noite / Cineclube)")
    print("   💬 Auto-Resposta de Comentários em Fotos e Reels:")
    print("      👉 A cada 30 minutos (Atendimento ágil 24/7)")
    
    # Verificação inicial de comentários
    try:
        verificar_e_responder_comentarios()
    except Exception as e:
        print(f"⚠️ Aviso na checagem inicial: {e}")

    # Executa o loop principal com horário oficial de Brasília
    loop_agendamento_brasilia()

if __name__ == "__main__":
    main()
