import tkinter as tk
from tkinter import filedialog
from fpdf import FPDF
import libperg
import lib_func2



# Função para inserir e exibir nome do jogador
lib_func2.exibir_nome_jogador()

# Função para exibir resultado
lib_func2.exibir_resultado()


# Função para girar a roleta
lib_func2.girar_roleta()

# Função para exibir uma pergunta aleatória
lib_func2.exibir_pergunta_aleatoria()


# Função para exibir uma pergunta 
lib_func2.exibir_pergunta("pergunta", "opcoes", "resposta", "imagem")


# Função para exibir uma mensagem na tela
lib_func2.exibir_mensagem("mensagem","cor")

# Função para salvar pontuação
lib_func2.salvar_pontuacao("nome_jogador", "pontuacao_total")


