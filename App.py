import tkinter 
import os 
from tkinter import ttk


class Aplicação:
    def __init__(self):

        self.programa = tkinter.Tk()
        self.config = self.configurações()
        self.frame1 = self.frame1config()
        self.frame2 = self.frame2config()
        self.text = self.textos()
        self.escreve = self.extractcontent()
        self.infinito = self.programa.mainloop()

    def configurações(self):

        self.config = self.programa.geometry('400x400')
        self.config = self.programa.title('Programa')

    def frame1config(self):

        frame1 = tkinter.Frame(self.programa, background='lightblue', highlightbackground='Red', highlightthickness=2)
        frame1.place(relx=0.04, rely=0, relwidth=0.9, relheight=0.5)
        botaopesquisar = tkinter.Button(frame1, text='Pesquisar', command=self.butonpesquisar)
        botaopesquisar.place(relx=0.77, rely=0.4, relwidth=0.2, relheight=0.1)
        botaoapagar = tkinter.Button(frame1, text="Apagar", command=self.buttonapagar)
        botaoapagar.place(relx=0.77, rely=0.6, relwidth=0.2, relheight=0.1)
    def textos(self):

        diretoriodearquivos = tkinter.Label(self.frame1, text='Nome do diretorio', font=('Arial', 10), background='white')
        diretoriodearquivos.place(relx=0.1, rely=0.2)
        Nomeparaapagar = tkinter.Label(self.frame1, text="Em espera", font=('Arial', 10), background='white')
        Nomeparaapagar.place(relx=0.1, rely=0.3)

    def frame2config(self):

        frame2 = tkinter.Frame(self.programa, highlightbackground='black', highlightthickness=2)
        frame2.place(relx=0.04, rely=0.5, relwidth=0.9, relheight=0.5)

        self.tree = ttk.Treeview(frame2, columns=("indice", "Nome"), show="headings")
        
        self.tree.column("indice", minwidth=0, width=50)
        self.tree.column("Nome", minwidth=0, width=250)

        self.tree.heading("indice", text="Indice")
        self.tree.heading("Nome", text="Nomes")

        barra_de_rolagem = ttk.Scrollbar(frame2, orient='vertical')
        barra_de_rolagem.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)

        self.tree.configure(yscroll=barra_de_rolagem)
        self.tree.pack()

    def extractcontent(self):

        self.escrever1 = tkinter.Entry(self.frame1, width=20)
        self.escrever1.place(relx=0.41, rely=0.2)

        self.escrever2 = tkinter.Entry(self.frame1, width=20)
        self.escrever2.place(relx=0.41, rely=0.3)

    def butonpesquisar(self):

        for root, dir, files in os.walk(self.escrever1.get()):
            for file in files:
                for c in range(1, len(files)-1):
                    self.tree.insert("", "end",  values=[c, os.path.join(root,file)])
    
    def buttonapagar(self):
        for root, dir, files in os.walk(self.escrever1.get()):
            for file in files:
                arquivo = os.path.join(root, file)
                if self.escrever2.get() in file:
                    os.remove(arquivo)
program = Aplicação()