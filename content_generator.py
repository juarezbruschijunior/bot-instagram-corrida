import sys
import os
import json
import random

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

BOT_DIR = os.path.dirname(__file__)
HISTORICO_CINEMA_FILE = os.path.join(BOT_DIR, "historico_posts_cinema.json")

# Pacote Oficial de Posts de Cinema (Imagem Exclusiva + Curiosidade 100% Sincronizada)
PACOTE_POSTS_CINEMA = [
    {
        "id": "interestelar",
        "filme": "Interestelar (2014)",
        "imagem": "cinema_interestelar.jpg",
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
        "id": "batman_cavaleiro_trevas",
        "filme": "Batman: O Cavaleiro das Trevas (2008)",
        "imagem": "cinema_batman_cavaleiro_trevas.jpg",
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
        "id": "matrix",
        "filme": "Matrix (1999)",
        "imagem": "cinema_matrix.jpg",
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
        "id": "peaky_blinders",
        "filme": "Peaky Blinders",
        "imagem": "cinema_peaky_blinders.jpg",
        "caption": """🥃 **Quantos cigarros Thomas Shelby realmente fumou em Peaky Blinders?**

Quem assiste a *Peaky Blinders* sabe que o líder dos Blinders praticamente não passa um minuto em cena sem um cigarro aceso na boca. Mas você já parou para pensar na saúde do ator Cillian Murphy? 🚬

Como as gravações duravam meses e tinham vários ângulos por cena, Cillian Murphy revelou que fumava cerca de **1.000 cigarros por temporada**!

Para não prejudicar a saúde do ator, a equipe de figurino usava **cigarros 100% de ervas naturais e pétalas de rosa**, completamente livres de tabaco e nicotina.

━━━━━━━━━━━━━━━━━━━━━
🎬 **Siga @alin_emanuela para acompanhar dicas e curiosidades das suas séries favoritas!**
📌 *Salve este post no seu feed!*
💬 *Qual é o seu personagem favorito em Peaky Blinders?* 👇🔥

#peakyblinders #thomasshelby #cillianmurphy #seriesnetflix #curiosidadesdeseries #netflixbrasil #cinema #bbc #seriesefilmes"""
    },
    {
        "id": "senhor_dos_aneis",
        "filme": "O Senhor dos Anéis (2002)",
        "imagem": "cinema_senhor_dos_aneis.jpg",
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
        "id": "star_trek",
        "filme": "Jornada nas Estrelas (Star Trek)",
        "imagem": "cinema_star_trek_apresentadora.jpg",
        "caption": """🖖 **Você sabia que Jornada nas Estrelas mudou a história do mundo em 1968?**

Nos bastidores da série clássica de *Star Trek*, William Shatner (Capitão Kirk) e Nichelle Nichols (Tenente Uhura) gravaram o que se tornaria o primeiro beijo inter-racial da história da televisão americana! 📺✨

Com medo da censura da época, os executivos da emissora exigiram que fosse gravada uma versão alternativa *sem o beijo*. Mas sabe o que William Shatner fez? Ele errou de propósito e fez caretas em TODAS as tomadas sem beijo, forçando a emissora a exibir a versão histórica com o beijo no ar!

🤯 Martin Luther King Jr. chegou a ligar pessoalmente para Nichelle Nichols pedindo para ela nunca desistir da série, pois ela era um símbolo vivo de conquista e inspiração para milhões.

━━━━━━━━━━━━━━━━━━━━━
🎬 **Gostou da curiosidade? Siga @alin_emanuela para descobrir os maiores segredos do cinema e das séries todos os dias!**
📌 *Salve este post para compartilhar com aquele amigo que ama ficção científica!*
💬 *Qual é a sua série de ficção favorita de todos os tempos? Comenta aqui embaixo!* 👇🔥

#startrek #jornadanasestrelas #curiosidadesdefilmes #cinema #seriesclassicas #ficcaocientifica #hollywood #bastidores #nerdbrasil #filmeseseries #cinefilos"""
    }
]

def carregar_historico_cinema():
    if os.path.exists(HISTORICO_CINEMA_FILE):
        try:
            with open(HISTORICO_CINEMA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    return []

def salvar_historico_cinema(historico):
    try:
        with open(HISTORICO_CINEMA_FILE, "w", encoding="utf-8") as f:
            json.dump(historico, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"⚠️ Erro ao salvar histórico cinema: {e}")

def obter_proximo_post_cinema():
    """
    Garante que CADA publicação seja um FILME/SÉRIE DIFERENTE com IMAGEM e LEGENDA 100% SINCRONIZADAS.
    Nunca repete até que todos os filmes do pacote tenham sido postados!
    """
    historico = carregar_historico_cinema()
    
    # Filtra posts que ainda não foram publicados no ciclo atual
    posts_disponiveis = [p for p in PACOTE_POSTS_CINEMA if p["id"] not in historico]
    
    if not posts_disponiveis:
        print("🔄 Todos os filmes do pacote foram publicados! Reiniciando ciclo de rotação...")
        ultimo_id = historico[-1] if historico else None
        candidatos = [p for p in PACOTE_POSTS_CINEMA if p["id"] != ultimo_id] or PACOTE_POSTS_CINEMA
        post_escolhido = random.choice(candidatos)
        historico = [post_escolhido["id"]]
    else:
        post_escolhido = posts_disponiveis[0] # Segue fila sequencial ordenada
        historico.append(post_escolhido["id"])

    salvar_historico_cinema(historico)
    
    pos = len(historico)
    total = len(PACOTE_POSTS_CINEMA)
    print(f"🎬 [Fila Cinema Anti-Repetição] Filme: {post_escolhido['filme']} (Post {pos}/{total} do ciclo)")
    
    return post_escolhido

def gerar_post_e_prompt(tema=None):
    post = obter_proximo_post_cinema()
    return post
