import pygame
import random
import time
import tkinter as tk
from tkinter import filedialog
from fpdf import FPDF
import libperg


#---------------------------------TELA---------------------------------#



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

fontname = "futura bold"
    # Fonte para as perguntas e opções
font = pygame.font.SysFont(fontname, 30)

font2 = pygame.font.SysFont(fontname, 22)

nome_jogador = ""
  

 #-----------------------------NOME JOGADOR---------------------------------#

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

#-----------------------------VARIAVEL DA FUNÇÃO NOME JOGADOR---------------------------------#
nome_jogador = exibir_nome_jogador()
print("Nome do jogador:", nome_jogador)


#-----------------------------FUNÇÃO EXIBIR RESULTADO---------------------------------#

def exibir_resultado(pontuacao):
 screen.fill(WHITE)

    # Mensagem de resultado
 mensagem = f"Parabéns, {nome_jogador}! Sua pontuação foi: {pontuacao}"
 texto_mensagem = font.render(mensagem, True, BLACK)
 texto_rect_mensagem = texto_mensagem.get_rect(center=(WIDTH // 2, HEIGHT // 2))
 screen.blit(texto_mensagem, texto_rect_mensagem)
 
pygame.display.flip()  

#-----------------------------VARIAVEIS---------------------------------#
pontuacao = 0
resposta_selecionada = None
jogando = True

#-----------------------------FUNÇÃO GIRAR A ROLETA---------------------------------#

def girar_roleta():
    angulo = 0
    velocidade = random.randint(20, 30)
    tempo_girar = random.randint(2, 12)
    tempo_parar = random.randint(2, 3)
    parar_angulo = random.randint(0, 359)

    start_time = time.time()

    pygame.mixer.music.load("som/roulette-game-sound-effect-2301.wav")
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

    #-----------------------------FUNÇÃO EXIBIR PERGUNTA ALEATORIA---------------------------------#

def exibir_pergunta_aleatoria():


    rodadas = 10

    for _ in range(rodadas):
    # Verifica se todas as perguntas já foram usadas
     if not libperg.perguntas:
        print("Todas as perguntas foram usadas!")
        break

    pergunta = random.choice(libperg.perguntas)
    libperg.perguntas.remove(pergunta)
    return exibir_pergunta(pergunta["pergunta"], pergunta["opcoes"], pergunta["resposta"], pergunta["imagem"])

#-----------------------------CORES PARA TELA PERGUNTA---------------------------------#

# Defina as cores
BACKGROUND_COLOR = (240, 240, 240)  # Cor de fundo geral
QUESTION_COLOR = (220, 220, 220)  # Cor de fundo da pergunta
QUESTION_BORDER_COLOR = (230, 230, 230)  # Cor do contorno da pergunta
OPTION_COLOR = (200, 200, 200)  # Cor de fundo das opções de resposta
OPTION_HOVER_COLOR = (180, 180, 180)  # Cor de fundo das opções de resposta quando o mouse estiver sobre elas
OPTION_TEXT_COLOR = (0, 0, 0)  # Cor do texto das opções de resposta


#-----------------------------FUNÇÃO PRA EXIBIR PERGUNTA---------------------------------#

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
    option_width = 600 
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
        
#-----------------------------FUNÇÃO PRA EXIBIR MENSAGEM---------------------------------#
     
def exibir_mensagem(mensagem, cor):
    screen.fill(WHITE)
    mensagem_surface = font.render(mensagem, True, cor)
    mensagem_rect = mensagem_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(mensagem_surface, mensagem_rect)
    pygame.display.flip()
    pygame.time.wait(2000)
#-----------------------------VARIAVEIS JOGADOR E PONTUAÇÃO---------------------------------#

nome_jogador = exibir_nome_jogador()

 # Exibir pontuação inicial
pontuacao_total = 0
texto_pontuacao = font.render("PONTUAÇÃO: " + str(pontuacao_total), True, RED)
texto_rect_pontuacao = texto_pontuacao.get_rect(center=(WIDTH // 2, 50))


#-----------------------------Loop principal do jogo---------------------------------#
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
#-----------------------------FUNÇÃO EXIBIR  ANIMAÇÃO FOGUETES---------------------------------#

def exibir_animacao_foguetes():
        # Definir as imagens dos foguetes
        foguete1 = pygame.image.load("imagens/foguete1.png")
        foguete2 = pygame.image.load("imagens/foguete2.png")
        foguete3 = pygame.image.load("imagens/foguete3.png")

        # Posições iniciais dos foguetes
        posicao_foguete1 = [100, HEIGHT]
        posicao_foguete2 = [WIDTH // 2, HEIGHT]
        posicao_foguete3 = [WIDTH - 100, HEIGHT]

        # Velocidades dos foguetes
        velocidade_foguete1 = 5
        velocidade_foguete2 = 6
        velocidade_foguete3 = 7

        # Loop principal da animação
        animacao_foguetes = True
        while animacao_foguetes:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

        screen.fill(BLACK)

            # Movimento dos foguetes
        posicao_foguete1[1] -= velocidade_foguete1
        posicao_foguete2[1] -= velocidade_foguete2
        posicao_foguete3[1] -= velocidade_foguete3

            # Exibição dos foguetes
        screen.blit(foguete1, posicao_foguete1)
        screen.blit(foguete2, posicao_foguete2)
        screen.blit(foguete3, posicao_foguete3)

        pygame.display.flip()
        pygame.time.Clock().tick(60)

            # Verificar se os foguetes chegaram ao topo da tela
        if posicao_foguete1[1] <= -foguete1.get_height() or posicao_foguete2[1] <= -foguete2.get_height() or posicao_foguete3[1] <= -foguete3.get_height():
                animacao_foguetes = False

#-----------------------------VERIFICAR PONTUAÇÃO E MOSTRAR MENSAGEM---------------------------------#

# Verificar pontuação final e exibir mensagem de parabéns
if pontuacao_total >= 70:
    exibir_mensagem("Parabéns! Você jogou " + str(jogadas) +" "+ nome_jogador + "e fez" + str(pontuacao_total) + " pontos!", GREEN)

# Exibir animação de foguetes se acertou todas as perguntas
if pontuacao_total == 100:

    # Definir a função para exibir a animação de foguetes
    exibir_mensagem("Parabéns! Você acertou todas as perguntas e fez   " + str(pontuacao_total) + "  pontos!", GREEN)

    # Chamar a função para exibir a animação de foguetes
    exibir_animacao_foguetes()

if pontuacao_total < 50:
    exibir_mensagem("Continue estudando! Sua pontuação foi " + str(pontuacao_total) + " pontos.", RED)
elif pontuacao_total >= 50:
      exibir_mensagem("Parabéns! Você fez " + str(pontuacao_total) + " pontos!", GREEN)
else:
    exibir_mensagem("Parabéns! Sua pontuação foi  " + str(pontuacao_total) + "  pontos.", GREEN)

#-----------------------------MENSAGEM ALERTA DE SALVAR PONTUAÇÃO DO JOGO---------------------------------#
mensagem_salvar = font.render("Para concluir o jogo, é obrigatório assinar e salvar.", True, BLACK)
mensagem_rect_salvar = mensagem_salvar.get_rect(center=(WIDTH // 2, HEIGHT // 2))
screen.blit(mensagem_salvar, mensagem_rect_salvar)
pygame.display.flip()
pygame.time.wait(2000)

#---------------------------------FUNÇÃO SALVAR PONTUAÇÃO--------------------------------------#

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


#-------------------------------PONTUAÇÃO FINAL----------------------------------------#
 # Exibir pontuação final

salvar_pontuacao(nome_jogador, pontuacao_total,)

screen.fill(WHITE)
texto_pontuacao_final = font.render("Pontuação total:  " + str(pontuacao_total), True, BLACK)
texto_rect_pontuacao_final = texto_pontuacao_final.get_rect(center=(WIDTH // 2, HEIGHT // 2))
screen.blit(texto_pontuacao_final, texto_rect_pontuacao_final)
pygame.display.flip()

#--------------------------------FINALIZANDO O JOGO---------------------------------------#

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()