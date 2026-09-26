import json
import random
import config

TEMAS_BIOTOOLS_FOLLOWER_BOOST = [
    {
        "tema": "Como baixar seu Pace nos 5km (Do 6:00 para o 4:50)",
        "caption": """⏱️ Quer baixar seu tempo nos 5km e sair daquele pace travado?

Muita gente acha que para correr mais rápido basta "tentar correr forte" todo dia... Mas a verdade é que isso só traz cansaço e lesão! 

O segredo está em variar os estímulos na semana:
1️⃣ 1x Treino intervalado (tiros curtos de 400m a 800m)
2️⃣ 1x Treino de ritmo / limiar (no ritmo que você quer sustentar na prova)
3️⃣ 1x Rodagem leve regenerativa (para construir base aeróbica)
4️⃣ 1x Longão no fim de semana

📊 Eu controlo todos os meus ritmos na **Planilha da BioTools**. Ela calcula os paces exatos para cada treino e você recebe sua planilha completa de 4 semanas por **apenas R$ 37,90**!

👉 Quer evoluir de verdade? Clique no **link da minha bio** e garanta a sua planilha!
🔗 https://biotoolspremium.com.br/#physiological-tools-section

━━━━━━━━━━━━━━━━━━━━━
🏃‍♀️ **Gostou da dica? Siga @alin_emanuela para receber treinos e motivação diária de corrida de rua!**
📌 *Salve este post para consultar antes do seu treino de amanhã!*
💬 *Me conta aqui nos comentários: qual é o seu pace médio nos 5km hoje?* 👇🔥

#corridaderua #pace5km #treinodecorrida #biotools #planilhadecorrida #portoalegre #corredores #viciadosemcorrida #mulheresquecorrem #loucosporcorrida"""
    },
    {
        "tema": "Adeus Assessoria Cara: Periodização Completa por R$ 37,90",
        "caption": """🏃‍♀️ Você realmente precisa gastar R$ 200/mês em assessoria para ter resultados na corrida?

Muita gente desiste de treinar com método porque acha que assessoria esportiva é inacessível... Mas hoje você pode ter uma **periodização científica de 4 semanas** no seu celular por uma fração desse valor!

💡 Na **BioTools**, você monta a sua planilha personalizada por **apenas R$ 37,90** (menos que uma pizza no fim de semana!).

O que a planilha entrega para você:
✅ Paces exatos de tiro, ritmo e rodagem calculados para o seu nível
✅ Controle de volume semanal para evitar canelite e dor no joelho
✅ Periodização para 5km, 10km, 21km ou emagrecimento
✅ Acesso imediato no celular

👉 Pare de correr no escuro! Acesse o **link na minha bio** e monte sua planilha agora:
🔗 https://biotoolspremium.com.br/#physiological-tools-section

━━━━━━━━━━━━━━━━━━━━━
🏃‍♀️ **Siga @alin_emanuela para acompanhar minha rotina de treinos na Orla de Porto Alegre e dicas diárias!**
📌 *Compartilhe esse post com aquele amigo que precisa começar a correr com você!*
💬 *Qual a sua maior dificuldade na corrida hoje?* 👇

#corridasaudavel #treinodecorrida #planilhadecorrida #biotools #5km #10km #amocorrer #corridaderuabrasil #focofitness #portoalegre"""
    },
    {
        "tema": "Prevenção de Lesões: O Maior Erro do Corredor",
        "caption": """🛑 O motivo pelo qual 70% dos corredores sentem dores no joelho e canelite no primeiro mês!

O corpo humano não suporta aumentos bruscos de quilometragem. A regra de ouro é nunca aumentar mais de 10% do volume semanal de uma vez!

Com a ferramenta da **BioTools**, você tem uma periodização científica de 4 semanas ajustada para você por apenas **R$ 37,90**:
✅ Volume semanal 100% controlado
✅ Dias certos de descanso e intensidade para não sobrecarregar as articulações
✅ Gráficos de evolução para acompanhar seu progresso

👟💨 Dê o próximo passo com segurança! O link para gerar sua planilha está disponível na minha **bio**!
🔗 https://biotoolspremium.com.br/#physiological-tools-section

━━━━━━━━━━━━━━━━━━━━━
🏃‍♀️ **Siga @alin_emanuela para mais dicas de saúde, ritmo e prevenção de lesões na corrida!**
📌 *Salve esse post para lembrar da regra dos 10% no seu próximo planejamento!*
💬 *Você já teve canelite ou dor no joelho correndo? Me conta nos comentários!* 👇

#prevençãodelesões #canelite #dicasdecorrida #planilhadecorrida #biotools #corridaderua #corredoresiniciantes #viciadosemcorridaderua #saudeemovimento"""
    },
    {
        "tema": "Motivação Matinal: Treino feito na Orla do Guaíba",
        "caption": """☀️ 8km entregues na Orla do Guaíba com sensação de dever cumprido! ✨

Sabe qual é a diferença entre quem desiste e quem evolui na corrida? **Ter um plano anotado.**

Quando você acorda e já sabe exatamente o treino do dia na sua planilha (quantos km, qual o ritmo e quanto tempo), você não perde tempo pensando: você só calça o tênis e vai! 👟💨

🎯 Se você quer ter disciplina e método nos seus treinos neste mês, monte sua planilha de 4 semanas na **BioTools por apenas R$ 37,90** no link da minha bio!

━━━━━━━━━━━━━━━━━━━━━
🏃‍♀️ **Siga @alin_emanuela para receber sua dose diária de motivação e rotina de treinos!**
📌 *Salve este post para se inspirar a sair da cama amanhã cedo!*
💬 *Você é do time que corre de manhã cedo ou prefere treinar à noite?* 👇🔥

🔗 https://biotoolspremium.com.br/#physiological-tools-section

#treinomatinal #orladoguaiba #portoalegre #treinopago #corredora #mulheresquecorrem #corridaderua #biotools #planilhadecorrida #motivaçãofitness"""
    }
]

def gerar_post_e_prompt(tema=None):
    """
    Gera legenda focada na venda da BioTools (R$ 37,90) + atração massiva de seguidores
    e engajamento nos comentários.
    """
    if config.GEMINI_API_KEY and "AIza" in config.GEMINI_API_KEY:
        try:
            from google import genai
            client = genai.Client(api_key=config.GEMINI_API_KEY)
            
            prompt_sistema = f"""
            Você é {config.PERSONA_NAME}, corredora de rua em Porto Alegre/RS e parceira oficial da BioTools.
            Crie um post de alto engajamento para o Instagram com a seguinte estrutura:
            
            1. TÍTULO IMPACTANTE com emojis na 1ª linha.
            2. DICA PRÁTICA E ÚTIL de corrida (Pace, zonas de treino, tiros, prevenção de canelite ou motivação).
            3. OFERTA DA BIOTOOLS: Planilha de 4 semanas por apenas R$ 37,90 no link da bio ({config.LINK_PLANILHA}).
            4. GATILHO DE SEGUIDOR: '🏃‍♀️ Siga @alin_emanuela para dicas diárias de corrida de rua e motivação!'
            5. GATILHO DE SALVAMENTO: '📌 Salve este post para consultar antes do treino!'
            6. PERGUNTA DE ENGAJAMENTO para incentivar comentários (ex: 'Qual seu pace hoje?').
            7. 8 a 10 hashtags estratégicas (#corridaderua, #pace5km, #biotools, #portoalegre, etc.).
            
            Retorne APENAS o texto formatado da legenda.
            """
            
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt_sistema
            )
            if response and response.text:
                return {"caption": response.text.strip()}
        except Exception as e:
            print(f"[Aviso Gemini]: {e}. Usando template de alta conversão de seguidores.")

    escolhido = random.choice(TEMAS_BIOTOOLS_FOLLOWER_BOOST)
    return {"caption": escolhido["caption"]}
