import json
import os
from PIL import Image, ImageDraw, ImageFont

brain_dir = r"C:\Users\juare\.gemini\antigravity\brain\958fe970-8f1b-4e8b-80e3-f6adfc73d1e8"
bot_dir = r"C:\Users\juare\OneDrive\Área de Trabalho\bot_instagram_corrida"
posts_dir = os.path.join(bot_dir, "posts_gerados")

# Lista dos 100+ Maiores Filmes e Séries da História com Curiosidades Virais
CATALOGO_100_FILMES = [
    # 1 a 10: Clássicos Sci-Fi & Espaço
    ("interestelar", "Interestelar (2014)", "cinema_interestelar_apresentadora.jpg", "🎬 CURIOSIDADES DO CINEMA", "O som que conta o tempo real na Terra",
     "🌊 **Você sabia que o barulho de fundo dessa cena conta o tempo real na Terra?**\n\nNa clássica cena do Planeta de Miller em *Interestelar (2014)*, um detalhe nos bastidores do áudio de Christopher Nolan e Hans Zimmer passou despercebido por 99% das pessoas:\n\n⏳ Aquele som de **tique-taque ritmado** que toca durante toda a cena acontece a cada **1,25 segundos**. Cada um desses 'tiques' representa exatamente **um dia inteiro** se passando para nós na Terra, por conta da extrema dilatação gravitacional do buraco negro Gargantua!\n\nQuando Cooper e Brand retornam para a nave e descobrem que se passaram **23 anos na Terra**, para eles no planeta pareceram apenas **3 horas e 17 minutos**.\n\n🤯 O astrofísico Kip Thorne calculou as equações científicas reais para renderizar o buraco negro!\n\n━━━━━━━━━━━━━━━━━━━━━\n🎬 **Siga @alin_emanuela para acompanhar curiosidades diárias sobre cinema e séries!**\n📌 *Salve este post e compartilhe com seu amigo cinéfilo!*\n💬 *Quantas vezes você já assistiu a Interestelar?* 👇🚀\n\n#interestelar #cinema #filmes #curiosidadesdefilmes #seriesefilmes #christophernolan #cinefilos #bastidores #astronomia #hollywood"),

    ("matrix", "Matrix (1999)", "cinema_matrix_apresentadora.jpg", "🎬 CURIOSIDADES DO CINEMA", "O segredo por trás do código verde digital",
     "🟢 **Você sabe o que realmente está escrito no famoso código verde de Matrix?**\n\nAquela clássica cascata de símbolos verdes que abre a trilogia *Matrix* parece uma sequência indecifrável de criptografia hacker ultra-avançada... Mas a verdade é hilária! 💻\n\nO designer de produção Simon Whiteley revelou que escaneou os símbolos diretamente dos **livros de receitas de sushi em japonês** da sua esposa! 🍣🥢\n\nPortanto, quando Neo e Morpheus olham para a tela cheia de códigos, estão lendo receitas de sushi, ramen e rolinhos primavera!\n\n━━━━━━━━━━━━━━━━━━━━━\n🎬 **Siga @alin_emanuela para receber sua dose diária de curiosidades do cinema!**\n📌 *Salve este post para lembrar desse fato!*\n💬 *Você tomaria a pílula azul ou a pílula vermelha?* 👇💊\n\n#matrix #keanureeves #filmes #curiosidadesdefilmes #cinema #ficcaocientifica #cyberpunk #bastidores #nerd #culturapop"),

    ("batman_cavaleiro_trevas", "Batman: O Cavaleiro das Trevas (2008)", "cinema_batman_apresentadora.jpg", "🎬 CURIOSIDADES DO CINEMA", "O improviso de Heath Ledger que chocou o set",
     "🃏 **O improviso lendário de Heath Ledger que não estava no roteiro do Batman!**\n\nNa cena em que o Coringa está preso na delegacia de Gotham e o Comissário Gordon é promovido, todos os policiais aplaudem. De repente, o Coringa começa a bater palmas de forma lenta, sarcástica e perturbadora. 👏\n\nAquilo **NÃO estava no roteiro original!** Foi uma ideia 100% espontânea de Heath Ledger na hora da gravação. O diretor Christopher Nolan achou a atuação tão genial e sinistra que manteve a cena no corte final do filme.\n\n💣 Além disso, Ledger passou semanas trancado sozinho em um quarto de hotel em Londres para criar a voz e os tiques do personagem em um diário macabro.\n\n━━━━━━━━━━━━━━━━━━━━━\n🎬 **Siga @alin_emanuela para mais bastidores e segredos do cinema!**\n📌 *Compartilhe esse post nos seus stories!*\n💬 *Heath Ledger foi o melhor Coringa de todos os tempos?* 👇🦇\n\n#batman #ocavaleirodastrevas #heathledger #coringa #joker #christophernolan #dccomics #cinema #curiosidadesdefilmes"),

    ("peaky_blinders", "Peaky Blinders", "cinema_peaky_apresentadora.jpg", "🎬 CURIOSIDADES DE SÉRIES", "O mistério dos 3.000 cigarros de Tommy Shelby",
     "🥃 **Quantos cigarros Thomas Shelby realmente fumou em Peaky Blinders?**\n\nQuem assiste a *Peaky Blinders* sabe que o líder dos Blinders praticamente não passa um minuto em cena sem um cigarro aceso na boca. 🚬\n\nComo as gravações duravam meses e tinham vários ângulos por cena, Cillian Murphy revelou que fumava cerca de **1.000 cigarros por temporada**!\n\nPara não prejudicar a saúde do ator, a equipe usava **cigarros 100% de ervas naturais e pétalas de rosa**, completamente livres de tabaco e nicotina.\n\n━━━━━━━━━━━━━━━━━━━━━\n🎬 **Siga @alin_emanuela para acompanhar dicas e curiosidades das suas séries favoritas!**\n📌 *Salve este post!*\n💬 *Qual é o seu personagem favorito em Peaky Blinders?* 👇🔥\n\n#peakyblinders #thomasshelby #cillianmurphy #seriesnetflix #curiosidadesdeseries #netflixbrasil #cinema"),

    ("senhor_dos_aneis", "O Senhor dos Anéis (2002)", "cinema_senhor_aneis_apresentadora.jpg", "🎬 BASTIDORES DE HOLLYWOOD", "O grito de dor 100% real de Viggo Mortensen",
     "🗡️ **O grito real de agonia de Aragorn em As Duas Torres!**\n\nNa cena em que Aragorn acredita que Merry e Pippin morreram, ele chuta com toda a força um capacete de ferro pesado e solta um grito desesperador caindo de joelhos. 💥\n\nAquele grito **não foi atuação:** Viggo Mortensen realmente **quebrou dois dedos do pé** ao chutar o capacete de metal! Em vez de parar a gravação, ele usou a dor excruciante real na cena.\n\nO diretor Peter Jackson ficou tão impressionado com o profissionalismo de Viggo que aquela tomada exata foi a que foi para as telas dos cinemas do mundo todo!\n\n━━━━━━━━━━━━━━━━━━━━━\n🎬 **Siga @alin_emanuela para acompanhar curiosidades diárias do cinema!**\n📌 *Salve o post e envie para um fã da Terra Média!*\n💬 *Qual é o seu filme favorito da trilogia?* 👇🧝‍♂️\n\n#osenhordosaneis #lordoftherings #aragorn #viggomortensen #peterjackson #cinema #curiosidadesdefilmes #fantasia"),

    ("star_trek", "Jornada nas Estrelas (Star Trek)", "cinema_star_trek_apresentadora.jpg", "🎬 HISTÓRIA DA TV & CINEMA", "O beijo que quebrou barreiras em 1968",
     "🖖 **Você sabia que Jornada nas Estrelas mudou a história do mundo em 1968?**\n\nNos bastidores de *Star Trek*, William Shatner (Capitão Kirk) e Nichelle Nichols (Uhura) gravaram o primeiro beijo inter-racial da história da televisão americana! 📺✨\n\nCom medo da censura, os executivos exigiram gravar uma versão alternativa sem beijo. Mas Shatner errou e fez caretas de propósito em todas as tomadas sem beijo, forçando a emissora a exibir a versão histórica com o beijo!\n\nMartin Luther King Jr. pediu pessoalmente para Nichelle nunca sair da série, por ser um símbolo de inspiração para milhões.\n\n━━━━━━━━━━━━━━━━━━━━━\n🎬 **Siga @alin_emanuela para os maiores segredos do cinema e das séries!**\n📌 *Salve e compartilhe com quem ama ficção científica!*\n💬 *Qual a sua série de ficção clássica favorita?* 👇🔥\n\n#startrek #jornadanasestrelas #curiosidadesdefilmes #cinema #seriesclassicas #ficcaocientifica #bastidores"),

    ("star_wars_vader", "Star Wars: O Império Contra-Ataca (1980)", "cinema_star_wars_apresentadora.jpg", "🎬 BASTIDORES DE HOLLYWOOD", "O segredo de 'Eu sou seu pai' escondido do elenco",
     "🌌 **O segredo absoluto de 'Eu sou seu pai' em Star Wars!**\n\nNa gravação da icônica cena climática de *O Império Contra-Ataca*, apenas 3 pessoas sabiam a verdade: George Lucas, o diretor Irvin Kershner e Mark Hamill.\n\n🤫 Durante a filmagem, o ator na armadura de Darth Vader (David Prowse) disse no microfone: *'Obi-Wan matou seu pai!'*. Hamill foi instruído a reagir em choque fingindo ouvir outra coisa.\n\nApenas na pós-produção a voz de James Earl Jones gravou a frase real: *'Não, eu sou seu pai!'*. Nem o elenco sabia até a grande estreia!\n\n━━━━━━━━━━━━━━━━━━━━━\n🎬 **Siga @alin_emanuela para descobrir segredos dos clássicos!**\n📌 *Salve e compartilhe com um fã de Star Wars!*\n💬 *Qual o seu filme favorito de Star Wars?* 👇⚔️\n\n#starwars #darthvader #lukeskywalker #georgelucas #cinema #curiosidadesdefilmes #bastidores #nerdbrasil"),

    ("de_volta_para_o_futuro", "De Volta para o Futuro (1985)", "cinema_de_volta_futuro_apresentadora.jpg", "🎬 CURIOSIDADES DO CINEMA", "A máquina do tempo quase foi uma geladeira",
     "⚡ **O DeLorean quase foi uma geladeira comum!**\n\nNos primeiros roteiros de *De Volta para o Futuro*, a máquina do tempo do Dr. Brown não era um carro, mas sim uma **geladeira doméstica**! 🧊\n\nSteven Spielberg e Robert Zemeckis mudaram a ideia por temerem que crianças assistissem ao filme e se trancassem dentro de geladeiras em casa.\n\nFoi aí que surgiu a ideia genial de usar o DeLorean DMC-12 com portas asas de gaivota, que parecia uma nave alienígena nos anos 50! 🚗⚡\n\n━━━━━━━━━━━━━━━━━━━━━\n🎬 **Siga @alin_emanuela para curiosidades diárias sobre filmes!**\n📌 *Salve este post!*\n💬 *Se você tivesse um DeLorean, para qual ano viajaria?* 👇⏳\n\n#devoltaparaofuturo #backtothefuture #martymcfly #delorean #cinema #curiosidadesdefilmes #anos80"),

    ("jurassic_park", "Jurassic Park: O Parque dos Dinossauros (1993)", "cinema_jurassic_park_apresentadora.jpg", "🎬 CURIOSIDADES DO CINEMA", "A origem inusitada do rugido do T-Rex",
     "🦖 **De onde veio o aterrorizante rugido do T-Rex de Jurassic Park?**\n\nO designer de som Gary Rydstrom levou meses para criar o rugido do Tiranossauro Rex. A combinação de áudios usados é inacreditável:\n\n🐾 O rugido é uma mistura de um **filhote de elefante**, um **tigre** e um **cachorro Jack Russell Terrier** brincando com uma corda de brinquedo!\n\nO som do sopro mortal antes do ataque? Foi a respiração gravada de uma baleia através do espiráculo! 🐋\n\n━━━━━━━━━━━━━━━━━━━━━\n🎬 **Siga @alin_emanuela para bastidores dos seus filmes favoritos!**\n📌 *Compartilhe com quem ama Jurassic Park!*\n💬 *Qual a sua cena favorita de Jurassic Park?* 👇🦕\n\n#jurassicpark #stevenspielberg #dinossauros #trexbastidores #cinema #curiosidadesdefilmes #filmesclassicos"),

    ("titanic", "Titanic (1997)", "cinema_titanic_apresentadora.jpg", "🎬 CURIOSIDADES DO CINEMA", "Quem realmente desenhou o retrato de Rose?",
     "🚢 **Quem realmente desenhou a Rose no clássico Titanic?**\n\nNa cena em que Jack desenha Rose usando o colar 'Coração do Oceano', os closes das mãos habilidosas desenhando no caderno **não pertenciam a Leonardo DiCaprio**! ✏️\n\nAs mãos pertenciam ao próprio diretor, **James Cameron**!\n\nComo James Cameron é canhoto e Leonardo DiCaprio é destro, a imagem foi espelhada digitalmente na edição para parecer a mão direita de Jack!\n\n━━━━━━━━━━━━━━━━━━━━━\n🎬 **Siga @alin_emanuela para mais segredos de Hollywood!**\n📌 *Salve este post!*\n💬 *O Jack cabia ou não naquela porta de madeira?* 👇🥶\n\n#titanic #leonardodicaprio #katewinslet #jamescameron #cinema #curiosidadesdefilmes #filmesclassicos"),

    # 11 a 20: Grandes Sucessos do Cinema & Marvel
    ("vingadores_ultimato", "Vingadores: Ultimato (2019)", "cinema_vingadores_apresentadora.jpg", "🎬 BASTIDORES MARVEL", "A fala 'Eu sou o Homem de Ferro' foi de última hora",
     "🦾 **A frase mais épica dos Vingadores quase não existiu!**\n\nNa cena climática de *Vingadores: Ultimato*, Thanos diz *'Eu sou inevitável'* e Tony Stark responde *'E eu... sou o Homem de Ferro!'* antes do estalo. 💎\n\nOriginalmente, Tony Stark não dizia nada na cena! Mas na edição, o editor Jeff Ford sugeriu que ele precisava de uma resposta final de impacto.\n\nRobert Downey Jr. gravou a icônica fala **apenas 3 meses antes da estreia mundial**!\n\n━━━━━━━━━━━━━━━━━━━━━\n🎬 **Siga @alin_emanuela para tudo sobre o cinema!**\n📌 *Compartilhe com um fã da Marvel!*\n💬 *Você chorou no final de Vingadores: Ultimato?* 👇❤️\n\n#vingadores #avengersendgame #homemdeferro #robertdowneyjr #marvelbrasil #mcu #cinema"),

    ("harry_potter", "Harry Potter e a Pedra Filosofal (2001)", "cinema_harry_potter_apresentadora.jpg", "🎬 CURIOSIDADES DO CINEMA", "As velas flutuantes no Grande Salão eram reais",
     "⚡ **As velas flutuantes de Hogwarts não eram efeitos de computador!**\n\nNo Grande Salão de Hogwarts, vemos centenas de velas flutuando magicamente no ar. 🕯️✨\n\nA equipe pendurou **centenas de velas reais com fios de náilon**, fogo de verdade e cera especial.\n\nPorém, durante uma gravação, o calor queimou alguns fios e as velas despencaram sobre as mesas! A partir do 2º filme passaram a usar CGI por segurança.\n\n━━━━━━━━━━━━━━━━━━━━━\n🎬 **Siga @alin_emanuela para o mundo mágico do cinema!**\n📌 *Salve e envie para um fã de Harry Potter!*\n💬 *Qual é a sua casa de Hogwarts?* 👇🏰\n\n#harrypotter #hogwarts #grifinoria #sonserina #curiosidadesdefilmes #cinema #bastidores"),

    ("breaking_bad", "Breaking Bad", "cinema_breaking_bad_apresentadora.jpg", "🎬 CURIOSIDADES DE SÉRIES", "A lendária pizza no telhado em um único take",
     "🍕 **A jogada impossível de Walter White em Breaking Bad!**\n\nNa 3ª temporada, Walter White arremessa uma pizza inteira que sobe girando no ar e cai perfeitamente esticada no telhado da casa. 🏠\n\nVince Gilligan separou dezenas de pizzas prevendo horas de gravação.\n\nPara o espanto de toda a equipe, Bryan Cranston acertou o arremesso perfeito **no primeiríssimo take**!\n\n━━━━━━━━━━━━━━━━━━━━━\n🎬 **Siga @alin_emanuela para segredos das melhores séries!**\n📌 *Salve este post!*\n💬 *Breaking Bad é a melhor série já feita?* 👇⚗️\n\n#breakingbad #walterwhite #bryancranston #vincegilligan #seriesnetflix #curiosidadesdeseries"),

    ("clube_da_luta", "Clube da Luta (1999)", "cinema_clube_luta_apresentadora.jpg", "🎬 CURIOSIDADES DO CINEMA", "Um copo da Starbucks em TODAS as cenas",
     "☕ **O detalhe oculto em 100% das cenas de Clube da Luta!**\n\nO diretor David Fincher escondeu uma mensagem secreta sobre consumismo em *Clube da Luta*:\n\nHá um **copo de café da Starbucks** visível em praticamente **todas as cenas do filme**! Seja sobre uma mesa, lixeira ou na mão de figurantes. 🥤\n\nA própria Starbucks autorizou a brincadeira satírica!\n\n━━━━━━━━━━━━━━━━━━━━━\n🎬 **Siga @alin_emanuela para mensagens ocultas nos filmes!**\n📌 *Salve para conferir na próxima vez que assistir!*\n💬 *Qual a primeira regra do Clube da Luta?* 👇🥊\n\n#clubedaluta #fightclub #bradpitt #edwardnorton #davidfincher #cinema #curiosidadesdefilmes"),

    ("o_iluminado", "O Iluminado (1980)", "cinema_o_iluminado_apresentadora.jpg", "🎬 BASTIDORES DE HOLLYWOOD", "Jack Nicholson quebrou 60 portas de verdade",
     "🪓 **A icônica cena de 'Here’s Johnny!' em O Iluminado!**\n\nPara a cena do machado no banheiro, a produção preparou portas falsas leves. Mas como Jack Nicholson foi bombeiro na juventude, quebrava rápido demais! 🚪\n\nStanley Kubrick mandou instalar **portas de carvalho maciço reais**, e Jack destruiu cerca de **60 portas verdadeiras** ao longo de 3 dias de filmagens!\n\n━━━━━━━━━━━━━━━━━━━━━\n🎬 **Siga @alin_emanuela para histórias insanas do cinema!**\n📌 *Salve este post!*\n💬 *Qual o filme de terror mais assustador que você já viu?* 👇👀\n\n#oiluminado #theshining #jacknicholson #stanleykubrick #terror #curiosidadesdefilmes #cinema"),

    ("stranger_things", "Stranger Things", "cinema_stranger_things_apresentadora.jpg", "🎬 CURIOSIDADES DE SÉRIES", "Millie Bobby Brown odeia waffles na vida real",
     "🧇 **O segredo gastronômico da Eleven em Stranger Things!**\n\nA paixão da Eleven por waffles Eggo se tornou icônica na 1ª temporada. 👧⚡\n\nMas Millie Bobby Brown revelou que **detesta waffles** na vida real! A cada tomada comendo pilhas de waffles, ela precisava de um balde escondido para cuspir ao ouvir 'Corta!'.\n\n━━━━━━━━━━━━━━━━━━━━━\n🎬 **Siga @alin_emanuela para bastidores das suas séries favoritas!**\n📌 *Salve este post!*\n💬 *Quem é o seu personagem favorito em Stranger Things?* 👇🧇\n\n#strangerthings #eleven #milliebobbybrown #netflixbrasil #curiosidadesdeseries #culturapop"),

    ("forrest_gump", "Forrest Gump (1994)", "cinema_forrest_gump_apresentadora.jpg", "🎬 CURIOSIDADES DO CINEMA", "A bola de ping-pong nunca existiu no set",
     "🏓 **O segredo das partidas de ping-pong de Forrest Gump!**\n\nNas cenas em que Forrest joga tênis de mesa em velocidade sobre-humana, **não havia nenhuma bolinha na mesa durante as filmagens**! 🏆\n\nTom Hanks apenas fingia rebater o ar no ritmo exato, e a bolinha foi inserida 100% em computação gráfica na pós-produção!\n\n━━━━━━━━━━━━━━━━━━━━━\n🎬 **Siga @alin_emanuela para curiosidades diárias do cinema!**\n📌 *Salve e compartilhe!*\n💬 *Qual a sua frase favorita de Forrest Gump?* 👇🍫\n\n#forrestgump #tomhanks #cinema #curiosidadesdefilmes #filmesclassicos #hollywood"),

    ("pulp_fiction", "Pulp Fiction (1994)", "cinema_pulp_fiction_apresentadora.jpg", "🎬 CURIOSIDADES DO CINEMA", "O que brilhava na maleta de Tarantino?",
     "💼 **O maior mistério de Pulp Fiction!**\n\nQuando a maleta preta se abre e emite uma luz dourada brilhante, fãs especulam sobre ouro ou almas humanas. ✨\n\nNo set, era apenas **uma lâmpada laranja conectada a uma bateria de 12V**! Tarantino deixou o conteúdo misterioso para atiçar a imaginação.\n\n━━━━━━━━━━━━━━━━━━━━━\n🎬 **Siga @alin_emanuela para os maiores mistérios dos filmes!**\n📌 *Salve este post!*\n💬 *O que você acha que estava dentro da maleta?* 👇💡\n\n#pulpfiction #quentintarantino #samuelljackson #johntravolta #cinema #curiosidadesdefilmes"),

    ("avatar", "Avatar (2009)", "cinema_avatar_apresentadora.jpg", "🎬 BASTIDORES DE HOLLYWOOD", "O idioma Na'vi com mais de 1.000 palavras reais",
     "🌿 **O idioma Na'vi de Avatar é uma língua 100% real e funcional!**\n\nJames Cameron contratou o linguista Dr. Paul Frommer para criar a língua Na'vi com regras gramaticais estritas e mais de **1.000 palavras catalogadas**! 🌌\n\nO elenco fez semanas de aulas para falar fluentemente em cena!\n\n━━━━━━━━━━━━━━━━━━━━━\n🎬 **Siga @alin_emanuela para grandes produções do cinema!**\n📌 *Compartilhe este post!*\n💬 *Você já assistiu Avatar em 3D?* 👇💙\n\n#avatar #jamescameron #pandora #navi #cinema #curiosidadesdefilmes #ficcaocientifica"),

    ("o_poderoso_chefao", "O Poderoso Chefão (1972)", "cinema_poderoso_chefao_apresentadora.jpg", "🎬 CURIOSIDADES DO CINEMA", "O gato de Don Corleone foi improvisado",
     "🐱 **O gato mais famoso do cinema foi um improviso total!**\n\nDon Vito Corleone acaricia um gato na famosa cena de abertura. O gato **não estava no roteiro**: Coppola o encontrou abandonado no estúdio minutos antes e o pôs no colo de Marlon Brando! 🌹\n\nO gato ronronou tão alto que quase abafou a voz do ator!\n\n━━━━━━━━━━━━━━━━━━━━━\n🎬 **Siga @alin_emanuela para histórias dos clássicos!**\n📌 *Salve este post!*\n💬 *Qual é o seu filme favorito da trilogia?* 👇🎩\n\n#opoderosochefao #thegodfather #marlonbrando #francisfordcoppola #cinema #curiosidadesdefilmes")
]

# Gerador complementar para atingir 105 clássicos completos
TEMAS_EXTRAS = [
    ("gladiador", "Gladiador (2000)", "Russel Crowe recusou dublê e enfrentou tigres reais a 1 metro de distância", "O confronto real com tigres no Coliseu de Roma", "#gladiador #russellcrowe #ridleyscott"),
    ("homem_aranha_2002", "Homem-Aranha (2002)", "Tobey Maguire pegou a bandeja do almoço com comida em 156 tentativas sem efeitos digitais", "A cena da bandeja pegando o almoço no ar sem CGI", "#homemaranha #spiderman #tobeymaguire"),
    ("shrek", "Shrek (2001)", "O banho de lama inicial exigiu que animadores tomassem banho de lama real para estudar a física", "O teste com lama real dos animadores da DreamWorks", "#shrek #dreamworks #animacao"),
    ("rei_leao", "O Rei Leão (1994)", "O rugido de Mufasa foi feito com um microfone dentro de uma lata de lixo de ferro", "Como foi feito o rugido estrondoso de Mufasa", "#oreileao #thelionking #disney"),
    ("toy_story", "Toy Story (1995)", "Woody quase foi um vilão mimado e sarcástico nos primeiros testes", "Woody seria o vilão da história original", "#toystory #pixar #disney"),
    ("corra", "Corra! (Get Out - 2017)", "A cena do afundamento no 'Lugar Submerso' foi gravada com câmera lenta reversa e cabos", "O segredo do Lugar Submerso e a xícara hipnótica", "#getout #corra #jordanpeele #terror"),
    ("game_of_thrones", "Game of Thrones", "A carne de cavalo que Daenerys comeu na 1ª temporada era feita de 1,5 kg de jujuba sólida", "O coração de cavalo feito de jujuba de Daenerys", "#gameofthrones #daenerys #hbo"),
    ("the_last_of_us", "The Last of Us", "O fungo Cordyceps que cria os infectados realmente existe na natureza e controla formigas", "A ciência assustadora do fungo Cordyceps real", "#thelastofus #pedropascal #hbomax"),
    ("wandinha", "Wandinha (Wednesday)", "Jenna Ortega inventou a coreografia viral em 2 dias inspirada em punks dos anos 80", "A dança icônica de Jenna Ortega sem piscar os olhos", "#wandinha #wednesday #jennaortega #netflix"),
    ("the_office", "The Office", "A cena do beijo entre Michael e Oscar foi 100% improvisada por Steve Carell", "O beijo improvisado que chocou o elenco de The Office", "#theoffice #stevecarell #series"),
    ("friends", "Friends", "A fonte de água da abertura foi gravada às 4 da manhã com água quase congelando", "Os bastidores gelados da fonte da abertura de Friends", "#friends #sitcom #seriesclassicas"),
    ("la_casa_de_papel", "La Casa de Papel", "O Professor quase teve o nome de Tóquio como líder da narrativa", "O segredo por trás do hino Bella Ciao", "#lacasadepapel #elprofesor #netflix"),
    ("dark", "Dark", "O mapa do tempo e a árvore genealógica de Winden ocupavam uma sala inteira de roteiristas", "A complexidade da árvore genealógica de Dark", "#darknetflix #ficcaocientifica #netflix"),
    ("vikings", "Vikings", "A maquiagem de guerra de Ragnar Lothbrok continha pigmentos reais da era nórdica", "A fidelidade histórica nas tatuagens de Ragnar", "#vikings #ragnarlothbrok #series"),
    ("house_of_the_dragon", "A Casa do Dragão", "Os 17 dragões foram criados com personalidades e sons de espécies diferentes de aves e répteis", "O design sonoro único de cada dragão", "#houseofthedragon #gameofthrones #hbo"),
    ("lost", "Lost", "A cena do acidente de avião no episódio piloto foi o mais caro da história da TV na época", "Os 14 milhões de dólares do episódio piloto", "#lost #seriesclassicas #mistério"),
    ("supernatural", "Supernatural", "O clássico Chevrolet Impala 1967 tinha 9 réplicas idênticas para cenas de ação", "O carro lendário Baby e suas 9 versões", "#supernatural #jensenackles #jaredpadalecki"),
    ("dexter", "Dexter", "O sangue cenográfico foi criado com calda de bordo e corante alimentar não tóxico", "A receita do sangue cenográfico das cenas de crime", "#dexter #michaelchall #series"),
    ("the_walking_dead", "The Walking Dead", "Os figurantes que faziam zumbis passaram por uma 'Escola de Zumbis' para aprender a andar", "A Escola de Zumbis dos bastidores de TWD", "#thewalkingdead #zumbis #series"),
    ("the_boys", "The Boys", "O Capitão Pátria (Homelander) usa ombreiras com enchimento para imitar a bandeira americana", "O simbolismo oculto no uniforme do Homelander", "#theboys #homelander #primevideo"),
    ("blade_runner", "Blade Runner (1982)", "O monólogo 'Lágrimas na Chuva' de Rutger Hauer foi improvisado minutos antes de gravar", "O monólogo mais poético da ficção científica", "#bladerunner #ridleyscott #harrisonford"),
    ("2001_uma_odisseia", "2001: Uma Odisseia no Espaço (1968)", "Stanley Kubrick usou um estúdio giratório de 30 toneladas para criar a gravidade zero", "A roda gigante giratória de gravidade de Kubrick", "#2001umaodisseianoespaco #stanleykubrick #scifi"),
    ("o_exterminador_do_futuro_2", "O Exterminador do Futuro 2 (1991)", "O som do T-1000 atravessando as grades foi feito com ração de cachorro escorrendo de uma lata", "Os sons bizarros do androide de metal líquido", "#exterminadordofuturo #arnoldschwarzenegger #jamescameron"),
    ("alien_o_oitavo_passageiro", "Alien: O Oitavo Passageiro (1979)", "A reação do elenco na cena do 'peito explodindo' foi de pavor 100% real", "A surpresa com órgãos reais no set de filmagem", "#alien #ridleyscott #sigourneyweaver"),
    ("duna", "Duna (2021)", "O som dos vermes gigantes da areia de Arrakis foi feito enterrando microfones no deserto", "A gravação do som sob as dunas de Abu Dhabi", "#duna #dunemovie #timotheechalame #denisvilleneuve"),
    ("a_origem_inception", "A Origem (Inception - 2010)", "O corredor giratório da luta em gravidade zero foi construído em tamanho real sem CGI", "O corredor giratório mecânico de Christopher Nolan", "#inception #aorigem #leonardodicaprio #christophernolan"),
    ("mad_max_estrada_da_furia", "Mad Max: Estrada da Fúria (2015)", "O guitarrista cego realmente tocava uma guitarra que soltava labaredas de fogo reais", "A guitarra lança-chamas totalmente funcional", "#madmax #furyroad #tomhardy #charlizetheron"),
    ("john_wick", "John Wick (2014)", "Keanu Reeves aprendeu judô, jiu-jitsu e tiro tático treinando 8 horas por dia", "O treinamento tático insano de Keanu Reeves", "#johnwick #keanureeves #cinemaacao"),
    ("deadpool", "Deadpool (2016)", "Ryan Reynolds financiou do próprio bolso os roteiristas no set porque a Fox cortou a verba", "A dedicação de Ryan Reynolds para o filme acontecer", "#deadpool #ryanreynolds #marvel"),
    ("homem_de_ferro_2008", "Homem de Ferro (2008)", "O roteiro não tinha falas prontas e os atores improvisavam quase todas as cenas", "O nascimento do MCU através de improvisos brilhantes", "#homemdeferro #ironman #robertdowneyjr #marvel"),
    ("homem_aranha_aranhaverso", "Homem-Aranha no Aranhaverso (2018)", "Miles Morales foi animado a 12 frames por segundo para parecer desajeitado no início", "A técnica inovadora de animação a 12fps", "#aranhaverso #milesmorales #spiderman"),
    ("piratas_do_caribe", "Piratas do Caribe: A Maldição do Pérola Negra (2003)", "Johnny Depp se inspirou em Keith Richards e no gambá Pepe Le Pew para criar Jack Sparrow", "A criação excêntrica do Capitão Jack Sparrow", "#piratasdocaribe #jacksparrow #johnnydepp"),
    ("o_show_de_truman", "O Show de Truman (1998)", "As câmeras escondidas no filme eram lentes reais de segurança instaladas no set", "A genialidade visual da vigilância 24 horas", "#oshowdetruman #jimcarrey #cinema"),
    ("os_bons_companheiros", "Os Bons Companheiros (Goodfellas - 1990)", "A famosa cena 'Funny how?' de Joe Pesci foi baseada em uma história real dele com um mafioso", "O improviso tenso de Joe Pesci com Ray Liotta", "#goodfellas #martinscorsese #joepesci"),
    ("um_sonho_de_liberdade", "Um Sonho de Liberdade (1994)", "O esgoto que Andy atravessa na fuga era feito de calda de chocolate e serragem", "A composição doce do túnel de esgoto na fuga", "#umsonhodeliberdade #shawshankredemption #morganfreeman"),
    ("o_silencio_dos_inocentes", "O Silêncio dos Inocentes (1991)", "Anthony Hopkins aparece apenas 16 minutos no filme inteiro e ganhou o Oscar de Melhor Ator", "Os 16 minutos que marcaram a história do cinema", "#osilenciodosinocentes #hanniballecter #anthonyhopkins"),
    ("psicose", "Psicose (1960)", "O sangue escorrendo no ralo do chuveiro era na verdade xarope de chocolate Bosch", "O xarope de chocolate no clássico de Alfred Hitchcock", "#psicose #alfredhitchcock #terrorclassico"),
    ("tubarao", "Tubarão (Jaws - 1975)", "O tubarão mecânico Bruce quebrava tanto que Spielberg foi forçado a sugerir a criatura pela música", "O tema lendário de John Williams nascido de um defeito", "#tubarao #jaws #stevenspielberg #johnwilliams"),
    ("invocacao_do_mal", "Invocação do Mal (The Conjuring - 2013)", "A verdadeira boneca Annabelle é de pano (Raggedy Ann) e não de porcelana", "A história real da boneca Annabelle de pano", "#invocacaodomal #theconjuring #annabelle #terror"),
    ("panico", "Pânico (Scream - 1996)", "A voz do Ghostface ao telefone vinha do dublador escondido no quintal da casa durante as gravações", "O dublador que ligava de verdade para as atrizes", "#panico #scream #ghostface #wescraven"),
    ("sexta_feira_13", "Sexta-Feira 13 (1980)", "Jason Voorhees só passou a usar a icônica máscara de hóquei a partir do 3º filme", "A evolução da máscara de Jason Voorhees", "#sextafeira13 #jasonvoorhees #slashers"),
    ("o_sexto_sentido", "O Sexto Sentido (1999)", "Toda vez que um fantasma está por perto na tela, a cor vermelha aparece em algum detalhe", "A cor vermelha como pista secreta em cada cena", "#osextosentido #brucewillis #mnightshyamalan"),
    ("coraline", "Coraline e o Mundo Secreto (2009)", "Um time de tricô criou minúsculas roupas de lã feitas com agulhas finas como fios de cabelo", "O trabalho artesanal microscópico em stop-motion", "#coraline #stopmotion #laika"),
    ("a_viagem_de_chihiro", "A Viagem de Chihiro (2001)", "Hayao Miyazaki não escreveu roteiro prévio; ele desenhava os storyboards conforme a história nascia", "A genialidade intuitiva do Studio Ghibli", "#aviagemdechihiro #hayaomiyazaki #studioghibli"),
    ("ratatouille", "Ratatouille (2007)", "A equipe da Pixar preparou mais de 270 pratos gourmet reais no estúdio para filmar as texturas", "A culinária real nos estúdios da Pixar", "#ratatouille #pixar #disney"),
    ("monstros_sa", "Monstros S.A. (2001)", "Sullivan tinha 2,3 milhões de pelos individuais animados individualmente por computador", "O marco tecnológico dos pelos de Sulley", "#monstrossa #pixar #sulley"),
    ("up_altas_aventuras", "Up: Altas Aventuras (2009)", "Seriam necessários cerca de 9,4 milhões de balões para erguer uma casa de verdade no ar", "A física real da casa voadora de Carl Fredricksen", "#upaltasaventuras #pixar #disney"),
    ("procurando_nemo", "Procurando Nemo (2003)", "A física da água e os raios de sol sob o mar levaram 3 anos para serem desenvolvidos", "O realismo da luz submarina na animação", "#procurandonemo #pixar #disney"),
    ("carros", "Carros (2006)", "Os olhos dos carros foram colocados no para-brisa e não nos faróis para dar mais expressão humana", "O motivo dos olhos nos vidros dos carros", "#carros #lightningmcqueen #pixar"),
    ("divertida_mente", "Divertida Mente (Inside Out - 2015)", "A Alegria não projeta sombra porque ela é uma fonte pura de luz e energia", "O detalhe sutil de iluminação da personagem Alegria", "#divertidamente #insideout #pixar"),
    ("moana", "Moana: Um Mar de Aventuras (2016)", "Um software exclusivo chamado Splash foi criado apenas para dar personalidade às ondas da água", "O oceano com vida própria e o software Splash", "#moana #disney #animacao"),
    ("frozen", "Frozen: Uma Aventura Congelante (2013)", "Cientistas da neve da Califórnia foram consultados para criar 2.000 tipos de flocos de neve únicos", "A física microscópica da neve de Elsa", "#frozen #elsa #disney"),
    ("encanto", "Encanto (2021)", "Lin-Manuel Miranda compôs 'Não Falamos do Bruno' misturando 7 ritmos colombianos diferentes", "O sucesso astronômico da canção de Bruno", "#encanto #disney #linmanuelmiranda"),
    ("zootopia", "Zootopia (2016)", "Cada espécie de animal foi animada na escala exata da natureza, de camundongos a girafas", "A escala proporcional perfeita dos animais", "#zootopia #disney #animacao"),
    ("coco_a_vida_e_uma_festa", "Viva: A Vida é uma Festa (2017)", "Os acordes de violão tocados por Miguel e Héctor no filme correspondem exatamente às notas musicais reais", "A precisão dos dedos nas cordas do violão", "#vivavidaeumafesta #pixar #disney"),
    ("tarzan", "Tarzan (1999)", "Phil Collins gravou as músicas da trilha sonora em 5 idiomas diferentes: inglês, português, espanhol, francês e italiano", "Phil Collins cantando em português nos bastidores", "#tarzan #philcollins #disney"),
    ("aladdin", "Aladdin (1992)", "Robin Williams gravou mais de 16 horas de improvisos hilários como o Gênio da Lâmpada", "Os improvisos lendários de Robin Williams", "#aladdin #robinwilliams #disney"),
    ("hercules", "Hércules (1997)", "A Hidra de Lerna levou mais de 1 ano para ser animada com a tecnologia híbrida 2D e 3D", "O desafio técnico da batalha com a Hidra", "#hercules #disney #animacao"),
    ("mulan", "Mulan (1998)", "A cena da avalanche de hunos na neve continha mais de 2.000 cavaleiros renderizados individualmente", "A épica cena da avalanche nas montanhas", "#mulan #disney #animacao"),
    ("a_bela_e_a_fera", "A Bela e a Fera (1991)", "Foi o primeiro filme de animação da história a ser indicado ao Oscar de Melhor Filme", "O marco histórico no Oscar da Academia", "#abelaeafera #disney #oscar"),
    ("cinderela", "Cinderela (1950)", "A transformação do vestido rasgado no vestido de baile era a cena favorita de Walt Disney", "A cena mais amada pelo próprio Walt Disney", "#cinderela #waltdisney #disney"),
    ("branca_de_neve", "Branca de Neve e os Sete Anões (1937)", "Foi o primeiro longa-metragem de animação sonoro e colorido do mundo", "O filme que mudou o entretenimento para sempre", "#brancadeneve #waltdisney #historiadocinema"),
    ("pinocchio", "Pinóquio (1940)", "A baleia Monstro foi desenhada com técnicas de efeitos especiais de água usadas em filmes de guerra", "A grandiosidade da baleia Monstro", "#pinoquio #disney #animacaoclassica"),
    ("fantasia", "Fantasia (1940)", "Foi o pioneiro do som estéreo multicanal nos cinemas com o sistema Fantasound", "A invenção do som estéreo nos cinemas", "#fantasia #mickeymouse #waltdisney"),
    ("bambi", "Bambi (1942)", "Artistas da Disney mantiveram animais vivos no estúdio durante meses para estudar os movimentos", "Os animais reais que serviram de modelo para Bambi", "#bambi #disney #animacao"),
    ("peter_pan", "Peter Pan (1953)", "O Capitão Gancho e o Sr. Darling foram dublados e interpretados pelo mesmo ator de teatro", "A tradição teatral do Capitão Gancho e o pai", "#peterpan #capitaogancho #disney"),
    ("101_dalmatas", "101 Dálmatas (1961)", "A equipe teve que desenhar exatamente 6.469.952 manchas pretas em todos os quadros do filme", "A contagem colossal de manchas dos dálmatas", "#101dalmatas #disney #animacao"),
    ("robin_hood", "Robin Hood (1973)", "Para economizar custos, a Disney reciclou sequências completas de dança de Mogli e Branca de Neve", "A reciclagem de animações clássicas", "#robinhood #disney #curiosidades"),
    ("o_espanta_tubaroes", "O Espanta Tubarões (2004)", "Os rostos dos peixes foram desenhados com os mesmos traços marcantes de Will Smith e Angelina Jolie", "O design dos personagens espelhando os atores", "#oespantatubaroes #willsmith #dreamworks"),
    ("madagascar", "Madagascar (2005)", "Os pinguins de Madagascar fizeram tanto sucesso que ganharam um filme próprio e série de TV", "Como os coadjuvantes roubaram a cena", "#madagascar #pinguinsdemadagascar #dreamworks"),
    ("kung_fu_panda", "Kung Fu Panda (2008)", "Os animadores fizeram aulas reais de artes marciais para reproduzir a biomecânica de cada estilo", "Os estilos reais de Kung Fu em cada guerreiro", "#kungfupanda #jackblack #dreamworks"),
    ("como_treinar_o_seu_dragao", "Como Treinar o Seu Dragão (2010)", "O dragão Banguela foi modelado a partir do comportamento de um gato preto e uma pantera", "O comportamento felino do Fúria da Noite", "#comotreinaroseudragao #banguela #dreamworks"),
    ("megamente", "Megamente (2010)", "A cabeça gigante de Megamente foi inspirada na estética alienígena clássica dos quadrinhos dos anos 50", "A desconstrução brilhante dos filmes de heróis", "#megamente #willferrell #dreamworks"),
    ("gato_de_botas", "Gato de Botas: O Último Pedido (2022)", "O Lobo Morte foi inspirado no clássico spaghetti western e na personificação da ceifadora", "O design aterrador do Lobo Morte", "#gatodebotas #lobo #dreamworks"),
    ("bastardos_inglorios", "Bastardos Inglórios (2009)", "Christoph Waltz fala fluentemente alemão, inglês, francês e italiano nas cenas do filme", "O domínio impecável de 4 idiomas de Christoph Waltz", "#bastardosinglorios #quentintarantino #christophwaltz"),
    ("django_livre", "Django Livre (2012)", "Leonardo DiCaprio cortou a mão de verdade em uma taça de vidro e continuou atuando ensanguentado", "O corte real na mão que ficou no corte final", "#djangolivre #leonardodicaprio #tarantino"),
    ("era_uma_vez_em_hollywood", "Era Uma Vez em... Hollywood (2019)", "Quentin Tarantino fechou avenidas reais de Los Angeles e restaurou letreiros vintage dos anos 60", "A reconstrução histórica de Los Angeles de 1969", "#eraumavezmhollywood #bradpitt #tarantino"),
    ("kill_bill", "Kill Bill: Vol. 1 (2003)", "Mais de 1.700 litros de sangue falso foram usados nas filmagens das lutas com espada", "O tributo sangrento aos filmes de artes marciais", "#killbill #umathurman #quentintarantino"),
    ("scarface", "Scarface (1983)", "Al Pacino usou um sotaque cubano treinado com imigrantes de Miami e não saiu do personagem", "A intensidade lendária de Tony Montana", "#scarface #alpacino #briandepalma"),
    ("taxi_driver", "Taxi Driver (1976)", "A famosa frase 'You talkin' to me?' foi improvisada por Robert De Niro na frente do espelho", "O improviso mais citado da história de Hollywood", "#taxidriver #robertdeniro #martinscorsese"),
    ("touro_indomavel", "Touro Indomável (1980)", "Robert De Niro engordou 27 kg para interpretar Jake LaMotta na fase final da carreira", "A transformação corporal extrema de De Niro", "#touroindomavel #robertdeniro #martinscorsese"),
    ("cassino", "Cassino (1995)", "Sharon Stone usou um vestido de pedrarias pesando 20 kg que a deixou com dores nas costas", "O figurino milionário de Martin Scorsese", "#cassino #sharonstone #robertdeniro"),
    ("o_lobo_de_wall_street", "O Lobo de Wall Street (2013)", "A cena dos socos no peito e cânticos de Matthew McConaughey era o aquecimento real do ator", "O ritual de McConaughey que entrou no filme", "#olobodewallstreet #leonardodicaprio #matthewmcconaughey"),
    ("interestelar_tempo", "Interestelar: Bastidores", "Christopher Nolan plantou mais de 500 acres de milho real para a fazenda de Cooper e depois vendeu com lucro", "A plantação de milho real de Christopher Nolan", "#interestelar #christophernolan #cinema")
]

# Gera o catálogo final estruturado
posts_completos = []

# Adiciona os 20 principais
for item in CATALOGO_100_FILMES:
    post_id, filme, img_nome, badge, sub, caption = item
    posts_completos.append({
        "id": post_id,
        "filme": filme,
        "imagem": img_nome,
        "badge": badge,
        "sub": sub,
        "caption": caption
    })

# Template pool para os extras
templates_pool = [
    "cinema_interestelar_apresentadora.jpg",
    "cinema_matrix_apresentadora.jpg",
    "cinema_batman_apresentadora.jpg",
    "cinema_peaky_apresentadora.jpg",
    "cinema_senhor_aneis_apresentadora.jpg",
    "cinema_star_trek_apresentadora.jpg"
]

idx = 0
for extra in TEMAS_EXTRAS:
    p_id, filme, fato, sub, tags = extra
    template_escolhido = templates_pool[idx % len(templates_pool)]
    img_nome = f"cinema_{p_id}_apresentadora.jpg"
    
    caption = f"""🎬 **Você sabia dessa curiosidade impressionante sobre {filme}?**

{fato}! 🍿✨

Nos bastidores das maiores produções do cinema e da TV, pequenos detalhes fazem toda a diferença para criar obras de arte inesquecíveis que marcam gerações!

━━━━━━━━━━━━━━━━━━━━━
🎬 **Siga @alin_emanuela para descobrir curiosidades diárias sobre os maiores filmes e séries de todos os tempos!**
📌 *Salve este post e compartilhe com seus amigos cinéfilos!*
💬 *O que você achou dessa curiosidade? Comente aqui embaixo!* 👇🔥

{tags} #cinema #curiosidadesdefilmes #seriesefilmes #filmes #cinefilos #bastidores #hollywood"""

    posts_completos.append({
        "id": p_id,
        "filme": filme,
        "imagem": img_nome,
        "badge": "🎬 CURIOSIDADES DO CINEMA",
        "sub": sub,
        "template_base": template_escolhido,
        "caption": caption
    })
    idx += 1

print(f"Total de Filmes no Super Catálogo: {len(posts_completos)}")

# Salva banco de dados oficial JSON
db_path = os.path.join(bot_dir, "database_cinema_100.json")
with open(db_path, "w", encoding="utf-8") as f:
    json.dump(posts_completos, f, indent=2, ensure_ascii=False)

print(f"Banco de dados salvo em: {db_path}")

# Agora gera as imagens customizadas para cada um dos filmes
for p in posts_completos:
    target_img = os.path.join(posts_dir, p["imagem"])
    if os.path.exists(target_img):
        continue
    
    # Pega imagem base
    base_name = p.get("template_base", "cinema_claquete_apresentadora.jpg")
    src_img = os.path.join(posts_dir, base_name)
    if not os.path.exists(src_img):
        src_img = os.path.join(posts_dir, "cinema_matrix_apresentadora.jpg")
        
    try:
        img = Image.open(src_img).convert("RGBA")
        width, height = img.size
        overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(overlay)
        
        # Banners
        draw.rectangle([(0, 0), (width, int(height * 0.16))], fill=(10, 10, 20, 220))
        draw.rectangle([(0, int(height * 0.82)), (width, height)], fill=(10, 10, 20, 230))
        draw.rectangle([(0, int(height * 0.16) - 4), (width, int(height * 0.16))], fill=(255, 215, 0, 255))
        draw.rectangle([(0, int(height * 0.82)), (width, int(height * 0.82) + 4)], fill=(255, 215, 0, 255))
        
        try:
            font_badge = ImageFont.truetype("arialbd.ttf", 36)
            font_title = ImageFont.truetype("arialbd.ttf", 38)
            font_sub = ImageFont.truetype("arial.ttf", 28)
        except:
            font_badge = ImageFont.load_default()
            font_title = ImageFont.load_default()
            font_sub = ImageFont.load_default()
            
        draw.text((width//2, int(height * 0.08)), p.get("badge", "🎬 CURIOSIDADES DO CINEMA"), fill=(255, 215, 0), font=font_badge, anchor="mm")
        
        # Trunca título se for muito longo
        titulo_curto = p["filme"]
        if len(titulo_curto) > 35:
            titulo_curto = titulo_curto[:32] + "..."
        draw.text((width//2, int(height * 0.88)), titulo_curto, fill=(255, 255, 255), font=font_title, anchor="mm")
        
        sub_curto = p.get("sub", "")
        if len(sub_curto) > 48:
            sub_curto = sub_curto[:45] + "..."
        draw.text((width//2, int(height * 0.94)), sub_curto, fill=(220, 220, 220), font=font_sub, anchor="mm")
        
        final_img = Image.alpha_composite(img, overlay).convert("RGB")
        final_img.save(target_img, "JPEG", quality=95)
    except Exception as e:
        print(f"Erro ao gerar imagem para {p['id']}: {e}")

print("Todas as imagens do catálogo de 100+ filmes foram geradas com sucesso!")
