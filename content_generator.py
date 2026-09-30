import json
import random
import config

TEMAS_CINEMA_CURIOSIDADES = [
    {
        "filme": "Jornada nas Estrelas (Star Trek)",
        "subtitulo": "O beijo que desafiou a censura na TV em 1968",
        "caption": """🖖 **Você sabia que Jornada nas Estrelas mudou a história do mundo em 1968?**

Nos bastidores da série clássica de *Star Trek*, William Shatner (Capitão Kirk) e Nichelle Nichols (Tenente Uhura) gravaram o que se tornaria o primeiro beijo inter-racial da história da televisão americana! 📺✨

Com medo da censura da época, os executivos da emissora exigiram que fosse gravada uma versão alternativa *sem o beijo*. Mas sabe o que William Shatner fez? Ele errou de propósito e fez caretas em TODAS as tomadas sem beijo, forçando a emissora a exibir a versão histórica com o beijo no ar!

🤯 Martin Luther King Jr. chegou a ligar pessoalmente para Nichelle Nichols pedindo para ela nunca desistir da série, pois ela era um símbolo vivo de conquista e inspiração para milhões.

━━━━━━━━━━━━━━━━━━━━━
🎬 **Gostou da curiosidade? Siga @alin_emanuela para descobrir os maiores segredos do cinema e das séries todos os dias!**
📌 *Salve este post para compartilhar com aquele amigo que ama ficção científica!*
💬 *Qual é a sua série de ficção favorita de todos os tempos? Comenta aqui embaixo!* 👇🔥

#startrek #jornadanasestrelas #curiosidadesdefilmes #cinema #seriesclassicas #ficcaocientifica #hollywood #bastidores #nerdbrasil #filmeseseries #cinefilos"""
    },
    {
        "filme": "Interestelar (2014)",
        "subtitulo": "A física real por trás da cena do buraco negro",
        "caption": """🌊 **Você sabia que o barulho de fundo dessa cena conta o tempo real na Terra?**

Na clássica cena do Planeta de Miller em *Interestelar (2014)*, um detalhe nos bastidores do áudio de Christopher Nolan e Hans Zimmer passou despercebido por 99% das pessoas:

⏳ Aquele som de **tique-taque ritmado** que toca durante toda a cena acontece a cada **1,25 segundos**. Cada um desses "tiques" representa exatamente **um dia inteiro** se passando para nós na Terra, por conta da extrema dilatação gravitacional do buraco negro Gargantua!

Quando Cooper e Brand retornam para a nave e descobrem que se passaram **23 anos na Terra**, para eles no planeta pareceram apenas **3 horas e 17 minutos**.

🤯 E tem mais: o astrofísico e vencedor do Nobel Kip Thorne calculou as equações científicas para renderizar o buraco negro, e o código do filme gerou novas descobertas na física teórica real!

━━━━━━━━━━━━━━━━━━━━━
🎬 **Siga @alin_emanuela para acompanhar curiosidades diárias sobre o mundo dos filmes e séries!**
📌 *Salve este post e compartilhe com seu amigo cinéfilo!*
💬 *Quantas vezes você já assistiu a Interestelar? Qual sua cena favorita?* 👇🚀

#interestelar #cinema #filmes #curiosidadesdefilmes #seriesefilmes #christophernolan #cinefilos #bastidores #astronomia #hollywood #filmeseseries #netflixbrasil"""
    },
    {
        "filme": "Batman: O Cavaleiro das Trevas (2008)",
        "subtitulo": "O improviso genial de Heath Ledger na prisão",
        "caption": """🃏 **O improviso lendário de Heath Ledger que não estava no roteiro do Batman!**

Na cena em que o Coringa está preso na delegacia de Gotham e o Comissário Gordon é promovido, todos os policiais começam a aplaudir. De repente, o Coringa começa a bater palmas de forma lenta, sarcástica e perturbadora. 👏

Aquilo **NÃO estava no roteiro original!** Foi uma ideia 100% espontânea de Heath Ledger na hora da gravação. O diretor Christopher Nolan achou a atuação tão genial e sinistra que manteve a cena no corte final do filme.

💣 Além disso, Ledger passou semanas trancado sozinho em um quarto de hotel em Londres para criar a voz, a risada e os tiques do personagem em um diário macabro.

━━━━━━━━━━━━━━━━━━━━━
🎬 **Siga @alin_emanuela para mais bastidores e segredos dos maiores clássicos do cinema!**
📌 *Compartilhe esse post nos seus stories!*
💬 *Na sua opinião, Heath Ledger fez o melhor Coringa da história do cinema?* 👇🦇

#batman #ocavaleirodastrevas #heathledger #coringa #joker #christophernolan #dccomics #cinema #curiosidadesdefilmes #bastidores #filmeseseries"""
    },
    {
        "filme": "Matrix (1999)",
        "subtitulo": "A verdade secreta sobre o código verde que cai na tela",
        "caption": """🟢 **Você sabe o que realmente está escrito no famoso código verde de Matrix?**

Aquela clássica cascata de símbolos verdes que abre a trilogia *Matrix* parece uma sequência indecifrável de criptografia hacker ultra-avançada... Mas a verdade vai te surpreender! 💻

O designer de produção Simon Whiteley revelou anos depois que escaneou os símbolos direto dos **livros de receitas de sushi em japonês** da sua esposa! 🍣🥢

Portanto, quando Neo e Morpheus estão olhando para a tela cheia de códigos misteriosos, na verdade estão lendo receitas detalhadas de sushi, ramen e rolinhos primavera!

━━━━━━━━━━━━━━━━━━━━━
🎬 **Siga @alin_emanuela para receber sua dose diária de curiosidades do cinema e da cultura pop!**
📌 *Salve este post para lembrar desse fato hilário da próxima vez que rever Matrix!*
💬 *Você tomaria a pílula azul ou a pílula vermelha? Deixe nos comentários!* 👇💊

#matrix #keanureeves #filmes #curiosidadesdefilmes #cinema #ficcaocientifica #cyberpunk #bastidores #nerd #geekbrasil #culturapop"""
    },
    {
        "filme": "O Senhor dos Anéis (2002)",
        "subtitulo": "O grito real de dor de Viggo Mortensen que ficou no filme",
        "caption": """🗡️ **O grito real de agonia de Aragorn em O Senhor dos Anéis: As Duas Torres!**

Em uma cena emocionante onde Aragorn acredita que Merry e Pippin foram mortos pelos Orcs, ele chuta com toda a força um capacete de ferro pesado e solta um grito desesperador caindo de joelhos. 💥

Aquele grito **não foi atuação:** Viggo Mortensen realmente **quebrou dois dedos do pé** ao chutar o capacete de metal! Em vez de pedir para parar a gravação, ele usou a dor excruciante real na cena.

O diretor Peter Jackson ficou tão impressionado com o profissionalismo de Viggo que aquela tomada exata foi a que foi para as telas dos cinemas do mundo todo!

━━━━━━━━━━━━━━━━━━━━━
🎬 **Siga @alin_emanuela para não perder as melhores histórias dos bastidores do cinema!**
📌 *Salve o post e envie para um fã da Terra Média!*
💬 *Qual é o seu filme favorito da trilogia O Senhor dos Anéis?* 👇🧝‍♂️

#osenhordosaneis #lordoftherings #aragorn #viggomortensen #peterjackson #cinema #curiosidadesdefilmes #fantasia #hollywood #filmeseseries"""
    },
    {
        "filme": "Peaky Blinders",
        "subtitulo": "O segredo por trás dos cigarros de Thomas Shelby",
        "caption": """🥃 **Quantos cigarros Thomas Shelby realmente fumou em Peaky Blinders?**

Quem assiste a *Peaky Blinders* sabe que o líder dos Blinders praticamente não passa um minuto em cena sem um cigarro aceso na boca. Mas você já parou para pensar na saúde do ator Cillian Murphy? 🚬

Como as gravações duravam meses e tinham vários ângulos por cena, Cillian Murphy revelou que fumava cerca de **1.000 cigarros por temporada**!

Para não prejudicar a saúde do ator, a equipe de figurino usava **cigarros 100% de ervas naturais e pétalas de rosa**, completamente livres de tabaco e nicotina.

━━━━━━━━━━━━━━━━━━━━━
🎬 **Siga @alin_emanuela para acompanhar dicas e curiosidades das suas séries favoritas!**
📌 *Salve este post no seu feed!*
💬 *Qual é o seu personagem favorito em Peaky Blinders?* 👇🔥

#peakyblinders #thomasshelby #cillianmurphy #seriesnetflix #curiosidadesdeseries #netflixbrasil #cinema #bbc #seriesefilmes"""
    }
]

def gerar_post_e_prompt(tema=None):
    """
    Gera curiosidades de alto impacto sobre Filmes e Séries clássicas e modernas,
    otimizadas para compartilhamento, retenção e atração de novos seguidores.
    """
    if config.GEMINI_API_KEY and "AIza" in config.GEMINI_API_KEY:
        try:
            from google import genai
            client = genai.Client(api_key=config.GEMINI_API_KEY)
            
            prompt_sistema = """
            Você é especialista em Cinema, Séries e Cultura Pop e redige conteúdos virais para o Instagram.
            Crie um post de alto impacto e curiosidade fascinante sobre um grande filme ou série famosa (ex: Harry Potter, Oppenheimer, Breaking Bad, Stranger Things, Gladiador, Titanic, Vingadores, etc.).
            
            Estrutura obrigatória:
            1. TÍTULO IMPACTANTE com emojis e pergunta misteriosa na 1ª linha.
            2. HISTÓRIA DE BASTIDORES ou FATO CIENTÍFICO/SECRETO contado de forma envolvente em 3 a 4 parágrafos curtos.
            3. GATILHO DE SEGUIDOR: '🎬 Siga @alin_emanuela para descobrir os maiores segredos e bastidores do cinema todos os dias!'
            4. GATILHO DE SALVAMENTO: '📌 Salve este post para compartilhar com os amigos!'
            5. PERGUNTA DE ENGAJAMENTO para estimular debates nos comentários.
            6. 8 a 12 hashtags estratégicas de cinema e séries (#cinema #curiosidadesdefilmes #filmeseseries #bastidores, etc.).
            
            Retorne APENAS o texto pronto da legenda.
            """
            
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt_sistema
            )
            if response and response.text:
                return {"caption": response.text.strip()}
        except Exception as e:
            print(f"[Aviso Gemini]: {e}. Usando template de curiosidades de cinema.")

    escolhido = random.choice(TEMAS_CINEMA_CURIOSIDADES)
    return {"caption": escolhido["caption"], "filme": escolhido.get("filme"), "subtitulo": escolhido.get("subtitulo")}
