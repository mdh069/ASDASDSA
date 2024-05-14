class Funcionario():
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.__salario = salario
        self.__cargo = cargo
    
    def calcular_bonus(self):
        bonus = self.__salario * 1.10
        print(f"seu bonus é {bonus}")
        return bonus
    
    def info_funcinario(self):
        print(f"nome: {self.nome} salario: {self.__salario} cargo: {self.__cargo}")
        
    @property
    def salario(self):
        return self.__salario 
    
class Gerente(Funcionario):
    def __init__(self, nome, salario, cargo):
        super().__init__(nome, salario, cargo)
        
    def calcular_bonus(self):
        bonus = self.salario * 1.15
        print(f"seu bonus é {bonus}")
        return bonus
    
class Vendedor(Funcionario):
    def __init__(self, nome, salario, cargo):
        super().__init__(nome, salario, cargo)
        
    def calcular_bonus(self):
        bonus = (self.salario * 1.05) + 500
        print(f"seu bonus é {bonus}")
        return bonus

        
davi_friz = Vendedor("Davi Friz", 2000, "Gerente de caixa")
davi_friz.calcular_bonus()
davi_friz.info_funcinario()