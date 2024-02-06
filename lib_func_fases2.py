import sys
import pygame
import random
import time
import tkinter as tk
from tkinter import filedialog
from fpdf import FPDF


perguntas = [
      
         {
            "pergunta": "Quanto a posição e dimensões do rim?",
            "opcoes": ["O direito é mais superior do que o esquerdo",
                       "Posicionado na região anteperitoneal",
                       "Localizado á direita e esquerda da coluna vertebral",
                       "Possui uma glândula no polo inferior"
                       "Suas dimensões aproximadas são: 30cm C – 10cm L – 5,5cm E"],
            "resposta": "Localizado á direita e esquerda da coluna vertebral",
            "imagem": "df"
        },
        {
            "pergunta": "Qual o nome da unidade funcional do rim?",
            "opcoes": ["Nefrite",
                       "Glóbulos",
                       "Epidídimo",
                       "Néfrons",
                       "Pleura" ],
            "resposta": "Néfrons",
            "imagem": "df2"
        },
         {
            "pergunta": "Quais estruturas passam pelo Hilo renal?",
            "opcoes": ["Ureter e artéria renal",
                       "Ureter, artéria renal, veia renal, nervos e vasos linfáticos",
                       "Nervos e vasos linfáticos",
                       "Artéria renal, veia renal",
                       "Uretra" ],
            "resposta": "Ureter, artéria renal, veia renal, nervos e vasos linfáticos",
            "imagem": "df2"
        },
         {
            "pergunta": "Qual o nome da estrutura que transporta urina da pelve renal até a bexiga?",
            "opcoes": ["Uretra", "Ureter", "Néfrons","Cálice Maior", "Papila renal" ],
            "resposta": "Ureter",
            "imagem": "df5"
        },
         {
            "pergunta": "Quais as três porções do ureter?",
            "opcoes": ["Abdominal, Pélvica e Intramural", "Pélvica, Intreposta e adjacente", "Abdominal, Torácica e lombar","Cervical, iguinal e umbilical", "Curva, reta e linear" ],
            "resposta": "Abdominal, Pélvica e Intramural",
            "imagem": "df5"
        },
         {
            "pergunta": "A parede do ureter consiste em três camadas. São elas:",
            "opcoes": ["Túnicas interna, vastigial e conjuntivas", "Túnica mucosa, Músculo liso e Tecido conjuntivo", "Endotélio, Epitélio e Miotélio","Túnica vastigial, Túnica muscular e Túnica Lisa", "Endotélio, Endocárdio e Peritônio" ],
            "resposta": "Túnica mucosa, Músculo liso e Tecido conjuntivo",
            "imagem": "df5"
        },
         {
            "pergunta": "Qual a função das artérias arqueadas?",
            "opcoes": ["Irrigar o córtex renal",
                       "Irrigar a medula renal",
                       "Irrigar a pelve renal",
                       "Irrigar as colunas renais",
                       "Drenar as pirâmides renais" ],
            "resposta": "Irrigar o córtex renal",
            "imagem": "df3"
        },
         {
            "pergunta": "Quais as três porções internas dos rins?",
            "opcoes": ["Pirâmides renais, corpúsculo renal e Pelve renal",
                       "Medula renal, córtex renal e coluna renal",
                       "Cápsula fibrosa, ureter e hilo renal",
                       "Coroa radiada, Cálice menor e medula renal",
                       "Uretra, Néfrons e Cálice maior" ],
            "resposta": "Medula renal, córtex renal e coluna renal",
            "imagem": "df4"
        },
         {
            "pergunta": "São funções fisiológicas dos rins, exceto:",
            "opcoes": ["Regulação da composição iônica do sangue ",
                       "Manutenção da osmolaridade do sangue",
                       "Regulação do volume sanguíneo",
                       "Regulação da pressão arterial",
                       "Liberação de anticorpos no sangue" ],
            "resposta": "Liberação de anticorpos no sangue",
            "imagem": "df4"
        },
         {
            "pergunta": "São componentes do Sistema de tubos de captação da urina?",
            "opcoes": ["Cálice maior, Ureter e Pelve renal",
                       "Papila renal (da pirâmide) e Cálice meno",
                       "Papila renal, Cálice menor, Cálice maior, Pelve renal e Ureter",
                       "Uretra e Ureter",
                       "Bexiga e uretra" ],
            "resposta": "Papila renal, Cálice menor, Cálice maior, Pelve renal e Ureter",
            "imagem": "df4"
        },
         {
            "pergunta": "Quais estruturas formam a pelve renal?",
            "opcoes": ["Cálice menor e Cálice maior",
                       "Seio renal e papila renal",
                       "Radiações medulares e coluna de Bertin",
                       "Parênquima renal",
                       "Células caliciformes" ],
            "resposta": "Cálice menor e Cálice maior",
            "imagem": "df4"
        },
         {
            "pergunta": "A parede do ureter consiste em três camadas. São elas:",
            "opcoes": ["Túnicas interna, vastigial e conjuntivas",
                       "Túnica mucosa, Músculo liso e Tecido conjuntivo",
                       "Endotélio, Epitélio e Miotélio",
                       "Túnica vastigial, Túnica muscular e Túnica Lisa",
                       "Endotélio, Endocárdio e Peritônio" ],
            "resposta": "Túnica mucosa, Músculo liso e Tecido conjuntivo",
            "imagem": "df5"
        },
         {
            "pergunta": "Quais as características e funções da bexiga urinária?",
            "opcoes": ["Órgão de reservatório e excreção de plasma",
                       "Órgão sacular oco de armazenamento e excreção da urina.",
                       "Órgão de produção e excreção de urina",
                       "Órgão de liberação de hormônios",
                       "Órgão de trocas gasosas" ],
            "resposta": "Órgão sacular oco de armazenamento e excreção da urina.",
            "imagem": "df6"
        },
        {
            "pergunta": "São porções da uretra masculina, exceto?",
            "opcoes": ["Uretra prostática atravessando a próstata",
                       "Uretra membranácea atravessando o assoalho pélvico",
                       "Uretra esponjosa envolvida pelo corpo esponjoso do pênis",
                       "Uretra Adjacente, atravessando a pelve renal",
                       "Prostática, membranácea e esponjosa" ],
            "resposta": "Uretra Adjacente, atravessando a pelve renal",
            "imagem": "df7"
        },
        {
            "pergunta": "A uretra masculina é responsável por transportar?",
            "opcoes": ["Sêmem e urina",
                       "Sêmem",
                       "Urina",
                       "Plasma e sêmem",
                       "Urina e sangue" ],
            "resposta": "Sêmem e urina",
            "imagem": "df7"
        },
        {
            "pergunta": "São características da uretra feminina, exceto?",
            "opcoes": ["Tem cerca de 4 cm de extensão e 8 mm de diâmetro",
                       "Ligeiramente  curva",
                       "Esfíncter uretral interno é o mais importante na continência urinária",
                       "Possui inervação somente somática",
                       "Está mais propícia a riscos de infecção" ],
            "resposta": "Possui inervação somente somática",
            "imagem": "df8"
        },
        {
            "pergunta": "São sintomas da inflamação da uretra feminina, exceto?",
            "opcoes": ["Corrimento claro e esbranquiçado na região íntima",
                       "Queimação e ardência ao urinar",
                       "Coceira no órgão genital e nas demais regiões",
                       "Edema",
                       "Dor no saco escrotal" ],
            "resposta": "Dor no saco escrotal",
            "imagem": "df8"
        },
        {
            "pergunta": "Qual região anatômica e vascularizada pela artéria mesentérica?",
            "opcoes": ["Membro inferior",
                       "Baço",
                       "Membro superior",
                       "Encéfalo e pescoço",
                       "Intestino" ],
            "resposta": "Intestino",
            "imagem": "df25"
        },
        {
            "pergunta": "Qual é a ordem correta da geração e condução de um estímulo cardíaco?",
            "opcoes": ["Nodo sinusal, nodo atrioventricular, feixe de His e fibras de Purkinje",
                       "Nó sinusal,vias internodais,nodo atrioventricular,feixe de His e fibras de Purkinje",
                       "Feixe de His, fibras de Purkinje, vias internodais, nodo atrioventricular",
                       "Nodo atrioventricular, feixe de His e fibras de Purkinje",
                       "Nodo atrioventricular, nodo sinusal, vias internodais, feixe de His" ],
            "resposta": "Nó sinusal,vias internodais,nodo atrioventricular,feixe de His e fibras de Purkinje",
            "imagem": "df26"
        },
        {
            "pergunta": "Qual é a definição do ciclo cardíaco?",
            "opcoes": ["Início de um batimento cardíaco até o final do mesmo batimento cardíaco",
                       "Fim de um batimento cardíaco até o início do batimento cardíaco seguinte",
                       "Fim de um batimento cardíaco até o fim do batimento cardíaco seguinte",
                       "Início de um batimento cardíaco até a metade do mesmo batimento",
                       "Início de um batimento cardíaco até o início do batimento cardíaco seguinte" ],
            "resposta": "Início de um batimento cardíaco até o início do batimento cardíaco seguinte",
            "imagem": "df26"
        },
        {
            "pergunta": "Quais são os fatores endógenos que podem causar a hipertensão arterial?",
            "opcoes": ["Hereditariedade, idade, raça e obesidade",
                       "Tabagismo, sedentarismos, bebida alcóolica e raça",
                       "Hereditariedade, raça, obesidade e alcoolismo",
                       "Tabagismo, excesso de sal, estresse e idade",
                       "Hereditariedade, sedentarismo, tabagismo e idade" ],
            "resposta": "Hereditariedade, idade, raça e obesidade",
            "imagem": "df27"
        },
        {
            "pergunta": "Qual é o valor considerado como uma pressão arterial normal?",
            "opcoes": ["115 mmHg pressão sistólica e 95 mmHg pressão diastólica",
                       "120 mmHg pressão sistólica e 75 mmHg pressão diastólica",
                       "110 mmHg pressão sistólica e 95 mmHg pressão diastólica",
                       "130 mmHg pressão sistólica e 85 mmHg pressão diastólica",
                       "125 mmHg pressão sistólica e 75 mmHg pressão diastólica" ],
            "resposta": "130 mmHg pressão sistólica e 85 mmHg pressão diastólica",
            "imagem": "df27"
        },
        {
            "pergunta": "Para controlar o nível de glicose sanguínea o pâncreas secreta quais hormônios:",
            "opcoes": ["glucagon e hormônio do crescimento",
                       "glucagon e insulina",
                       "somatostatina e prolactina",
                       "somatostatina e tiroxina",
                       "insulina e tiroxina" ],
            "resposta": "glucagon e insulina",
            "imagem": "df28"
        },
        {
            "pergunta": "Quais são os pacientes que a síndrome pós-pólio atinge e o que ele provoca?",
            "opcoes": ["Pacientes com paralisia infantil/febre alta e dor no pescoço",
                       "Pacientes com paralisia infantil/crises convulsivas e fadiga intensa",
                       "Pacientes com doença de Alzheimer/provoca fraqueza muscular e fadiga",
                       "Pacientes com doença de Alzheimer/cefaleias e alterações na visão",
                       "Pacientes com paralisia infantil/provoca fraqueza muscular e fadiga" ],
            "resposta": "Pacientes com paralisia infantil/provoca fraqueza muscular e fadiga",
            "imagem": "df29"
        }, 
        {
            "pergunta": "Os espermatozóides são somados a líquidos que são produzidos por:",
            "opcoes": ["glândulas seminais, próstata e glândulas bulbouretrais",
                       "glândulas bulbouretrais, próstata e testículo",
                       "glândulas seminais, túbulos seminíferos e próstata ",
                       "glândulas bulbouretrais, testículo e bexiga",
                       "glândulas seminais, testículo e glândulas bulbouretrais" ],
            "resposta": "glândulas seminais, próstata e glândulas bulbouretrais",
            "imagem": "df30"
        }, 
        {
            "pergunta": "A testosterona é produzida pelas células do testículo chamadas de:",
            "opcoes": ["células mãe",
                       "células espermátides",
                       "células de Sertoli ",
                       "células de Leydig ",
                       "células espermatogônias" ],
            "resposta": "células de Leydig ",
            "imagem": "df31"
        }, 
        {
            "pergunta": "O processo de formação dos espermatozoides é divido em quais fases:",
            "opcoes": ["separação, divisão e duplicação",
                       "meiose e mitose",
                       "reprodução e maturação",
                       "Germinativa, crescimento, maturação e diferenciação",
                       "mitose e meiose" ],
            "resposta": "Germinativa, crescimento, maturação e diferenciação",
            "imagem": "df32"
        }, 
        {
            "pergunta": "Qual estrutura do sistema genital feminino recolhe o ovócito após ser liberado?",
            "opcoes": ["Miométrio",
                       "Endométrio",
                       "Cílios da tuba uterina",
                       "Fímbrias",
                       "Folículos ovarianos " ],
            "resposta": "Fímbrias",
            "imagem": "df33"
        }, 
        {
            "pergunta": "Qual o nome do envoltório de células externas do ovário?",
            "opcoes": ["grânulos corticais",
                       "acrossomo",
                       "células foliculares",
                       "zona pelúcida",
                       "corona radiata" ],
            "resposta": "corona radiata",
            "imagem": "df33"
        }, 
        {
            "pergunta": "Qual é a função do surfactante pulmonar?",
            "opcoes": ["Aumentar a tensão superficial do líquido que reveste os alvéolos",
                       "Não se sabe ainda qual é a sua função",
                       "Impedir que as pleuras entrem em atrito",
                       "Reduzir a tensão superficial do líquido que reveste os alvéolos",
                       "Auxiliar no movimento inspiratório e expiratório" ],
            "resposta": "Reduzir a tensão superficial do líquido que reveste os alvéolos",
            "imagem": "df34"
        }, 
        {
            "pergunta": "O pulmão trabalha com volumes e capacidades respiratórias. O que é volume corrente?",
            "opcoes": ["É a quantidade de ar que normalmente entra ou sai do pulmão em cada respiração",
                       "É a quantidade de ar que entra no pulmão, mas não participa das trocas gasosas",
                       "É a quantidade de ar expirado após o esforço respiratório máximo",
                       "Quantidade que pode ser movida para dentro e para fora dos pulmões em um minuto",
                       "É a quantidade de ar que ainda permanece nos pulmões após uma expiração forçada" ],
            "resposta": "É a quantidade de ar que normalmente entra ou sai do pulmão em cada respiração",
            "imagem": "df34"
        }, 
        {
            "pergunta": "Qual é a definição de asma?",
            "opcoes": ["É um acúmulo anormal de líquido nos tecidos dos pulmões",
                       "É uma obstrução das artérias pulmonares por coágulos (trombos ou êmbolos)",
                       "É definida como uma infecção ou inflamação aguda dos alvéolos",
                       "É uma inflamação crônica por hipersensibilidade a estímulos como pólen e ácaros",
                       "É definida como a inflamação das mucosas dos seios da face" ],
            "resposta": "É uma inflamação crônica por hipersensibilidade a estímulos como pólen e ácaros",
            "imagem": "df35"
        }, 
        {
            "pergunta": "Quais são os brônquios lobares originados pelo brônquio principal esquerdo?",
            "opcoes": ["Brônquios lobares superior, médio e inferior",
                       "Brônquios lobares superior e inferior",
                       "Brônquios lobares posterior, médio e inferior",
                       "Brônquios lobares posterior e inferior",
                       "Brônquios lobares médio e inferior" ],
            "resposta": "Brônquios lobares superior e inferior",
            "imagem": "df35"
        },  
]
   # Definição das cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (200, 200, 200)
CIANO_CLARO = (224,255,255)
OURO = (255,215,0)
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
fase = 2

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
    import lib_func_fases2

def exibir_nome_jogador():
    global nome_jogador

    screen.fill(WHITE)

    campo_nome = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 25, 200, 50)
    pygame.draw.rect(screen, BLACK, campo_nome, 2)

    mensagem = font.render("Insira seu nome para iniciar o jogo na fase 2", True, BLACK)
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

        screen.fill(OURO)
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

    screen.fill(CIANO_CLARO)

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
   exibir_mensagem("Parabéns! Você passou pra fase 3 e fez" + str(pontuacao_total) + "  pontos!", GREEN)
   pygame.display.flip()  # Atualize a tela para mostrar a mensagem
   pygame.time.delay(4000)  # Aguarde 4 segundos (4000 milissegundos)

   import lib_func_fases3
   lib_func_fases3.exibir_nome_jogador() 
   
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