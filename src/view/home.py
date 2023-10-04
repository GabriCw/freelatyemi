from tkinter import *
import customtkinter

# Define global variables to store the windows
janela = None
janela2 = None

def abrir_janela1():
    global janela
    global janela2

    if janela2:
        janela2.destroy()

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
    botao = customtkinter.CTkButton(janela, text="Inserir")
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

    if janela:
        janela.destroy()

    janela2 = customtkinter.CTk()
    janela2.title("Splitwise")
    janela2.geometry("500x700")
    janela2.maxsize(width=500, height=700)

    # Button to go back to janela1
    botao2 = customtkinter.CTkButton(janela2, text="Voltar", command=lambda: abrir_janela1())
    botao2.place(x=20, y=20)
    botao2.configure(corner_radius=10, font=("Arial",15, "bold"))

    #MARGEM TOP
    margem_cima = customtkinter.CTkLabel(janela2, text="")
    margem_cima.pack(pady=30, side=TOP)

    # LABEL TESTE
    teste = customtkinter.CTkLabel(janela2, text="Grupo :", font=("Arial",16, "bold"))
    teste.pack(padx=10, pady=3)

    #MARGEM
    margem = customtkinter.CTkLabel(janela2, text="")
    margem.pack(pady=20, side=TOP)

    # Button to go back to janela1
    botao3 = customtkinter.CTkButton(janela2, text="Nova Conta")
    botao3.pack(padx=70, pady=5, side=LEFT)
    botao3.configure(corner_radius=10, font=("Arial",15, "bold"))

    # Button to go back to janela1
    botao4 = customtkinter.CTkButton(janela2, text="Pagar Conta")
    botao4.pack(padx=10, pady=5, side=LEFT)
    botao4.configure(corner_radius=10, font=("Arial",15, "bold"))

    janela2.mainloop()

# Run the initial window (janela1)
abrir_janela1()