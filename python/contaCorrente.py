class Conta:
    def __init__(self, numero_da_conta, nome_correntista, saldo, sal):
        self.numero_da_conta = numero_da_conta
        self.nome_correntista = nome_correntista
        self.__saldo = saldo
        self.numeroAleatorio = sal
        
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, novo_valor):
        self.__saldo = novo_valor
    
    def deposito(self):
        valor_deposito = float(input("Qual vai ser o valor do deposito: "))
        self.__saldo += valor_deposito
    
    def saque(self):
        valor_saque = float(input("Qual vai ser o valor de saque: "))
        if valor_saque > self.saldo:
            print("Voce não tem esse dinheiro")
        else: 
            self.saldo -= valor_saque
            return valor_saque
    
    def extrato(self):
        print(f"O saldo e {self.saldo}")
        print(f"O saldo e {self.numeroAleatorio}")
        
        
derik = Conta(26, "DEREK ALBURQUERQUE", 2000, 10)
derik.deposito()
derik.saque()
derik.extrato()
derik.numeroAleatorio = "GUlherme"
derik.extrato()
