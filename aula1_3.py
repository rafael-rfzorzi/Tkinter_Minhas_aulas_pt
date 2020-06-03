### Primeira aula sobre Tkinter
### Criando uma janela e aprendendo comandos de configuração da mesma

### Chamando modulo tkinter
from tkinter import *

# Criando uma variavel para identificar a janela
root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        # criando o Loop
        root.mainloop()
    def tela(self):
        self.root.title("Cadastro de Clientes")
        self.root.configure(background= '#1e3743')
        self.root.geometry("700x600")
        self.root.resizable(True, True)
        self.root.maxsize(width=800, height=700)
        self.root.minsize(width=500, height=300)

Application()

