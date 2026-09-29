import sys
import os
from instagrapi import Client

SESSION_FILE = os.path.join(os.path.dirname(__file__), "session_instagram.json")

def login(code=None):
    cl = Client()
    username = "alin_emanuela"
    password = "3495242Luc@s"
    
    print(f"🔑 Tentando login para @{username}...")
    try:
        if code:
            cl.login(username, password, verification_code=code.strip())
        else:
            cl.login(username, password)
            
        cl.dump_settings(SESSION_FILE)
        print(f"🎉 LOGIN CONCLUÍDO COM SUCESSO! User ID: {cl.user_id}")
        print(f"💾 Sessão salva permanentemente em {SESSION_FILE}")
        return True
    except Exception as e:
        print(f"❌ Erro no login: {e}")
        return False

if __name__ == "__main__":
    code_arg = sys.argv[1] if len(sys.argv) > 1 else None
    login(code_arg)
