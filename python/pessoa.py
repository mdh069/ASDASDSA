class Pessoa:
    def __init__( self, nome, idade, peso, altura ):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        
    def envelhecer (self ):
        self.idade += 1
    
    def crescer (self):
        if self.idade < 21:
            self.altura += 0.05
            
    def passar_ano(self):
        self.envelhecer ()
        self.crescer ()
        
    def dados(self):
        print (self.nome, self.idade, self.peso, self.altura)   
        
davi_friz = Pessoa("Davi Friz", 16, 63.5, 1.72)           
davi_friz.passar_ano()
davi_friz.dados()
    
        