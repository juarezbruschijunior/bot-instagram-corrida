import sys
import os
import time

# Configura Fuso Horário de Brasília (America/Sao_Paulo) para servidores na nuvem
if hasattr(time, 'tzset'):
    os.environ['TZ'] = 'America/Sao_Paulo'
    time.tzset()

import datetime
import random
import schedule

# Garante envio imediato de logs para a tela do Render e suporte UTF-8
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', line_buffering=True)
    
    # Desativa o modo de seleção do Windows que congela o script ao clicar na tela preta
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

import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/media/"):
            filename = self.path[len("/media/"):].split("?")[0]
            bot_dir = os.path.dirname(__file__)
            path_posts = os.path.join(bot_dir, "posts_gerados", filename)
            path_reels = os.path.join(bot_dir, "reels_gerados", filename)
            
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
        self.wfile.write(b"Bot Aline Manuela 24/7 Ativo e Rodando!")
    def log_message(self, format, *args):
        return # Silencia logs de requisicoes HTTP

def iniciar_servidor_web():
    porta = int(os.environ.get("PORT", 10000))
    try:
        server = HTTPServer(("0.0.0.0", porta), HealthCheckHandler)
        print(f"🌐 Servidor Web de monitoramento ativo na porta {porta}!")
        server.serve_forever()
    except Exception as e:
        print(f"⚠️ Aviso servidor web: {e}")

from content_generator import gerar_post_e_prompt
from image_generator import gerar_imagem_persona
from reels_generator import gerar_reels_com_musica
from multi_publisher import MultiPlatformBot
from comment_responder import verificar_e_responder_comentarios

def executar_ciclo_postagem(forcar_reels=False):
    agora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n[{agora}] 🎬 Iniciando ciclo de publicação de Cinema & Séries...")
    
    # 1. Seleciona o Próximo Filme Inédito da Fila (Anti-Repetição)
    post_pacote = gerar_post_e_prompt()
    legenda = post_pacote["caption"]
    nome_imagem = post_pacote.get("imagem", "cinema_star_trek_apresentadora.jpg")
    
    bot_dir = os.path.dirname(__file__)
    local_path = os.path.join(bot_dir, "posts_gerados", nome_imagem)
    image_url = f"https://raw.githubusercontent.com/juarezbruschijunior/bot-instagram-corrida/main/posts_gerados/{nome_imagem}"
    
    print(f"🎬 [Cinema Selecionado] {post_pacote.get('filme', 'Filme')} | Imagem: {nome_imagem}")
    print(f"☁️ Link CDN em Alta Definição: {image_url}")
    
    bot = MultiPlatformBot()
    sucesso = bot.publicar_todas(image_url, legenda, is_video=False)
    
    if sucesso:
        print(f"[{agora}] ✅ Publicação de Cinema concluída com sucesso no Instagram!\n")
    else:
        print(f"[{agora}] ❌ Falha no ciclo de postagem.\n")

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

    if "--responder" in sys.argv or "-r" in sys.argv:
        print("🔍 Modo de verificação de comentários selecionado.")
        verificar_e_responder_comentarios()
        return

    # Inicia servidor web em segundo plano para o Render
    threading.Thread(target=iniciar_servidor_web, daemon=True).start()

    agora_br = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(f"\n⏰ [Relógio Sincronizado] Horário de Brasília atual: {agora_br}")
    print("🗓️ Grade de Automações Agendadas (4x ao Dia):")
    print("   🎬 Postagens de Cinema, Séries & Bastidores:")
    print("      👉 08:30 (Café da Manhã / Dica do Dia)")
    print("      👉 12:30 (Pico do Almoço / Curiosidade Rápida)")
    print("      👉 17:30 (Fim de Tarde / Estreias & Bastidores)")
    print("      👉 21:15 (Horário Nobre da Noite / Cineclube)")
    print("   💬 Auto-Resposta de Comentários em Fotos e Reels:")
    print("      👉 A cada 30 minutos (Atendimento ágil 24/7)")
    
    # 1. Executa verificação inicial de comentários imediatamente na inicialização
    print("\n🔍 Realizando verificação inicial de comentários pendentes...")
    try:
        verificar_e_responder_comentarios()
    except Exception as e:
        print(f"⚠️ Aviso na checagem inicial: {e}")

    # Agendamento de Postagens (4x ao dia)
    schedule.every().day.at("08:30").do(executar_ciclo_postagem)
    schedule.every().day.at("12:30").do(executar_ciclo_postagem)
    schedule.every().day.at("17:30").do(executar_ciclo_postagem)
    schedule.every().day.at("21:15").do(executar_ciclo_postagem)
    
    # Agendamento de Respostas de Comentários (A cada 30 minutos)
    schedule.every(30).minutes.do(verificar_e_responder_comentarios)
    
    print("⏳ Bot de Cinema 100% ativo e aguardando horários agendados de Brasília...")
    
    while True:
        schedule.run_pending()
        time.sleep(30)

if __name__ == "__main__":
    main()
