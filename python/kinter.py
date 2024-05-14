import tkinter as friz

janela = friz.Tk()
janela.config(bg="black")
janela.title("calculadora")

titulo = friz.Label(text="informe o número: ")
titulo.pack()

entrada1 = friz.Entry(janela)
entrada1.pack(padx=20, pady=20)



titulo2 = friz.Label(text="informe o número: ")
titulo2.pack()

entrada2 = friz.Entry(janela)
entrada2.pack(padx=20, pady=20)

radio = friz.IntVar()

rb_soma = friz.Radiobutton(janela, text="+", variable=radio, value=1)
rb_soma.pack()

rb_subtracao= friz.Radiobutton(janela, text="-", variable=radio, value=2)
rb_subtracao.pack()

rb_multiplicao = friz.Radiobutton(janela, text="x", variable=radio, value=3)
rb_multiplicao.pack()

rb_divisao = friz.Radiobutton(janela, text="%", variable=radio, value=4)
rb_divisao.pack(pady=10)

def calcular():
    n1 = float(entrada1.get())
    n2 = float(entrada2.get())
    operacao = radio.get()

    if operacao == 1:
        resultado = n1 + n2
    elif operacao == 2:
        resultado = n1 - n2
    elif operacao == 3: 
        resultado = n1 * n2   
    elif operacao == 4:
        resultado = n1 / n2
        
        if n2 == 0:
            resultado = "Erro"
        else:
            n1 / n2    
    else:    
        resultado = "Erro"
        
        print(resultado)
        lb_resultado.config(text=resultado)


botao = friz.Button(janela, text="Calcular", bg="orange", fg="white")
botao.pack()

lb_resultado = friz.Label(janela, text="oii")
lb_resultado.pack()

janela.geometry("500x500")

janela.mainloop()


