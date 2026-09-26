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
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(b"Bot Aline Manuela 24/7 Ativo e Rodando!")
    def log_message(self, format, *args):
        return # Silencia logs de requisições HTTP

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
    print(f"\n[{agora}] 🏃‍♀️ Iniciando ciclo de publicação do post...")
    
    # 1. Gerar Conteúdo Persuasivo com Gemini
    print("1️⃣ Gerando legenda estratégica e dicas com o Google Gemini IA...")
    conteudo = gerar_post_e_prompt()
    legenda = conteudo["caption"]
    
    # 2. Selecionar Foto da Aline em Porto Alegre
    print("2️⃣ Selecionando foto exclusiva da Aline em Porto Alegre...")
    nome_arquivo = f"post_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
    image_url, local_path = gerar_imagem_persona(filename=nome_arquivo)
    
    # Alterna entre Foto e Reels (Vídeo com Música Eletrônica Fitness)
    # Por padrão, os posts da tarde/noite (ou com flag) viram Reels com música!
    hora_atual = datetime.datetime.now().hour
    postar_como_reels = forcar_reels or (hora_atual >= 12 and random.random() > 0.3)
    
    bot = MultiPlatformBot()
    
    if postar_como_reels and local_path:
        print("🎬 [Modo Vídeo Reels] Gerando vídeo com batida eletrônica fitness...")
        video_url, video_local = gerar_reels_com_musica(local_path, duracao=8)
        if video_url:
            sucesso = bot.publicar_todas(video_url, legenda, is_video=True)
        else:
            sucesso = bot.publicar_todas(image_url, legenda, is_video=False)
    else:
        sucesso = bot.publicar_todas(image_url, legenda, is_video=False)
    
    if sucesso:
        print(f"[{agora}] ✅ Publicação concluída com sucesso nas redes!\n")
    else:
        print(f"[{agora}] ❌ Falha no ciclo de postagem.\n")

def main():
    print("="*65)
    print(" 🏃‍♀️ BOT DE DIVULGAÇÃO & ATENDIMENTO (FOTOS + REELS COM MÚSICA)")
    print("="*65)
    
    # Flags de teste manual
    if "--reels" in sys.argv:
        print("🔍 Modo de teste de REELS COM MÚSICA ELETRÔNICA selecionado.")
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
    print("🗓️ Grade de Automações Agendadas (Instagram & Facebook):")
    print("   📸 Postagens de Fotos & Reels com Trilha Sonora Eletrônica:")
    print("      👉 06:30 (Pico matinal dos corredores)")
    print("      👉 12:15 (Pico do almoço)")
    print("      👉 18:45 (Pico pós-treino da noite)")
    print("   💬 Auto-Resposta de Comentários em Fotos e Reels (2x ao dia):")
    print("      👉 10:30 (Manhã)")
    print("      👉 19:30 (Noite)")
    
    # 1. Executa verificação inicial de comentários imediatamente na inicialização
    print("\n🔍 Realizando verificação inicial de comentários pendentes...")
    try:
        verificar_e_responder_comentarios()
    except Exception as e:
        print(f"⚠️ Aviso na checagem inicial: {e}")

    # Agendamento de Postagens (3x ao dia)
    schedule.every().day.at("06:30").do(executar_ciclo_postagem)
    schedule.every().day.at("12:15").do(executar_ciclo_postagem)
    schedule.every().day.at("18:45").do(executar_ciclo_postagem)
    
    # Agendamento de Respostas de Comentários (2x ao dia)
    schedule.every().day.at("10:30").do(verificar_e_responder_comentarios)
    schedule.every().day.at("19:30").do(verificar_e_responder_comentarios)
    
    print("⏳ Bot 100% ativo e aguardando horários agendados de Brasília...")
    
    while True:
        schedule.run_pending()
        time.sleep(30)

if __name__ == "__main__":
    main()
