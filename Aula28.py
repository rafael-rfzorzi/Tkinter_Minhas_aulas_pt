from tkinter import *
from tkinter import ttk
import time

root = Tk()
root.title("Progress Bar")
root.geometry("500x400")

def step():
    #progress1['value'] +=10
    #progress1.start(10)
    for x in range(10):
        progress1['value'] +=10
        root.update_idletasks()
        time.sleep(1)

def stop():
    progress1.stop()

progress1 = ttk.Progressbar(root, orient=HORIZONTAL, length=300, mode= 'determinate')
progress1.pack(pady=20)

botao = Button(root, text="Progresso", command=step)
botao.pack(pady=20)

botao2 = Button(root, text="Parar", command= stop)
botao2.pack(pady=20)



root.mainloop()