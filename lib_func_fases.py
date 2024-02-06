import sys
import pygame
import random
import time
import tkinter as tk
from tkinter import filedialog
from fpdf import FPDF


perguntas = [
        {
            "pergunta": "Qual o nome deste sistema?",
            "opcoes": ["Circulatório", "Digestivo", "Endócrino", "Urinário", "Linfático"],
            "resposta": "Urinário",
            "imagem": "df"
        },
        {
            "pergunta": "Qual a função dos rins?",
            "opcoes": ["Produção de linfa", "Filtrar o sangue", "Produzir anticorpos", "Renovar células sanguíneas","Armazenar cálcio"],
            "resposta": "Filtrar o sangue",
            "imagem": "df"
        },
        {
            "pergunta": "Qual a localização dos rins?",
            "opcoes": ["Abdome", "Pelve", "Tórax, superior", "Crânio, caudal","Tórax, inferior"],
            "resposta": "Abdome",
            "imagem": "df"
        },
        {
            "pergunta": "Qual o nome deste órgão?",
            "opcoes": ["Rim", "Baço", "Fígado", "Linfonodo", "Pâncreas "],
            "resposta": "Rim",
            "imagem": "df2"
        },
        {
            "pergunta": "Qual o nome da glândula localizada no polo  superior do rim?",
            "opcoes": ["Tireóide", "Timo", "Supra-Renal", "Hipófie","Pituitária"],
            "resposta": "Supra-Renal",
            "imagem": "df2"
        }, 
        {
            "pergunta": "Qual o nome da artéria que irriga o rim?",
            "opcoes": ["Mesentérica", "Esplênica", "Basílica", "Renal","Linfática"],
            "resposta": "Renal",
            "imagem": "df3"
  
        },    
        {
            "pergunta": "Qual o nome da estrutura que transporta urina da pelve renal até a bexiga?",
            "opcoes": ["Uretra", "Ureter", "Néfrons", "Cálice Maior","Papila renal"],
            "resposta": "Ureter",
            "imagem": "df5"
        },       
        {
            "pergunta": "Quais as três porções do ureter?",
            "opcoes": ["Abdominal, Pélvica e Intramural", "Pélvica, Intreposta e adjacente", "Abdominal, Torácica e lombar", "Cervical, iguinal e umbilical", "Curva, reta e linear"],
            "resposta": "Abdominal, Pélvica e Intramural",
            "imagem": "df5"
        },
        {
            "pergunta": "Qual o nome deste órgão?",
            "opcoes": ["Vesícula biliar", "Coração", "Útero", "Bexiga Urinária","Prostáta"],
            "resposta": "Bexiga Urinária",
            "imagem": "df6"
        },
        {
            "pergunta": "Quem transporta urina da bexiga Urinária até o meio externo do corpo?",
            "opcoes": ["Ureter", "Canal seminal", "Uretra","Ducto ejaculatório","Vesícula seminal"],
            "resposta": "Uretra",
            "imagem": "df7"
        },
        {
            "pergunta": "Uretra é um órgão pertencente ao sistema",
            "opcoes": ["respiratório", "digestório", "endócrino","urinário","nervoso"],
            "resposta": "urinário",
            "imagem": "df7"
        },
        #
        {
            "pergunta": "A uretra feminina é responsável por transportar?",
            "opcoes": ["Sêmem e urina", "Sêmem","Urina","Plasma e sêmem", "Urina e sangue"],
            "resposta":"Urina",
            "imagem": "df8"
        },
        {
            "pergunta": "Quais são as principais funções do sangue?",
            "opcoes": ["Transporte e regulação", "Transporte, homeostase e proteção", "Transporte, hematose e proteção","Transporte e proteção", "Transporte, regulação e proteção" ],
            "resposta": "Transporte, regulação e proteção",
            "imagem": "df11"
        },
        {
            "pergunta": "Qual é a principal função das artérias?",
            "opcoes": ["É transportar o sangue sob baixa pressão até os tecidos", "É servir com um reservatório de sangue", "É realizar a troca entre os nutrientes","É transportar o sangue sob alta pressão até os tecidos", " É transportar o sangue sob alta ou baixa pressão até os tecidos" ],
            "resposta": "É transportar o sangue sob alta pressão até os tecidos",
            "imagem": "df12"
        },
        {
            "pergunta": "O que garante no sistema venoso a melhora do retorno venoso?",
            "opcoes": ["A pressão ser muito baixa e as paredes muito finas", "A pressão ser muito alta e as paredes muito finas", "A presença das válvulas nas veias","A presença das válvulas nas veias e a sua alta pressão", "A pressão ser muito baixa e as paredes muito grossas" ],
            "resposta": "A presença das válvulas nas veias",
            "imagem": "df12"
        },
        {
            "pergunta": "Nervo craniano que aciona os músculos da mímica da face é o:",
            "opcoes": ["oculomotor", "facial", "hipoglosso","trigêmeo", "abducente" ],
            "resposta": "facial",
            "imagem": "df13"
        },
        {
            "pergunta": "De acordo com conteúdos de neuroanatomia, assinale a alternativa correta:",
            "opcoes": ["Lobos frontais influenciam a atividade motora e o planejamento do comportamento",
                        "Lobos temporais processam o reconhecimento visual e a percepção nítida da imagem",
                          "Lobos parietais interpretam emoções e comportamento social",
                          "Lobo occipital é responsável pela compreensão dos sentidos de dor, calor e tato",
                            "Lobo da insula capta sinapses auditivas e olfativas" ],
            "resposta": "Lobos frontais influenciam a atividade motora e o planejamento do comportamento",
            "imagem": "df14"
        },
        {
            "pergunta": "As meninges se encontram dispostas, da parte superficial para profunda em:",
            "opcoes": ["Aracnoide, pia-máter e dura-máter",
                        "Pia-máter, dura-máter e aracnoide",
                          "Dura-máter, camada meníngea e pia-máter",
                          "Camada endosteal, dura-máter e aracnoide",
                            "Dura-máter, aracnoide e pia-máter" ],
            "resposta": "Dura-máter, aracnoide e pia-máter",
            "imagem": "df15"
        },
        {
            "pergunta": "Com base nos conhecimentos sobre neuroanatomia, assinale a alternativa correta.",
            "opcoes": ["Encontramos as meninges revestindo somente o encéfalo",
                        "O diencéfalo é formado por giros e sulcos",
                          "O centro da fome e da saciedade se localiza no cerebelo",
                          "A área de Wernicke (giro opercular) é a área cortical da audição",
                            "O tronco encefálico é dividido em: mesencéfalo, ponte e bulbo" ],
            "resposta": "O tronco encefálico é dividido em: mesencéfalo, ponte e bulbo",
            "imagem": "df16"
        },
        {
            "pergunta": "Quais são as estruturas que compõem o encéfalo de um adulto?",
            "opcoes": ["Cérebro, cerebelo, medula espinhal e tronco encefálico",
                        "Cérebro, cerebelo, diencéfalo e medula espinhal",
                          "Cérebro, cerebelo e sistema nervoso autônomo",
                          "Cérebro, cerebelo e sistema nervoso periférico",
                            "Cérebro, cerebelo e tronco encefálico" ],
            "resposta": "Cérebro, cerebelo e tronco encefálico",
            "imagem": "df17"
        },
        {
            "pergunta": "Lábios maiores, lábios menores, clitóris e vagina, compõem o que chamamos de:",
            "opcoes": ["pudendo feminino",
                        "vagina",
                          "sistema urinário feminino",
                          "hímen",
                            "vestíbulo feminino" ],
            "resposta": "pudendo feminino",
            "imagem": "df18"
        },
        {
            "pergunta": "Quais hormônios  correspondem ao desenvolvimento do folículo e ovulação?",
            "opcoes": ["FSH e LH",
                        "GH e LH",
                          "Progesterora e FSH",
                          "LH e Estrógeno",
                            "Estrógeno e progesterona" ],
            "resposta": "FSH e LH",
            "imagem": "df18"
        },
        {
            "pergunta": "Onde são produzidos os espermatozóides: ",
            "opcoes": ["Escroto",
                        "Epidídimo",
                          "Próstata",
                          "Testículo",
                            "Pênis" ],
            "resposta": "Testículo",
            "imagem": "df19"
        },
        {
            "pergunta": "Qual órgão possui a função comum ao sistema reprodutor e ao sistema urinário.",
            "opcoes": ["Ducto deferente",
                        "Ureter",
                          "Uretra",
                          "Bexiga",
                            "Epidídimo" ],
            "resposta": "Uretra",
            "imagem": "df19"
        },
        {
            "pergunta": "O corpo humano possui vários reflexos e instintos. O que é o reflexo da tosse?",
            "opcoes": ["É um mecanismo de defesa artificial",
                        "Não se sabe ainda qual é a função desse reflexo",
                          "Contração dos músculos da expiração que expelem o ar pelo nariz e pela boca",
                          "Não é um mecanismo de defesa natural",
                            "Mecanismo de defesa natural que remove agentes irritantes nas vias aéreas" ],
            "resposta": "Mecanismo de defesa natural que remove agentes irritantes nas vias aéreas",
            "imagem": "df20"
        },
        {
            "pergunta": "Quais são as funções da parte interna do nariz?",
            "opcoes": ["Aquecimento, umidificação e filtração do ar exalado",
                        "Aquecimento e filtração do ar inalado",
                          "Aquecimento, umidificação e filtração do ar inalado",
                          "Aquecimento e umidificação do ar inalado",
                            "Aquecimento e filtração do ar exalado" ],
            "resposta": "Aquecimento, umidificação e filtração do ar inalado",
            "imagem": "df21"
        },
         {
            "pergunta": "Qual é a principal causa do enfisema?",
            "opcoes": ["Poluição do ar",
                        "Poluentes industriais",
                          "Exposição ocupacional",
                          "Bebida alcoólica",
                            "Cigarro" ],
            "resposta": "Cigarro",
            "imagem": "df22"
        },
        {
            "pergunta": "Qual o nome deste sistema?",
            "opcoes": ["Circulatório",
                        "Digestivo",
                          "Endócrino",
                          "Urinário",
                            "Respiratório" ],
            "resposta": "Respiratório",
            "imagem": "df22"
        },
        {
            "pergunta": "Qual o nome deste sistema?",
            "opcoes": ["Circulatório",
                        "Digestivo",
                          "Endócrino",
                          "Urinário",
                            "Linfático" ],
            "resposta": "Endócrino",
            "imagem": "df23"
        },
        {
            "pergunta": "Qual o nome deste sistema?",
            "opcoes": ["Circulatório",
                        "Digestivo",
                          "Endócrino",
                          "Urinário",
                            "Linfático" ],
            "resposta": "Circulatório",
            "imagem": "df24"
        },
]

   # Definição das cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (200, 200, 200)

    # Definição das dimensões da tela
WIDTH = 1024
HEIGHT = 700

    # Inicialização do Pygame
pygame.init()

    # Criação da tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("QUIZ")

    # Carregando a imagem da roleta
roleta_image = pygame.image.load("imagens/roleta.png")
roleta_rect = roleta_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

fontname = "futura"
    # Fonte para as perguntas e opções
font = pygame.font.SysFont(fontname, 27)

font2 = pygame.font.SysFont(fontname, 22)

nome_jogador = ""

fase = 1

def create_buttons():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if exit_button_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()
                if play_again_button_rect.collidepoint(mouse_pos):
                    reiniciar_jogo()

        # Limpe a tela
        screen.fill(WHITE)

        # Desenhe os botões como retângulos
        button_width, button_height = 200, 50
        button_spacing = 20

        exit_button_rect = pygame.draw.rect(screen, BLACK, (WIDTH - button_spacing - button_width, HEIGHT - button_spacing - button_height, button_width, button_height))
        play_again_button_rect = pygame.draw.rect(screen, BLACK, (button_spacing, HEIGHT - button_spacing - button_height, button_width, button_height))

        # Desenhe o texto nos botões
        exit_text = font.render("SAIR", True, WHITE)
        play_again_text = font.render("JOGAR", True, WHITE)

        exit_text_rect = exit_text.get_rect(center=exit_button_rect.center)
        play_again_text_rect = play_again_text.get_rect(center=play_again_button_rect.center)

        screen.blit(exit_text, exit_text_rect)
        screen.blit(play_again_text, play_again_text_rect)

        pygame.display.flip()

def reiniciar_jogo():
    import lib_func_fases
    

def exibir_nome_jogador():
    global nome_jogador

    screen.fill(WHITE)

    campo_nome = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 25, 200, 50)
    pygame.draw.rect(screen, BLACK, campo_nome, 2)

    mensagem = font.render("Insira seu nome para iniciar o jogo", True, BLACK)
    mensagem_rect = mensagem.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
    screen.blit(mensagem, mensagem_rect)

    botao_jogar = pygame.Rect(WIDTH // 2 - 50, HEIGHT // 2 + 50, 100, 50)
    pygame.draw.rect(screen, BLACK, botao_jogar)
    texto_jogar = font.render("Jogar", True, WHITE)
    texto_rect_jogar = texto_jogar.get_rect(center=botao_jogar.center)
    screen.blit(texto_jogar, texto_rect_jogar)

    pygame.display.flip()

    digitando_nome = True
    jogando = True
    cursor_piscando = True
    cursor_tempo = 0
    while jogando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE and digitando_nome:
                    nome_jogador = nome_jogador[:-1]
                elif event.key == pygame.K_RETURN and digitando_nome:
                    digitando_nome = False
                else:
                    nome_jogador += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_jogar.collidepoint(event.pos):
                    jogando = False

        screen.fill(WHITE)
        pygame.draw.rect(screen, BLACK, campo_nome, 2)
        texto_nome = font.render(nome_jogador, True, BLACK)
        texto_rect_nome = texto_nome.get_rect(center=campo_nome.center)
        screen.blit(texto_nome, texto_rect_nome)

        pygame.draw.rect(screen, BLACK, botao_jogar)
        screen.blit(texto_jogar, texto_rect_jogar)

        if digitando_nome:
            if cursor_piscando:
                cursor = font.render("|", True, BLACK)
                cursor_rect = cursor.get_rect(midleft=(campo_nome.x + 10, campo_nome.centery))
                screen.blit(cursor, cursor_rect)

            if pygame.time.get_ticks() - cursor_tempo > 500:
                cursor_piscando = not cursor_piscando
                cursor_tempo = pygame.time.get_ticks()

        screen.blit(mensagem, mensagem_rect)  # Exibir a mensagem novamente

        pygame.display.flip()

    return nome_jogador

nome_jogador = exibir_nome_jogador()
print("Nome do jogador:", nome_jogador)

def exibir_resultado(pontuacao):
    screen.fill(WHITE)

    # Mensagem de resultado
    mensagem = f"Parabéns, {nome_jogador}! Sua pontuação foi: {pontuacao}"
    texto_mensagem = font.render(mensagem, True, BLACK)
    texto_rect_mensagem = texto_mensagem.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(texto_mensagem, texto_rect_mensagem)

    pygame.display.flip()  
 
pontuacao = 0
resposta_selecionada = None
jogando = True

def girar_roleta():
    angulo = 0
    velocidade = random.randint(20, 30)
    tempo_girar = random.randint(2, 12)
    tempo_parar = random.randint(2, 3)
    parar_angulo = random.randint(0, 359)

    start_time = time.time()

    pygame.mixer.music.load("som/piao-do-bau-com-musica.mp3")
    pygame.mixer.music.play()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Girar roleta
        if time.time() - start_time < tempo_girar:
            angulo += velocidade
            if angulo >= 360:
                angulo -= 360

        elif time.time() - start_time > tempo_girar + tempo_parar:
            if angulo == parar_angulo:
                pygame.mixer.music.stop()
                return exibir_pergunta_aleatoria()
                        
            
        else:
            angulo = parar_angulo

        # Rotação da imagem da roleta
        roleta_rotated = pygame.transform.rotate(roleta_image, -angulo)
        roleta_rect = roleta_rotated.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(roleta_rotated, roleta_rect)

        pygame.display.flip()

def exibir_pergunta_aleatoria():


    rodadas = 10

    for _ in range(rodadas):
    # Verifica se todas as perguntas já foram usadas
     if not perguntas:
        print("Todas as perguntas foram usadas!")
        break

    pergunta = random.choice(perguntas)
    perguntas.remove(pergunta)
    return exibir_pergunta(pergunta["pergunta"], pergunta["opcoes"], pergunta["resposta"], pergunta["imagem"])


# Defina as cores
BACKGROUND_COLOR = (240, 240, 240)  # Cor de fundo geral
QUESTION_COLOR = (220, 220, 220)  # Cor de fundo da pergunta
QUESTION_BORDER_COLOR = (230, 230, 230)  # Cor do contorno da pergunta
OPTION_COLOR = (200, 200, 200)  # Cor de fundo das opções de resposta
OPTION_HOVER_COLOR = (180, 180, 180)  # Cor de fundo das opções de resposta quando o mouse estiver sobre elas
OPTION_TEXT_COLOR = (0, 0, 0)  # Cor do texto das opções de resposta

def exibir_pergunta(pergunta, opcoes, resposta, imagem):
    screen.fill(BACKGROUND_COLOR)

 # Definir tamanho e posição da moldura
    moldura_width = 200
    moldura_height = 265
    moldura_x = (WIDTH - moldura_width) // 2
    moldura_y = (HEIGHT - moldura_height) // 6

    # Desenhar moldura
    pygame.draw.rect(screen, QUESTION_BORDER_COLOR, (moldura_x, moldura_y, moldura_width, moldura_height))
    pygame.draw.rect(screen, QUESTION_COLOR, (moldura_x + 2, moldura_y + 2, moldura_width - 4, moldura_height - 4))

    # Função para exibir imagem
    imagem_path = f"imagens/{imagem}.png"  # Substitua pelo caminho correto da imagem
    img = pygame.image.load(imagem_path)
    img_rect = img.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 140))  # Ajuste a coordenada Y para posicionar acima do texto
    screen.blit(img, img_rect)

    
    texto_pergunta = font.render(pergunta, True, BLACK)
    texto_rect_pergunta = texto_pergunta.get_rect(center=(WIDTH // 2, HEIGHT // 1.8))
    screen.blit(texto_pergunta, texto_rect_pergunta)

    # Desenhar opções
    option_width = 700 
    option_height = 35
    option_x = (WIDTH - option_width) // 2
    option_y = HEIGHT // 2 + 90
    option_spacing = 12

    option_rects = []
    for i, opcao in enumerate(opcoes):
        option_rect = pygame.Rect(option_x, option_y + (option_height + option_spacing) * i, option_width, option_height)
        option_rects.append(option_rect)

    pygame.display.flip()

    # Esperar pela resposta do jogador
    resposta_selecionada = None
    while resposta_selecionada is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEMOTION:
                for i, rect in enumerate(option_rects):
                    if rect.collidepoint(event.pos):
                        pygame.draw.rect(screen, OPTION_HOVER_COLOR, rect)
                    else:
                        pygame.draw.rect(screen, OPTION_COLOR, rect)

                    # Desenhar texto das opções
                    texto_opcao = font2.render(opcoes[i], True, OPTION_TEXT_COLOR)
                    texto_rect_opcao = texto_opcao.get_rect(center=rect.center)
                    screen.blit(texto_opcao, texto_rect_opcao)

                pygame.display.flip()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    for i, rect in enumerate(option_rects):
                        if rect.collidepoint(mouse_pos):
                            resposta_selecionada = opcoes[i]

    screen.fill(BACKGROUND_COLOR)




    if resposta_selecionada == resposta:
        exibir_mensagem("Resposta correta!", GREEN)
        return 10
    else:
        exibir_mensagem("Resposta incorreta!", RED)
        return 0
    
def exibir_mensagem(mensagem, cor):
    screen.fill(WHITE)
    mensagem_surface = font.render(mensagem, True, cor)
    mensagem_rect = mensagem_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(mensagem_surface, mensagem_rect)
    pygame.display.flip()
    pygame.time.wait(2000)

nome_jogador = exibir_nome_jogador()

 # Exibir pontuação inicial
pontuacao_total = 0
texto_pontuacao = font.render("PONTUAÇÃO: " + str(pontuacao_total), True,RED)
texto_rect_pontuacao = texto_pontuacao.get_rect(center=(WIDTH // 2, 40))

 # Loop principal do jogo

game_over = False
jogadas = 0

 
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    screen.fill(WHITE)

     # Carregar a imagem de fundo
    fundo_path = "imagens/fundo.png"  
    fundo_image = pygame.image.load(fundo_path)
    screen.blit(fundo_image, (0, 40))

    # Desenhar roleta
    moldura_width = 1024
    moldura_height = 80
    moldura_x = (WIDTH - moldura_width) // 2
    moldura_y = (HEIGHT - moldura_height) // 50

    # Desenhar moldura
    pygame.draw.rect(screen, QUESTION_BORDER_COLOR, (moldura_x, moldura_y, moldura_width, moldura_height))
    pygame.draw.rect(screen, QUESTION_COLOR, (moldura_x + 2, moldura_y + 2, moldura_width - 4, moldura_height - 4))
    
    # Desenhar o nome do jogador no canto esquerdo da tela
    texto_nome_jogador = font.render("JOGADOR: " + nome_jogador, True, BLACK)
    texto_rect_nome_jogador = texto_nome_jogador.get_rect(topleft=(50, 38))
    screen.blit(texto_nome_jogador, texto_rect_nome_jogador)

    screen.blit(roleta_image, roleta_rect)

    # Desenhar fase depois do canto esquerdo da tela
    texto_fase = font.render("FASE:" + str(fase), True, BLACK)
    texto_rect_fase = texto_fase.get_rect(center=(WIDTH // 2, 72))
    screen.blit(texto_fase, texto_rect_fase)

    screen.blit(roleta_image, roleta_rect)

    # Desenhar contagem de rodadas

    texto_contar_rodada = font.render("RODADAS: " + str(jogadas) + " de 10", True, BLACK)
    texto_rect_contar_rodada = texto_contar_rodada.get_rect(center=(WIDTH // 1.2, 50))
    screen.blit(texto_contar_rodada, texto_rect_contar_rodada)

    screen.blit(roleta_image, roleta_rect)


    # Desenhar botão de girar
    pygame.draw.circle(screen, BLACK, (WIDTH // 2, HEIGHT // 2), 50)
    texto_girar = font.render("GIRAR", True, WHITE)
    texto_rect = texto_girar.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(texto_girar, texto_rect)

    # Exibir pontuação
    screen.blit(texto_pontuacao, texto_rect_pontuacao)

    pygame.display.flip()

    # Esperar pelo clique do jogador para girar a roleta
    mouse_pos = None
    while mouse_pos is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()

    if game_over:
        break

    # Verificar se o clique foi no botão de girar
    if texto_rect.collidepoint(mouse_pos):
        jogadas += 1
        pontuacao_rodada = girar_roleta()
        pontuacao_total += pontuacao_rodada
        texto_pontuacao = font.render("PONTUAÇÃO: " + str(pontuacao_total), True,RED)

        if jogadas >= 10:
            game_over = True

def salvar_pontuacao(nome_jogador, pontuacao_total):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, "Pontuação do Jogo", ln=True, align="C")

    pdf.cell(0, 10, f"Nome do jogador: {nome_jogador}", ln=True)
    pdf.cell(0, 10, f"Pontuação: {pontuacao_total}", ln=True)

    
    root = tk.Tk()
    root.withdraw()

    # Abrir caixa de diálogo de seleção de arquivo
    file_path = filedialog.asksaveasfilename(defaultextension=".pdf")


    if file_path:
        pdf.output(file_path)
        print(f"A pontuação da jogada foi salva em '{file_path}'.")
    else:
        print("Nenhum arquivo selecionado.")
# Verificar pontuação final e exibir mensagem de parabéns
if pontuacao_total >= 70:
   
   exibir_mensagem("Parabéns! Você passou pra fase 2 e fez" + str(pontuacao_total) + "  pontos!", GREEN)
   pygame.display.flip()  # Atualize a tela para mostrar a mensagem
   pygame.time.delay(5000)  # Aguarde 5 segundos (5000 milissegundos)

   import lib_func_fases2
   lib_func_fases2.exibir_nome_jogador() 
   
else:
    exibir_mensagem("Continue estudando! Você fez " + str(pontuacao_total) + " pontos.", RED)
    pygame.time.delay(2000)  # Aguarde 2 segundos (2000 milissegundos)
    

mensagem_salvar = font.render("Para concluir e sair do jogo, é obrigatório assinar e salvar.", True, BLACK)
mensagem_rect_salvar = mensagem_salvar.get_rect(center=(WIDTH // 2, HEIGHT // 2))
screen.blit(mensagem_salvar, mensagem_rect_salvar)
pygame.display.flip()
pygame.time.wait(2000)



 # Exemplo de uso
salvar_pontuacao(nome_jogador, pontuacao_total,)

pygame.time.delay(3000)  # Aguarde 3 segundos (3000 milissegundos)
create_buttons()

 # Exibir pontuação final
screen.fill(WHITE)
texto_pontuacao_final = font.render("Pontuação total:  " + str(pontuacao_total), True, BLACK)
texto_rect_pontuacao_final = texto_pontuacao_final.get_rect(center=(WIDTH // 2, HEIGHT // 2))
screen.blit(texto_pontuacao_final, texto_rect_pontuacao_final)
pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()