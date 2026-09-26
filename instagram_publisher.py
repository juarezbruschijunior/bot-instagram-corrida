import requests
import time
import config

class InstagramBot:
    def __init__(self):
        self.account_id = config.INSTAGRAM_ACCOUNT_ID
        self.access_token = config.INSTAGRAM_ACCESS_TOKEN
        # Tokens iniciados em "IGAA" utilizam o endpoint direto graph.instagram.com
        if self.access_token.startswith("IG"):
            self.base_url = "https://graph.instagram.com/v19.0"
        else:
            self.base_url = "https://graph.facebook.com/v19.0"

    def publicar_post(self, image_url, caption):
        """
        Publica uma foto com legenda via API oficial da Meta (Instagram Graph API).
        """
        if not self.account_id or not self.access_token or "SEU_" in self.access_token:
            print("\n" + "="*60)
            print("⚠️ MODO SIMULAÇÃO ATIVADO (Tokens não preenchidos)")
            print("="*60)
            print("Legenda gerada:\n", caption)
            print("URL da Imagem:\n", image_url)
            print("="*60 + "\n")
            return True

        print(f"🚀 [1/2] Criando container de mídia no Instagram para {self.account_id}...")
        url_container = f"{self.base_url}/{self.account_id}/media"
        params_container = {
            "image_url": image_url,
            "caption": caption,
            "access_token": self.access_token
        }
        
        try:
            resp_container = requests.post(url_container, data=params_container, timeout=30).json()
            
            if "id" not in resp_container:
                print("❌ Erro ao criar container de mídia no Instagram:", resp_container)
                return False
                
            creation_id = resp_container["id"]
            print(f"✅ Container criado com sucesso! (ID: {creation_id})")
            print("⏳ Aguardando 10 segundos para processamento da imagem nos servidores do Instagram...")
            time.sleep(10)
            
            print(f"🚀 [2/2] Publicando no feed do Instagram...")
            url_publish = f"{self.base_url}/{self.account_id}/media_publish"
            params_publish = {
                "creation_id": creation_id,
                "access_token": self.access_token
            }
            
            resp_publish = requests.post(url_publish, data=params_publish, timeout=30).json()
            
            if "id" in resp_publish:
                print(f"\n🎉🎉🎉 SUCESSO ABSOLUTO! Post publicado no seu Instagram! ID: {resp_publish['id']} 🎉🎉🎉\n")
                return True
            else:
                print("❌ Erro ao publicar mídia:", resp_publish)
                return False
        except Exception as e:
            print(f"❌ Exceção ao conectar à API do Instagram: {e}")
            return False
