import os
import random
import requests
from PIL import Image
import PIL.Image

# Compatibilidade Pillow 10+
if not hasattr(PIL.Image, 'ANTIALIAS'):
    PIL.Image.ANTIALIAS = PIL.Image.Resampling.LANCZOS

from moviepy.editor import ImageClip, AudioFileClip

BOT_DIR = os.path.dirname(__file__)
POSTS_DIR = os.path.join(BOT_DIR, "posts_gerados")
AUDIO_DIR = os.path.join(BOT_DIR, "audios_fitness")
REELS_DIR = os.path.join(BOT_DIR, "reels_gerados")

os.makedirs(REELS_DIR, exist_ok=True)

def fazer_upload_cdn_video(caminho_video):
    """
    Faz upload temporário do vídeo MP4 para obter o link público direto
    exigido pelos servidores da Meta / Instagram Graph API.
    """
    try:
        url = "https://catbox.moe/user/api.php"
        with open(caminho_video, "rb") as f:
            files = {"fileToUpload": f}
            data = {"reqtype": "fileupload"}
            resp = requests.post(url, files=files, data=data, timeout=60)
            if resp.status_code == 200 and resp.text.startswith("http"):
                return resp.text.strip()
    except Exception as e:
        print(f"⚠️ Erro ao enviar vídeo para o servidor: {e}")
    return None

def gerar_reels_com_musica(caminho_foto, duracao=8):
    """
    Transforma a foto da Aline em um Reels vertical (1080x1920) com
    trilha sonora eletrônica fitness animada.
    """
    print("🎬 [Reels] Montando vídeo vertical com música eletrônica de corrida...")
    
    # 1. Enquadrar imagem no formato vertical de Reels (9:16 / 1080x1920)
    pil_img = Image.open(caminho_foto)
    target_w, target_h = 1080, 1920
    scale = max(target_w / pil_img.width, target_h / pil_img.height)
    new_w = int(pil_img.width * scale)
    new_h = int(pil_img.height * scale)
    
    pil_resized = pil_img.resize((new_w, new_h), Image.Resampling.LANCZOS)
    left = (new_w - target_w) // 2
    top = (new_h - target_h) // 2
    pil_cropped = pil_resized.crop((left, top, left + target_w, top + target_h))
    
    temp_frame = os.path.join(REELS_DIR, "frame_temp.jpg")
    pil_cropped.save(temp_frame, quality=95)
    
    # 2. Selecionar áudio eletrônico fitness
    audios = [os.path.join(AUDIO_DIR, f) for f in os.listdir(AUDIO_DIR) if f.endswith(".mp3")]
    audio_path = audios[0] if audios else None
    
    # 3. Montar clipe de vídeo com áudio
    clip = ImageClip(temp_frame).set_duration(duracao)
    
    if audio_path and os.path.exists(audio_path):
        start_time = random.randint(10, 40)
        audio = AudioFileClip(audio_path).subclip(start_time, start_time + duracao).audio_fadeout(1)
        clip = clip.set_audio(audio)
    
    out_filename = f"reels_{random.randint(1000, 9999)}.mp4"
    out_path = os.path.join(REELS_DIR, out_filename)
    
    clip.write_videofile(out_path, fps=24, codec="libx264", audio_codec="aac", logger=None)
    print(f"✅ Vídeo Reels renderizado com sucesso: {out_path}")
    
    # 4. Upload para CDN público direto
    print("☁️ Preparando link do Reels (.mp4) para o Instagram...")
    cdn_video_url = fazer_upload_cdn_video(out_path)
    
    return cdn_video_url, out_path
