from tkinter import *
import customtkinter
from ..control.main import Projeto

# Define global variables to store the windows
janela = None
janela2 = None
janela3 = None
janela4 = None

def abrir_janela1():
    global janela
    global janela2
    global janela3
    global janela4

    if janela2:
        janela2.withdraw()

    janela = customtkinter.CTk()
    janela.title("Splitwise")
    janela.geometry("500x700")
    janela.maxsize(width=500, height=700)

    #MARGEM TOP
    margem_cima = customtkinter.CTkLabel(janela, text="")
    margem_cima.pack(pady=50, side=TOP)

    # LABEL GRUPO
    grupo = customtkinter.CTkLabel(janela, text="Adicione Pessoas ao seu grupo !", font=("Arial",16, "bold"))
    grupo.pack(padx=10, pady=3)

    #MARGEM 
    margem = customtkinter.CTkLabel(janela, text="")
    margem.pack(pady=5, side=TOP)

    # LABEL GRUPO
    nome = customtkinter.CTkLabel(janela, text="Nome:                  ", font=("Arial",16, "bold"))
    nome.pack(padx=10, pady=3)

    # ENTRY NOME
    entry = customtkinter.CTkEntry(janela)
    entry.pack(padx=10, pady=3)
    entry.configure(fg_color="#3d3d3d")

    # BOTÃO INSERIR
    def inserir_nome():
        nome_inserido = entry.get()
        Projeto.new_user(self=projeto, user=nome_inserido)
        entry.delete(0, END)

    botao = customtkinter.CTkButton(janela, text="Inserir", command=inserir_nome)
    botao.pack(padx=10, pady=10)
    botao.configure(corner_radius=10, font=("Arial",15, "bold"))

    #MARGEM
    margem2 = customtkinter.CTkLabel(janela, text="")
    margem2.pack(pady=30, side=TOP)

    # LABEL CONCLUIR
    nome = customtkinter.CTkLabel(janela, text="Não quer inserir mais ninguém?", font=("Arial",16, "bold"))
    nome.pack(padx=10, pady=3)

    # Button to open janela2
    botao2 = customtkinter.CTkButton(janela, text="Concluir", command=abrir_janela2)
    botao2.pack(padx=10, pady=10)
    botao2.configure(corner_radius=10, font=("Arial",15, "bold"))

    janela.mainloop()

def abrir_janela2():
    global janela
    global janela2
    global janela3
    global janela4

    if janela:
        janela.withdraw()
    
    if janela3:
        janela3.withdraw()

    if janela4:
        janela4.withdraw()

    janela2 = customtkinter.CTk()
    janela2.title("Splitwise")
    janela2.geometry("500x700")
    janela2.maxsize(width=500, height=700)

    # Button to go back to janela1
    botao2 = customtkinter.CTkButton(janela2, text="Voltar", command=abrir_janela1)
    botao2.place(x=20, y=20)
    botao2.configure(corner_radius=10, font=("Arial",15, "bold"))

    #MARGEM TOP
    margem_cima = customtkinter.CTkLabel(janela2, text="")
    margem_cima.pack(pady=30, side=TOP)

    # LABEL TESTE
    teste = customtkinter.CTkLabel(janela2, text="Grupo :", font=("Arial",16, "bold"))
    teste.pack(padx=10, pady=3)

    #LABEL NOMES
    Projeto.realizar_calculo(self=projeto)
    transactions_string = Projeto.get_transactions_string(self=projeto)

    nomes = customtkinter.CTkLabel(janela2, text=transactions_string)
    nomes.pack(pady=20, side=TOP)
    nomes.configure(font=("Arial",16, "bold"))

    # Button to go back to janela1
    botao3 = customtkinter.CTkButton(janela2, text="Nova Conta", command=abrir_janela3)
    botao3.pack(padx=70, pady=5, side=LEFT)
    botao3.configure(corner_radius=10, font=("Arial",15, "bold"))

    # Button to go back to janela1
    botao4 = customtkinter.CTkButton(janela2, text="Pagar Conta", command=abrir_janela4)
    botao4.pack(padx=10, pady=5, side=LEFT)
    botao4.configure(corner_radius=10, font=("Arial",15, "bold"))

    janela2.mainloop()

def abrir_janela3():

    global janela
    global janela2
    global janela3
    global janela4

    if janela2:
        janela2.withdraw()

    janela3 = customtkinter.CTk()
    janela3.title("Splitwise")
    janela3.geometry("500x700")
    janela3.maxsize(width=500, height=700)

    # Button to go back to janela2
    botao4 = customtkinter.CTkButton(janela3, text="Voltar", command=abrir_janela2)
    botao4.place(x=20, y=20)
    botao4.configure(corner_radius=10, font=("Arial",15, "bold"))

    #MARGEM TOP
    margem_cima = customtkinter.CTkLabel(janela3, text="")
    margem_cima.pack(pady=50, side=TOP)

    # LABEL PAGADOR
    nome_pagador = customtkinter.CTkLabel(janela3, text="Nome do Pagador:", font=("Arial",16, "bold"))
    nome_pagador.pack(padx=10, pady=3)

    # ENTRY PAGADOR
    entry2 = customtkinter.CTkEntry(janela3)
    entry2.pack(padx=10, pady=0)
    entry2.configure(fg_color="#3d3d3d")

    # LABEL PREÇO
    preco = customtkinter.CTkLabel(janela3, text="Valor da Conta:     ", font=("Arial",16, "bold"))
    preco.pack(padx=10, pady=3)

    # ENTRY PREÇO
    entry3 = customtkinter.CTkEntry(janela3)
    entry3.pack(padx=10, pady=0)
    entry3.configure(fg_color="#3d3d3d")

    #MARGEM
    margem2 = customtkinter.CTkLabel(janela3, text="")
    margem2.pack(pady=20, side=TOP)

    # BOTÃO ADICIONAR CONTA
    botao5 = customtkinter.CTkButton(janela3, text="Adicionar Conta")
    botao5.pack(padx=10, pady=10)
    botao5.configure(corner_radius=10, font=("Arial",15, "bold"))

    janela3.mainloop()

def abrir_janela4():

    global janela
    global janela2
    global janela3
    global janela4

    if janela2:
        janela2.withdraw()

    janela4 = customtkinter.CTk()
    janela4.title("Splitwise")
    janela4.geometry("500x700")
    janela4.maxsize(width=500, height=700)

    # Button to go back to janela2
    botao6 = customtkinter.CTkButton(janela4, text="Voltar", command=abrir_janela2)
    botao6.place(x=20, y=20)
    botao6.configure(corner_radius=10, font=("Arial",15, "bold"))

    #MARGEM TOP
    margem_cima = customtkinter.CTkLabel(janela4, text="")
    margem_cima.pack(pady=50, side=TOP)

    # LABEL PAGADOR
    nome_pagador2 = customtkinter.CTkLabel(janela4, text="Nome do Pagador:", font=("Arial",16, "bold"))
    nome_pagador2.pack(padx=10, pady=3)

    # ENTRY PAGADOR
    entry4 = customtkinter.CTkEntry(janela4)
    entry4.pack(padx=10, pady=0)
    entry4.configure(fg_color="#3d3d3d")

    # LABEL BENEFICIADO
    nome_beneficiado = customtkinter.CTkLabel(janela4, text="Nome do Beneficiado:", font=("Arial",16, "bold"))
    nome_beneficiado.pack(padx=10, pady=3)

    # ENTRY PREÇO
    entry5 = customtkinter.CTkEntry(janela4)
    entry5.pack(padx=10, pady=0)
    entry5.configure(fg_color="#3d3d3d")

    #MARGEM
    margem2 = customtkinter.CTkLabel(janela4, text="")
    margem2.pack(pady=20, side=TOP)

    # BOTÃO ADICIONAR CONTA
    botao7 = customtkinter.CTkButton(janela4, text="Pagar Divida")
    botao7.pack(padx=10, pady=10)
    botao7.configure(corner_radius=10, font=("Arial",15, "bold"))

    janela4.mainloop()

# Run the initial window (janela1)
users = [{'Gabriel': 5}, {'Felipe': 10}, {'Davi': 5}, {'Jonathan': 7}, {'Gabriel P': 10}, {'Matheus': 20}]

projeto = Projeto(users)

abrir_janela1()