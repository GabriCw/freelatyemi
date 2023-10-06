from tkinter import *
import customtkinter
from ..controller.controller import Controller
from ..model.model import Model
from PIL import Image, ImageTk 
import tempfile
import os


class View():
    
    def __init__(self, model, controller) -> None:
        self.model = model
        self.controller = controller
        self.janela = None
        self.janela2 = None
        self.janela3 = None
        self.janela4 = None
        self.imagem = None
        self.abrir_janela1()

    def carregar_imagem(self):
        # Carregue a imagem
        imagem = Image.open('src/assets/Logo.jpg')

        # Redimensione a imagem
        largura = 441  # Defina a largura desejada
        altura = 140  # Defina a altura desejada
        imagem = imagem.resize((largura, altura))
        
        # Crie o objeto PhotoImages
        imagem = ImageTk.PhotoImage(imagem)

        return imagem

    def abrir_janela1(self):
        
        if self.janela2:
            self.janela2.withdraw()

        self.janela = customtkinter.CTk()
        self.janela.title("BudgetBuddy")
        self.janela.geometry("500x600")
        self.janela.maxsize(width=500, height=600)

        #MARGEM TOP
        margem_cima = customtkinter.CTkLabel(self.janela, text="")
        margem_cima.pack(pady=10, side=TOP)


        ################## Carregando (tentando) a imagem #################
        # if imagem is None:
        #     imagem = carregar_imagem()
        
        # # Crie um widget Label para exibir a imagem
        # label_imagem = Label(janela, image=imagem, bg="#242424", anchor=NW)
        # label_imagem.image_names = imagem
        # label_imagem.pack(padx=0, pady=0)
        ###################################################################
        
        
        #MARGEM TOP
        margem_cima = customtkinter.CTkLabel(self.janela, text="")
        margem_cima.pack(pady=10, side=TOP)

        # LABEL GRUPO
        grupo = customtkinter.CTkLabel(self.janela, text="Adicione Pessoas ao seu grupo !", font=("Arial",16, "bold"))
        grupo.pack(padx=10, pady=3)

        #MARGEM 
        margem = customtkinter.CTkLabel(self.janela, text="")
        margem.pack(pady=5, side=TOP)

        # LABEL GRUPO
        nome = customtkinter.CTkLabel(self.janela, text="Nome:                  ", font=("Arial",16, "bold"))
        nome.pack(padx=10, pady=3)

        # ENTRY NOME
        entry = customtkinter.CTkEntry(self.janela)
        entry.pack(padx=10, pady=3)
        entry.configure(fg_color="#3d3d3d")

        # BOTÃO INSERIR
        def inserir_nome():
            nome_inserido = entry.get()
            Controller.new_user(self=self.controller, user=nome_inserido)
            entry.delete(0, END)

        botao = customtkinter.CTkButton(self.janela, text="Inserir", command=inserir_nome)
        botao.pack(padx=10, pady=10)
        botao.configure(corner_radius=10, font=("Arial",15, "bold"))

        #MARGEM
        margem2 = customtkinter.CTkLabel(self.janela, text="")
        margem2.pack(pady=10, side=TOP)

        # LABEL CONCLUIR
        nome = customtkinter.CTkLabel(self.janela, text="Não quer inserir mais ninguém?", font=("Arial",16, "bold"))
        nome.pack(padx=10, pady=3)

        # Button to open janela2
        botao2 = customtkinter.CTkButton(self.janela, text="Concluir", command=self.abrir_janela2, hover_color='dark green')
        botao2.pack(padx=10, pady=10)
        botao2.configure(corner_radius=10, font=("Arial",15, "bold"))

        self.janela.mainloop()

    def abrir_janela2(self):
        
        if self.janela:
            self.janela.withdraw()
        
        if self.janela3:
            self.janela3.withdraw()

        if self.janela4:
            self.janela4.withdraw()

        self.janela2 = customtkinter.CTk()
        self.janela2.title("BudgetBuddy")
        self.janela2.geometry("500x600")
        self.janela2.maxsize(width=500, height=700)

        # Button to go back to janela1
        botao2 = customtkinter.CTkButton(self.janela2, text="Voltar", command=self.abrir_janela1)
        botao2.place(x=20, y=20)
        botao2.configure(corner_radius=10, font=("Arial",15, "bold"))

        #MARGEM TOP
        margem_cima = customtkinter.CTkLabel(self.janela2, text="")
        margem_cima.pack(pady=30, side=TOP)

        # LABEL GRUPO
        grupo = customtkinter.CTkLabel(self.janela2, text="Integrantes do Grupo :", font=("Arial",16, "bold"), text_color='green')
        grupo.pack(padx=10, pady=3)

        #LABEL NOMES
        getusers = Controller.get_users(self=self.controller)

        nomes = customtkinter.CTkLabel(self.janela2, text=getusers)
        nomes.pack(pady=20, side=TOP)
        nomes.configure(font=("Arial",16, "bold"))

        #MARGEM
        margem2 = customtkinter.CTkLabel(self.janela2, text="")
        margem2.pack(pady=15, side=TOP)

        # LABEL GRUPO
        dividas = customtkinter.CTkLabel(self.janela2, text="Dividas em aberto:", font=("Arial",16, "bold"), text_color='red')
        dividas.pack(padx=10, pady=3)

        #LABEL DIVIDAS
        transactions_string = Controller.get_transactions_string(self=self.controller)

        dividas2 = customtkinter.CTkLabel(self.janela2, text=transactions_string)
        dividas2.pack(pady=20, side=TOP)
        dividas2.configure(font=("Arial",16, "bold"))

        # Button to go back to janela1
        botao3 = customtkinter.CTkButton(self.janela2, text="Nova Conta", command=self.abrir_janela3)
        botao3.pack(padx=70, pady=5, side=LEFT)
        botao3.configure(corner_radius=10, font=("Arial",15, "bold"))

        # Button to go back to janela1
        botao4 = customtkinter.CTkButton(self.janela2, text="Pagar Divida", command=self.abrir_janela4)
        botao4.pack(padx=10, pady=5, side=LEFT)
        botao4.configure(corner_radius=10, font=("Arial",15, "bold"))

        self.janela2.mainloop()

    def abrir_janela3(self):
        

        if self.janela2:
            self.janela2.withdraw()

        self.janela3 = customtkinter.CTk()
        self.janela3.title("BudgetBuddy")
        self.janela3.geometry("500x700")
        self.janela3.maxsize(width=500, height=700)

        # Button to go back to janela2
        botao4 = customtkinter.CTkButton(self.janela3, text="Voltar", command=self.abrir_janela2)
        botao4.place(x=20, y=20)
        botao4.configure(corner_radius=10, font=("Arial",15, "bold"))

        #MARGEM TOP
        margem_cima = customtkinter.CTkLabel(self.janela3, text="")
        margem_cima.pack(pady=50, side=TOP)

        # LABEL PAGADOR
        nome_pagador = customtkinter.CTkLabel(self.janela3, text="Nome do Pagador:", font=("Arial",16, "bold"))
        nome_pagador.pack(padx=10, pady=3)

        # ENTRY PAGADOR
        entry2 = customtkinter.CTkEntry(self.janela3)
        entry2.pack(padx=10, pady=0)
        entry2.configure(fg_color="#3d3d3d")

        # LABEL PREÇO
        preco = customtkinter.CTkLabel(self.janela3, text="Valor da Conta:     ", font=("Arial",16, "bold"))
        preco.pack(padx=10, pady=3)

        # ENTRY PREÇO
        entry3 = customtkinter.CTkEntry(self.janela3)
        entry3.pack(padx=10, pady=0)
        entry3.configure(fg_color="#3d3d3d")

        #MARGEM
        margem2 = customtkinter.CTkLabel(self.janela3, text="")
        margem2.pack(pady=20, side=TOP)
    
        # BOTÃO ADICIONAR CONTA
        def novaconta():
            status = customtkinter.CTkLabel(self.janela3, text='', font=("Arial",16, "bold"))
            pagador = entry2.get()
            preco = entry3.get()
            Controller.nova_conta(self=self.controller, pagador=pagador, valor=preco)
            entry2.delete(0, END)
            entry3.delete(0, END)
            # LABEL NOVA CONTA STATUS
            status = customtkinter.CTkLabel(self.janela3, text=Controller.get_nova_conta_status(self=self.controller), font=("Arial",16, "bold"))
            status.pack(padx=10, pady=10)

        botao5 = customtkinter.CTkButton(self.janela3, text="Adicionar Conta", command=novaconta)
        botao5.pack(padx=10, pady=10)
        botao5.configure(corner_radius=10, font=("Arial",15, "bold"))
        
        self.janela3.mainloop()

    def abrir_janela4(self):
        
        if self.janela2:
            self.janela2.withdraw()

        self.janela4 = customtkinter.CTk()
        self.janela4.title("BudgetBuddy")
        self.janela4.geometry("500x700")
        self.janela4.maxsize(width=500, height=700)

        # Button to go back to janela2
        botao6 = customtkinter.CTkButton(self.janela4, text="Voltar", command=self.abrir_janela2)
        botao6.place(x=20, y=20)
        botao6.configure(corner_radius=10, font=("Arial",15, "bold"))

        #MARGEM TOP
        margem_cima = customtkinter.CTkLabel(self.janela4, text="")
        margem_cima.pack(pady=50, side=TOP)

        # LABEL PAGADOR
        nome_pagador2 = customtkinter.CTkLabel(self.janela4, text="Nome do Pagador:", font=("Arial",16, "bold"))
        nome_pagador2.pack(padx=10, pady=3)

        # ENTRY PAGADOR
        entry4 = customtkinter.CTkEntry(self.janela4)
        entry4.pack(padx=10, pady=0)
        entry4.configure(fg_color="#3d3d3d")

        # LABEL BENEFICIADO
        nome_beneficiado = customtkinter.CTkLabel(self.janela4, text="Nome do Beneficiado:", font=("Arial",16, "bold"))
        nome_beneficiado.pack(padx=10, pady=3)

        # ENTRY PREÇO
        entry5 = customtkinter.CTkEntry(self.janela4)
        entry5.pack(padx=10, pady=0)
        entry5.configure(fg_color="#3d3d3d")

        #MARGEM
        margem2 = customtkinter.CTkLabel(self.janela4, text="")
        margem2.pack(pady=20, side=TOP)

        # BOTÃO PAGAR DIVIDA
        def pagar_a_divida():
            pagador = entry4.get()
            beneficiado = entry5.get()
            Controller.pagar_divida(self=self.controller, pagador=pagador, receptor=beneficiado)
            entry4.delete(0, END)
            entry5.delete(0, END)
            # LABEL PAGAR DIVIDA STATUS
            status2 = customtkinter.CTkLabel(self.janela4, text=Controller.get_pagar_divida_status(self=self.controller), font=("Arial",16, "bold"))
            status2.pack(padx=10, pady=3)

        botao7 = customtkinter.CTkButton(self.janela4, text="Pagar Divida", command=pagar_a_divida)
        botao7.pack(padx=10, pady=10)
        botao7.configure(corner_radius=10, font=("Arial",15, "bold"))

        self.janela4.mainloop()

