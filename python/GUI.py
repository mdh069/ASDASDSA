import tkinter as tk

janela = tk.Tk()
janela.title("Primeiro GUI")
janela.geometry("800x600")

text = tk.Label(text="Clica neles")

def botao1():
    text.config(text="Clica no Outro botão")
    print("chamou")
def botao2():
    text.config(text="Clica no botão Vermelho")
    print("chamou")

botao1 = tk.Button(janela, text="Botao1", command=botao1, bg="green", fg="white", height=1, width=20)
botao2 = tk.Button(janela, text="Botao2", command=botao2, bg ="red", fg="white", height=1, width=20)

text.pack()
botao1.pack(padx=50, pady=50)
botao2.pack(padx=50, pady=50)


janela.mainloop()