# 🏃‍♀️ Bot de Divulgação Automática no Instagram (Planilha de Corrida)

Este bot foi criado e configurado para você. Ele opera uma **persona de criadora de conteúdo / corredora de rua** que publica dicas de treino de corrida, fotos fotorrealistas geradas por IA e faz a chamada para ação (CTA) direcionando para a sua **Planilha de Corrida**.

---

## 📁 Estrutura dos Arquivos

* `main.py` — O agendador principal que roda nos horários de pico (06:30, 12:15, 18:45).
* `content_generator.py` — Gera as legendas com dicas de pace, periodização, prevenção de lesões e prompts de imagem.
* `image_generator.py` — Gera as fotos fotorrealistas em alta definição (proporção 4:5 ideal para o feed do Instagram).
* `instagram_publisher.py` — Envia e publica automaticamente via Instagram Graph API.
* `iniciar_bot.bat` — Atalho para iniciar o bot com 2 cliques no Windows.
* `.env` — Arquivo onde você coloca suas chaves de acesso.
* `posts_gerados/` — Pasta onde ficam salvas cópias de todas as fotos geradas para você conferir.

---

## 🚀 Como Usar

### 1. Testar Imediatamente
Abra o terminal na pasta ou dê dois cliques em `iniciar_bot.bat`. Para testar a geração de um post avulso imediatamente, execute:
```bash
python main.py --test
```

### 2. Ativar a Publicação Real no seu Instagram
Atualmente o bot está em **Modo de Demonstração/Simulação** (ele gera o texto e a foto, salva na pasta `posts_gerados`, mas não envia para a rede social porque falta a sua chave de conta).

Para publicar direto no seu perfil do Instagram:
1. Abra o arquivo `.env` com o bloco de notas.
2. Preencha os campos:
   * `INSTAGRAM_ACCOUNT_ID`: ID da sua conta profissional no Instagram.
   * `INSTAGRAM_ACCESS_TOKEN`: Token de acesso gerado no Meta for Developers.
   * `LINK_PLANILHA`: O link da sua página/planilha.
3. Salve o arquivo e inicie o bot (`iniciar_bot.bat`).
