import tkinter as tk
from tkinter import filedialog
from fpdf import FPDF
import libperg
import lib_func

# Função para inserir e exibir nome do jogador
lib_func.exibir_nome_jogador()

# Função para exibir resultado
lib_func.exibir_resultado()


# Função para girar a roleta
lib_func.girar_roleta()

# Função para exibir uma pergunta aleatória
lib_func.exibir_pergunta_aleatoria()


# Função para exibir uma pergunta 
lib_func.exibir_pergunta("pergunta", "opcoes", "resposta", "imagem")


# Função para exibir uma mensagem na tela
lib_func.exibir_mensagem("mensagem","cor")

# Função para salvar pontuação
lib_func.salvar_pontuacao("nome_jogador", "pontuacao_total")


