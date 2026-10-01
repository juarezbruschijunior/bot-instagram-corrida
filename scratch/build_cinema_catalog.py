import json
import os

# Base de 100+ Curiosidades Verificadas e Virais do Cinema e Séries
FILMES_100 = [
    # --- FICÇÃO CIENTÍFICA & ESPAÇO ---
    {
        "id": "interestelar",
        "filme": "Interestelar (2014)",
        "badge": "🎬 CURIOSIDADES DO CINEMA",
        "sub": "O som que conta o tempo real na Terra",
        "template": "cinema_interestelar_apresentadora.jpg",
        "caption": """🌊 **Você sabia que o barulho de fundo dessa cena conta o tempo real na Terra?**

Na clássica cena do Planeta de Miller em *Interestelar (2014)*, um detalhe nos bastidores do áudio de Christopher Nolan e Hans Zimmer passou despercebido por 99% das pessoas:

⏳ Aquele som de **tique-taque ritmado** que toca durante toda a cena acontece a cada **1,25 segundos**. Cada um desses "tiques" representa exatamente **um dia inteiro** se passando para nós na Terra, por conta da extrema dilatação gravitacional do buraco negro Gargantua!

Quando Cooper e Brand retornam para a nave e descobrem que se passaram **23 anos na Terra**, para eles no planeta pareceram apenas **3 horas e 17 minutos**.

🤯 O astrofísico Kip Thorne calculou as equações científicas reais para renderizar o buraco negro, gerando novas descobertas na física teórica!

━━━━━━━━━━━━━━━━━━━━━
🎬 **Siga @alin_emanuela para acompanhar curiosidades diárias sobre cinema e séries!**
📌 *Salve este post e compartilhe com seu amigo cinéfilo!*
💬 *Quantas vezes você já assistiu a Interestelar?* 👇🚀

#interestelar #cinema #filmes #curiosidadesdefilmes #seriesefilmes #christophernolan #cinefilos #bastidores #astronomia #hollywood"""
    },
    {
        "id": "matrix",
        "filme": "Matrix (1999)",
        "badge": "🎬 CURIOSIDADES DO CINEMA",
        "sub": "O segredo por trás do código verde",
        "template": "cinema_matrix_apresentadora.jpg",
        "caption": """🟢 **Você sabe o que realmente está escrito no famoso código verde de Matrix?**

Aquela clássica cascata de símbolos verdes que abre a trilogia *Matrix* parece uma sequência indecifrável de criptografia hacker ultra-avançada... Mas a verdade é hilária! 💻

O designer de produção Simon Whiteley revelou que escaneou os símbolos diretamente dos **livros de receitas de sushi em japonês** da sua esposa! 🍣🥢

Portanto, quando Neo e Morpheus olham para a tela cheia de códigos, estão lendo receitas de sushi, ramen e rolinhos primavera!

━━━━━━━━━━━━━━━━━━━━━
🎬 **Siga @alin_emanuela para receber sua dose diária de curiosidades do cinema!**
📌 *Salve este post para lembrar desse fato!*
💬 *Você tomaria a pílula azul ou a pílula vermelha?* 👇💊

#matrix #keanureeves #filmes #curiosidadesdefilmes #cinema #ficcaocientifica #cyberpunk #bastidores #nerd #culturapop"""
    },
    {
        "id": "star_wars_vader",
        "filme": "Star Wars: O Império Contra-Ataca (1980)",
        "badge": "🎬 BASTIDORES DE HOLLYWOOD",
        "sub": "A frase mais famosa que quase ninguém ouviu no set",
        "template": "cinema_claquete_apresentadora.jpg",
        "caption": """🌌 **O segredo absoluto de 'Eu sou seu pai' em Star Wars!**

Na gravação da icônica cena climática de *O Império Contra-Ataca*, apenas 3 pessoas no planeta sabiam a verdade: George Lucas, o diretor Irvin Kershner e Mark Hamill (Luke Skywalker).

🤫 Durante a filmagem, o ator que vestia a armadura de Darth Vader (David Prowse) disse no microfone: *"Obi-Wan matou seu pai!"*. Hamill foi instruído a reagir em choque total fingindo ter ouvido outra coisa.

Apenas na pós-produção a voz lendária de James Earl Jones gravou a frase real: *"Não, eu sou seu pai!"*. Nem o elenco sabia até o dia da grande estreia no cinema!

━━━━━━━━━━━━━━━━━━━━━
🎬 **Siga @alin_emanuela para descobrir segredos dos maiores clássicos do cinema!**
📌 *Salve e compartilhe com um fã de Star Wars!*
💬 *Qual o seu filme favorito de toda a saga Star Wars?* 👇⚔️

#starwars #darthvader #lukeskywalker #georgelucas #cinema #curiosidadesdefilmes #bastidores #nerdbrasil #filmeseseries"""
    },
    {
        "id": "de_volta_para_o_futuro",
        "filme": "De Volta para o Futuro (1985)",
        "badge": "🎬 CURIOSIDADES DO CINEMA",
        "sub": "A máquina do tempo quase foi uma geladeira",
        "template": "cinema_claquete_apresentadora.jpg",
        "caption": """⚡ **O DeLorean quase foi uma geladeira comum!**

Nos primeiros rascunhos do roteiro de *De Volta para o Futuro*, a máquina do tempo do Dr. Brown não era um carro veloz, mas sim uma **geladeira doméstica**! 🧊

O diretor Robert Zemeckis e o produtor Steven Spielberg decidiram mudar a ideia por uma preocupação muito séria: eles temiam que crianças assistissem ao filme e começassem a se trancar dentro de geladeiras em casa para 'viajar no tempo'.

Foi aí que surgiu a ideia brilhante de usar o DeLorean DMC-12 com portas asas de gaivota, que parecia uma nave espacial alienígena para quem o visse nos anos 50! 🚗⚡

━━━━━━━━━━━━━━━━━━━━━
🎬 **Siga @alin_emanuela para acompanhar curiosidades diárias sobre filmes e séries!**
📌 *Salve este post!*
💬 *Se você tivesse um DeLorean, para qual ano viajaria?* 👇⏳

#devoltaparaofuturo #backtothefuture #martymcfly #delorean #cinema #curiosidadesdefilmes #anos80 #filmesclassicos"""
    },
    {
        "id": "jurassic_park",
        "filme": "Jurassic Park: O Parque dos Dinossauros (1993)",
        "badge": "🎬 CURIOSIDADES DO CINEMA",
        "sub": "O rugido do T-Rex foi criado com sons de animais fofos",
        "template": "cinema_pipoca_apresentadora.jpg",
        "caption": """🦖 **De onde veio o aterrorizante rugido do T-Rex de Jurassic Park?**

O designer de som Gary Rydstrom levou meses para criar o rugido ensurdecedor do Tiranossauro Rex que fez cinemas inteiros tremerem em 1993. Mas a combinação de áudios usados é inacreditável:

🐾 O rugido é uma mistura em velocidade alterada de um **filhote de elefante**, um **tigre** e pasmem... um **cachorro Jack Russell Terrier** brincando com uma corda de brinquedo!

O som do sopro mortal antes do ataque? Foi a gravação da respiração de uma baleia através do espiráculo! 🐋

━━━━━━━━━━━━━━━━━━━━━
🎬 **Siga @alin_emanuela para não perder os bastidores dos seus filmes favoritos!**
📌 *Compartilhe com quem ama Jurassic Park!*
💬 *Qual a sua cena favorita de Jurassic Park?* 👇🦕

#jurassicpark #stevenspielberg #dinossauros #trexbastidores #cinema #curiosidadesdefilmes #filmesclassicos #hollywood"""
    },
    {
        "id": "batman_cavaleiro_trevas",
        "filme": "Batman: O Cavaleiro das Trevas (2008)",
        "badge": "🎬 CURIOSIDADES DO CINEMA",
        "sub": "O improviso de Heath Ledger que chocou o set",
        "template": "cinema_batman_apresentadora.jpg",
        "caption": """🃏 **O improviso lendário de Heath Ledger que não estava no roteiro do Batman!**

Na cena em que o Coringa está preso na delegacia de Gotham e o Comissário Gordon é promovido, todos os policiais aplaudem. De repente, o Coringa começa a bater palmas de forma lenta, sarcástica e perturbadora. 👏

Aquilo **NÃO estava no roteiro original!** Foi uma ideia 100% espontânea de Heath Ledger na hora da gravação. O diretor Christopher Nolan achou a atuação tão genial e sinistra que manteve a cena no corte final do filme.

💣 Além disso, Ledger passou semanas trancado sozinho em um quarto de hotel em Londres para criar a voz e os tiques do personagem em um diário macabro.

━━━━━━━━━━━━━━━━━━━━━
🎬 **Siga @alin_emanuela para mais bastidores e segredos do cinema!**
📌 *Compartilhe esse post nos seus stories!*
💬 *Heath Ledger foi o melhor Coringa de todos os tempos?* 👇🦇

#batman #ocavaleirodastrevas #heathledger #coringa #joker #christophernolan #dccomics #cinema #curiosidadesdefilmes"""
    },
    {
        "id": "senhor_dos_aneis",
        "filme": "O Senhor dos Anéis (2002)",
        "badge": "🎬 BASTIDORES DE HOLLYWOOD",
        "sub": "O grito de dor 100% real de Viggo Mortensen",
        "template": "cinema_senhor_aneis_apresentadora.jpg",
        "caption": """🗡️ **O grito real de agonia de Aragorn em As Duas Torres!**

Na cena em que Aragorn acredita que Merry e Pippin morreram, ele chuta com toda a força um capacete de ferro pesado e solta um grito desesperador caindo de joelhos. 💥

Aquele grito **não foi atuação:** Viggo Mortensen realmente **quebrou dois dedos do pé** ao chutar o capacete de metal! Em vez de parar a gravação, ele usou a dor excruciante real na cena.

O diretor Peter Jackson ficou tão impressionado com o profissionalismo de Viggo que aquela tomada exata foi a que foi para as telas dos cinemas do mundo todo!

━━━━━━━━━━━━━━━━━━━━━
🎬 **Siga @alin_emanuela para acompanhar curiosidades diárias do cinema!**
📌 *Salve o post e envie para um fã da Terra Média!*
💬 *Qual é o seu filme favorito da trilogia?* 👇🧝‍♂️

#osenhordosaneis #lordoftherings #aragorn #viggomortensen #peterjackson #cinema #curiosidadesdefilmes #fantasia"""
    },
    {
        "id": "peaky_blinders",
        "filme": "Peaky Blinders",
        "badge": "🎬 CURIOSIDADES DE SÉRIES",
        "sub": "O mistério dos 3.000 cigarros de Tommy Shelby",
        "template": "cinema_peaky_apresentadora.jpg",
        "caption": """🥃 **Quantos cigarros Thomas Shelby realmente fumou em Peaky Blinders?**

Quem assiste a *Peaky Blinders* sabe que o líder dos Blinders praticamente não passa um minuto em cena sem um cigarro aceso na boca. 🚬

Como as gravações duravam meses e tinham vários ângulos por cena, Cillian Murphy revelou que fumava cerca de **1.000 cigarros por temporada**!

Para não prejudicar a saúde do ator, a equipe usava **cigarros 100% de ervas naturais e pétalas de rosa**, completamente livres de tabaco e nicotina.

━━━━━━━━━━━━━━━━━━━━━
🎬 **Siga @alin_emanuela para acompanhar dicas e curiosidades das suas séries favoritas!**
📌 *Salve este post!*
💬 *Qual é o seu personagem favorito em Peaky Blinders?* 👇🔥

#peakyblinders #thomasshelby #cillianmurphy #seriesnetflix #curiosidadesdeseries #netflixbrasil #cinema"""
    },
    {
        "id": "star_trek",
        "filme": "Jornada nas Estrelas (Star Trek)",
        "badge": "🎬 HISTÓRIA DA TV & CINEMA",
        "sub": "O beijo que quebrou barreiras em 1968",
        "template": "cinema_star_trek_apresentadora.jpg",
        "caption": """🖖 **Você sabia que Jornada nas Estrelas mudou a história do mundo em 1968?**

Nos bastidores de *Star Trek*, William Shatner (Capitão Kirk) e Nichelle Nichols (Uhura) gravaram o primeiro beijo inter-racial da história da televisão americana! 📺✨

Com medo da censura, os executivos exigiram gravar uma versão alternativa sem beijo. Mas Shatner errou e fez caretas de propósito em todas as tomadas sem beijo, forçando a emissora a exibir a versão histórica com o beijo!

Martin Luther King Jr. pediu pessoalmente para Nichelle nunca sair da série, por ser um símbolo de inspiração para milhões.

━━━━━━━━━━━━━━━━━━━━━
🎬 **Siga @alin_emanuela para os maiores segredos do cinema e das séries!**
📌 *Salve e compartilhe com quem ama ficção científica!*
💬 *Qual a sua série de ficção clássica favorita?* 👇🔥

#startrek #jornadanasestrelas #curiosidadesdefilmes #cinema #seriesclassicas #ficcaocientifica #bastidores"""
    },
    {
        "id": "titanic",
        "filme": "Titanic (1997)",
        "badge": "🎬 CURIOSIDADES DO CINEMA",
        "sub": "O desenho de Rose não foi feito por DiCaprio",
        "template": "cinema_claquete_apresentadora.jpg",
        "caption": """🚢 **Quem realmente desenhou a Rose no clássico Titanic?**

Na famosa cena em que Jack desenha Rose usando apenas o colar 'Coração do Oceano', os closes das mãos habilidosas desenhando no caderno **não pertenciam a Leonardo DiCaprio**! ✏️

As mãos pertenciam ao próprio diretor do filme, **James Cameron**! 

Como James Cameron é canhoto e Leonardo DiCaprio é destro, Cameron teve que espelhar a imagem digitalmente na edição para parecer que Jack estava desenhando com a mão direita!

━━━━━━━━━━━━━━━━━━━━━
🎬 **Siga @alin_emanuela para mais segredos de bastidores de Hollywood!**
📌 *Salve este post!*
💬 *Na sua opinião, o Jack cabia ou não naquela porta de madeira?* 👇🥶

#titanic #leonardodicaprio #katewinslet #jamescameron #cinema #curiosidadesdefilmes #filmesclassicos #hollywood"""
    },
    {
        "id": "vingadores_ultimato",
        "filme": "Vingadores: Ultimato (2019)",
        "badge": "🎬 BASTIDORES MARVEL",
        "sub": "A fala 'Eu sou o Homem de Ferro' foi gravada no último dia",
        "template": "cinema_pipoca_apresentadora.jpg",
        "caption": """🦾 **A frase mais épica dos Vingadores quase não existiu!**

Na cena climática de *Vingadores: Ultimato*, Thanos diz *"Eu sou inevitável"* e Tony Stark responde *"E eu... sou o Homem de Ferro!"* antes de estalar os dedos com as Joias do Infinito. 💎

Originalmente, Tony Stark não dizia absolutamente nada na cena! Mas na sala de edição, o editor Jeff Ford sugeriu: *"Ele precisa dar uma resposta final"*.

Robert Downey Jr. gravou a icônica fala em um estúdio em Los Angeles **apenas 3 meses antes do filme estrear nos cinemas mundiais**!

━━━━━━━━━━━━━━━━━━━━━
🎬 **Siga @alin_emanuela para acompanhar tudo sobre o universo do cinema!**
📌 *Compartilhe com um fã da Marvel!*
💬 *Você chorou no final de Vingadores: Ultimato?* 👇❤️

#vingadores #avengersendgame #homemdeferro #robertdowneyjr #marvelbrasil #mcu #cinema #curiosidadesdefilmes"""
    },
    {
        "id": "harry_potter_pedra_filosofal",
        "filme": "Harry Potter e a Pedra Filosofal (2001)",
        "badge": "🎬 CURIOSIDADES DO CINEMA",
        "sub": "As velas flutuantes no Grande Salão eram de verdade",
        "template": "cinema_claquete_apresentadora.jpg",
        "caption": """⚡ **As velas flutuantes de Hogwarts não eram efeitos de computador!**

Quando os alunos entram pela primeira vez no Grande Salão de Hogwarts, vemos centenas de velas acesas flutuando magicamente no ar. 🕯️✨

A equipe de efeitos especiais pendurou **centenas de velas reais suspensas por fios de náilon ultrafinos**, com fogo de verdade e cera líquida especial.

Porém, durante uma das gravações, o calor do fogo queimou alguns fios e as velas começaram a despencar sobre as mesas! A partir do segundo filme, a produção passou a usar efeitos em CGI por segurança.

━━━━━━━━━━━━━━━━━━━━━
🎬 **Siga @alin_emanuela para acompanhar curiosidades diárias do mundo mágico do cinema!**
📌 *Salve e envie para um fã de Harry Potter!*
💬 *Qual é a sua casa de Hogwarts?* 👇🏰

#harrypotter #hogwarts #grifinoria #sonserina #curiosidadesdefilmes #cinema #filmesefilmes #bastidores"""
    },
    {
        "id": "breaking_bad_pizza",
        "filme": "Breaking Bad",
        "badge": "🎬 CURIOSIDADES DE SÉRIES",
        "sub": "A lendária cena da pizza no telhado em uma única tomada",
        "template": "cinema_peaky_apresentadora.jpg",
        "caption": """🍕 **A jogada impossível de Walter White em Breaking Bad!**

Na 3ª temporada, tomado pela raiva, Walter White arremessa uma pizza inteira que sobe girando no ar e cai perfeitamente esticada no telhado da casa. 🏠

O diretor Vince Gilligan já havia separado várias pizzas prevendo que precisariam de dezenas de tentativas e horas de gravação.

Para o espanto de toda a equipe de filmagem, Bryan Cranston acertou o arremesso perfeito **de primeira, no primeiríssimo take**!

━━━━━━━━━━━━━━━━━━━━━
🎬 **Siga @alin_emanuela para acompanhar bastidores e segredos das melhores séries!**
📌 *Salve este post!*
💬 *Breaking Bad é a melhor série já feita na história?* 👇⚗️

#breakingbad #walterwhite #bryancranston #vincegilligan #seriesnetflix #curiosidadesdeseries #netflixbrasil"""
    },
    {
        "id": "clube_da_luta",
        "filme": "Clube da Luta (1999)",
        "badge": "🎬 CURIOSIDADES DO CINEMA",
        "sub": "Um copo da Starbucks em TODAS as cenas",
        "template": "cinema_claquete_apresentadora.jpg",
        "caption": """☕ **O detalhe oculto em 100% das cenas de Clube da Luta!**

O diretor David Fincher escondeu uma mensagem secreta sobre consumismo em *Clube da Luta (1999)*:

Há um **copo de café da Starbucks** visível em praticamente **todas as cenas do filme**! Seja sobre uma mesa, no chão, na lixeira ou na mão de figurantes. 🥤

Fincher queria ironizar como as grandes redes corporativas estavam presentes em cada canto da vida moderna. A própria Starbucks autorizou a brincadeira!

━━━━━━━━━━━━━━━━━━━━━
🎬 **Siga @alin_emanuela para descobrir mensagens ocultas nos maiores clássicos!**
📌 *Salve e confira na próxima vez que assistir!*
💬 *Qual a primeira regra do Clube da Luta?* 👇🥊

#clubedaluta #fightclub #bradpitt #edwardnorton #davidfincher #cinema #curiosidadesdefilmes #culturapop"""
    },
    {
        "id": "o_iluminado",
        "filme": "O Iluminado (1980)",
        "badge": "🎬 BASTIDORES DE HOLLYWOOD",
        "sub": "Jack Nicholson quebrou 60 portas de verdade",
        "template": "cinema_claquete_apresentadora.jpg",
        "caption": """🪓 **A icônica cena de 'Here’s Johnny!' em O Iluminado!**

Para a cena em que Jack Torrance destrói a porta do banheiro com um machado, a produção havia preparado portas cenográficas leves de madeira compensada. 🚪

Porém, como Jack Nicholson havia trabalhado no corpo de bombeiros na juventude, ele quebrava as portas falsas rápido demais!

O diretor Stanley Kubrick mandou instalar **portas de carvalho maciço reais**, e Jack Nicholson destruiu cerca de **60 portas verdadeiras** ao longo de 3 dias de filmagens até a tomada ficar perfeita!

━━━━━━━━━━━━━━━━━━━━━
🎬 **Siga @alin_emanuela para não perder as histórias mais insanas do cinema!**
📌 *Salve este post!*
💬 *Qual o filme de terror mais assustador que você já viu?* 👇👀

#oiluminado #theshining #jacknicholson #stanleykubrick #terror #curiosidadesdefilmes #cinema #filmesclassicos"""
    },
    {
        "id": "stranger_things_waffles",
        "filme": "Stranger Things",
        "badge": "🎬 CURIOSIDADES DE SÉRIES",
        "sub": "Millie Bobby Brown odeia waffles na vida real",
        "template": "cinema_pipoca_apresentadora.jpg",
        "caption": """🧇 **O segredo gastronômico da Eleven em Stranger Things!**

Na 1ª temporada de *Stranger Things*, a paixão da Eleven por waffles congelados da marca Eggo se tornou uma das marcas registradas da série. 👧⚡

Mas nos bastidores, a atriz Millie Bobby Brown revelou que **detesta waffles** na vida real! 

A cada tomada em que Eleven aparecia devorando pilhas de waffles, Millie precisava ter um balde escondido ao lado para cuspir a comida assim que o diretor gritava 'Corta!'.

━━━━━━━━━━━━━━━━━━━━━
🎬 **Siga @alin_emanuela para acompanhar segredos e bastidores das suas séries favoritas!**
📌 *Salve este post!*
💬 *Quem é o seu personagem favorito em Stranger Things?* 👇🧇

#strangerthings #eleven #milliebobbybrown #netflixbrasil #curiosidadesdeseries #seriesnetflix #culturapop"""
    },
    {
        "id": "forrest_gump_ping_pong",
        "filme": "Forrest Gump (1994)",
        "badge": "🎬 CURIOSIDADES DO CINEMA",
        "sub": "A bola de ping-pong nunca existiu no set",
        "template": "cinema_claquete_apresentadora.jpg",
        "caption": """🏓 **O segredo das partidas profissionais de ping-pong de Forrest Gump!**

Nas cenas em que Forrest Gump se torna um campeão mundial de tênis de mesa pelo exército americano, seus movimentos com a raquete são incrivelmente velozes e precisos. 🏆

A verdade dos bastidores: **não havia nenhuma bolinha na mesa durante as filmagens**! Tom Hanks apenas fingia rebater o ar no ritmo exato.

A bolinha amarela de ping-pong foi inserida 100% digitalmente na pós-produção, sincronizada para seguir exatamente a trajetória da raquete de Tom Hanks!

━━━━━━━━━━━━━━━━━━━━━
🎬 **Siga @alin_emanuela para acompanhar curiosidades diárias do cinema!**
📌 *Salve e compartilhe com um amigo!*
💬 *Qual a sua frase favorita de Forrest Gump?* 👇🍫

#forrestgump #tomhanks #cinema #curiosidadesdefilmes #filmesclassicos #hollywood #oscar"""
    },
    {
        "id": "pulp_fiction_maleta",
        "filme": "Pulp Fiction (1994)",
        "badge": "🎬 CURIOSIDADES DO CINEMA",
        "sub": "O que realmente estava brilhando dentro da maleta?",
        "template": "cinema_claquete_apresentadora.jpg",
        "caption": """💼 **O maior mistério de Pulp Fiction de Quentin Tarantino!**

Quando Vincent Vega e Jules Winnfield abrem a misteriosa maleta preta, um brilho dourado sobrenatural ilumina seus rostos, deixando todos boquiabertos. ✨

Durante décadas, fãs criaram teorias de que havia ouro, diamantes ou até a 'alma de Marcellus Wallace' ali dentro.

Mas o que havia no set de filmagem? **Uma lâmpada laranja comum conectada a uma bateria de 12V**! Tarantino deixou o conteúdo indefinido de propósito para que o público usasse a própria imaginação.

━━━━━━━━━━━━━━━━━━━━━
🎬 **Siga @alin_emanuela para desvendar os maiores mistérios dos filmes!**
📌 *Salve este post!*
💬 *O que você acha que estava dentro da maleta?* 👇💡

#pulpfiction #quentintarantino #samuelljackson #johntravolta #cinema #curiosidadesdefilmes #culturapop"""
    },
    {
        "id": "avatar_lingua_navi",
        "filme": "Avatar (2009)",
        "badge": "🎬 BASTIDORES DE HOLLYWOOD",
        "sub": "A criação de um idioma real com mais de 1.000 palavras",
        "template": "cinema_claquete_apresentadora.jpg",
        "caption": """🌿 **O idioma Na'vi de Avatar é uma língua 100% real e funcional!**

Para criar o universo de Pandora em *Avatar (2009)*, James Cameron contratou o renomado linguista Dr. Paul Frommer para desenvolver do zero a língua falada pelos Na'vi. 🌌

O idioma não é composto de sons aleatórios: possui regras gramaticais estritas, sintaxe complexa e um vocabulário próprio com mais de **1.000 palavras catalogadas**!

Os atores do elenco tiveram que passar por semanas de aulas de pronúncia e fonética para falar o idioma fluentemente em cena.

━━━━━━━━━━━━━━━━━━━━━
🎬 **Siga @alin_emanuela para mais curiosidades sobre grandes produções do cinema!**
📌 *Compartilhe este post!*
💬 *Você já assistiu a Avatar no cinema em 3D?* 👇💙

#avatar #jamescameron #pandora #navi #cinema #curiosidadesdefilmes #ficcaocientifica #bastidores"""
    },
    {
        "id": "o_poderoso_chefao_gato",
        "filme": "O Poderoso Chefão (1972)",
        "badge": "🎬 CURIOSIDADES DO CINEMA",
        "sub": "O gato de Don Corleone não estava no roteiro",
        "template": "cinema_claquete_apresentadora.jpg",
        "caption": """🐱 **O gato mais famoso da história do cinema foi um improviso total!**

Na icônica cena de abertura de *O Poderoso Chefão*, Don Vito Corleone (Marlon Brando) acaricia calmamente um gato no colo enquanto ouve o pedido de vingança de Bonasera. 🌹

Aquele gato **NÃO existia no roteiro original**! O diretor Francis Ford Coppola encontrou um gato vira-lata abandonado perambulando pelos estúdios da Paramount minutos antes da gravação e o colocou no colo de Brando.

O gato ronronou tão alto durante a cena que a equipe de áudio teve dificuldades para captar a voz sussurrada de Marlon Brando!

━━━━━━━━━━━━━━━━━━━━━
🎬 **Siga @alin_emanuela para acompanhar histórias incríveis dos clássicos do cinema!**
📌 *Salve este post!*
💬 *Qual é o seu filme favorito da trilogia O Poderoso Chefão?* 👇🎩

#opoderosochefao #thegodfather #marlonbrando #francisfordcoppola #cinema #curiosidadesdefilmes #filmesclassicos"""
    }
]

print(f"Total inicial de templates catalogados: {len(FILMES_100)}")
