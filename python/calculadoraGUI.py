import tkinter as tk

janela = tk.Tk()
janela.title = "Calculadora"

text_principal = tk.Label(text="Calculadora") 
text_resultado = tk.Label(text="Resultaldo sera mostrado aqui")
input_num1 = tk.Entry()
input_num2 = tk.Entry()
buttons = [tk.Button(text="Somar", width=20, height=1), tk.Button(text="Subtração", width=20, height=1), tk.Button(text="Multiplicação", width=20, height=1), tk.Button(text="Dividir", width=20, height=1)]

text_principal.pack(pady=30)
input_num1.pack(pady=6)
input_num2.pack()
text_resultado.pack(pady=10)

def acessa_numeros ():
    return [float(input_num1.get()), float(input_num2.get())]

for botao in buttons:
    indice = buttons.index(botao)
    if indice == 0:
        def soma():
            try:
                text_resultado.config(text=sum(acessa_numeros()))
            except:
                text_resultado.config(text="Realize uma operação válida")
        botao.config(command=soma)
    if indice == 1:
        def sub():
            try:
                text_resultado.config(text=acessa_numeros()[0]-acessa_numeros()[1])
            except:
                text_resultado.config(text="Realize uma operação válida")
        botao.config(command=sub)
    if indice == 2:
        def multi():
            try:
                text_resultado.config(text=acessa_numeros()[0]*acessa_numeros()[1])
            except:
                text_resultado.config(text="Realize uma operação válida")
        botao.config(command=multi)
    if indice == 3:
        def div():
            try:
                text_resultado.config(text=acessa_numeros()[0]/acessa_numeros()[1])
            except:
                text_resultado.config(text="Realize uma operação válida")
        botao.config(command=div)
    botao.pack(pady=10)

janela.mainloop()