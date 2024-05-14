class Calculadora:
    def __init__(self):
       pass

    def soma(self, n1, n2):
        return n1 + n2
        
    def subtracao(self, n1, n2):
        return n1 - n2
        
    def multiplicacao(self, n1, n2):
        return n1 * n2
    
    def dividir(self, n1, n2):
        if n2 == 0:
            return "Nao possivel dividir por 0"
        return n1 / n2
        
    def calcular(self):
        operacao = input("Qual operacao vc quer fazer? ")
        numero1 = float(input("Numero 1 "))
        numero2 = float(input("Numero 2 "))
        if operacao == "+":
            print(f"O resultado da soma é {self.soma(numero1, numero2)}")
        if operacao == "-":
            print(f"O resultado da subtracao é {self.subtracao(numero1, numero2)}")
        if operacao == "*":
            print(f"O resultado da multiplicacao é {self.multiplicacao(numero1, numero2)}")
        if operacao == "/":
            print(f"O resultado da divisao é {self.dividir(numero1, numero2)}")


calculo = Calculadora ()
calculo.calcular()