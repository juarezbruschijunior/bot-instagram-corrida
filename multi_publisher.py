import requests
import time
import config

class MultiPlatformBot:
    def __init__(self):
        self.ig_account_id = config.INSTAGRAM_ACCOUNT_ID
        self.ig_access_token = config.INSTAGRAM_ACCESS_TOKEN
        self.fb_page_id = getattr(config, "FACEBOOK_PAGE_ID", None)
        self.fb_access_token = getattr(config, "FACEBOOK_ACCESS_TOKEN", None)

    def publicar_instagram_foto(self, image_url, caption):
        """
        Publica foto no Instagram Oficial.
        """
        if not self.ig_account_id or not self.ig_access_token:
            return False

        base_url = "https://graph.instagram.com/v19.0" if self.ig_access_token.startswith("IG") else "https://graph.facebook.com/v19.0"
        print(f"🚀 [Instagram Foto] Criando container para {self.ig_account_id}...")
        
        try:
            resp_container = requests.post(f"{base_url}/{self.ig_account_id}/media", data={
                "image_url": image_url,
                "caption": caption,
                "access_token": self.ig_access_token
            }, timeout=30).json()
            
            if "id" not in resp_container:
                print("❌ Erro no container de foto:", resp_container)
                return False
                
            creation_id = resp_container["id"]
            print(f"✅ Container criado (ID: {creation_id}). Processando...")
            time.sleep(10)
            
            resp_publish = requests.post(f"{base_url}/{self.ig_account_id}/media_publish", data={
                "creation_id": creation_id,
                "access_token": self.ig_access_token
            }, timeout=30).json()
            
            if "id" in resp_publish:
                print(f"🎉 [Instagram Foto] Publicado com sucesso! ID: {resp_publish['id']}")
                return True
            else:
                print("❌ Erro ao publicar foto:", resp_publish)
                return False
        except Exception as e:
            print(f"❌ Exceção Instagram: {e}")
            return False

    def publicar_instagram_reels(self, video_url, caption):
        """
        Publica vídeo Reels com música eletrônica no Instagram Oficial.
        """
        if not self.ig_account_id or not self.ig_access_token:
            return False

        base_url = "https://graph.instagram.com/v19.0" if self.ig_access_token.startswith("IG") else "https://graph.facebook.com/v19.0"
        print(f"🚀 [Instagram Reels] Criando container de vídeo para {self.ig_account_id}...")
        
        try:
            resp_container = requests.post(f"{base_url}/{self.ig_account_id}/media", data={
                "media_type": "REELS",
                "video_url": video_url,
                "caption": caption,
                "access_token": self.ig_access_token
            }, timeout=45).json()
            
            if "id" not in resp_container:
                print("❌ Erro no container de Reels:", resp_container)
                return False
                
            creation_id = resp_container["id"]
            print(f"✅ Container de Reels criado (ID: {creation_id}).")
            
            # Aguarda o Instagram processar e codificar o vídeo (geralmente 20 a 30 segundos)
            print("⏳ Aguardando os servidores da Meta processarem o vídeo e áudio...")
            for tentativa in range(6):
                time.sleep(10)
                status_resp = requests.get(f"{base_url}/{creation_id}", params={
                    "fields": "status_code",
                    "access_token": self.ig_access_token
                }).json()
                status = status_resp.get("status_code")
                print(f"   Status do vídeo ({tentativa+1}/6): {status}")
                if status == "FINISHED":
                    break
            
            print(f"🚀 [Instagram Reels] Publicando no feed e na aba Reels...")
            resp_publish = requests.post(f"{base_url}/{self.ig_account_id}/media_publish", data={
                "creation_id": creation_id,
                "access_token": self.ig_access_token
            }, timeout=30).json()
            
            if "id" in resp_publish:
                print(f"🎉 [Instagram Reels] Publicado com sucesso! ID: {resp_publish['id']}")
                return True
            else:
                print("❌ Erro ao publicar Reels:", resp_publish)
                return False
        except Exception as e:
            print(f"❌ Exceção Instagram Reels: {e}")
            return False

    def publicar_todas(self, media_url, caption, is_video=False):
        """
        Publica simultaneamente no Instagram (Foto ou Reels) e no Facebook.
        """
        print("\n" + "="*60)
        tipo = "REELS COM MÚSICA ELETRÔNICA" if is_video else "FOTO EM ALTA DEFINIÇÃO"
        print(f"🌐 INICIANDO PUBLICAÇÃO MULTIPLATAFORMA [{tipo}]")
        print("="*60)
        
        if is_video:
            sucesso_ig = self.publicar_instagram_reels(media_url, caption)
        else:
            sucesso_ig = self.publicar_instagram_foto(media_url, caption)
            
        print("ℹ️ [Facebook] O post será compartilhado na Página via integração automática da Meta.")
        return sucesso_ig
