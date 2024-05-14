import random
import math

class Dado():    
    def __init__(self, lados_do_dado):
        self.lados_do_dado = lados_do_dado
        
    def lancar_dados(self):
        return random.randrange(1, self.lados_do_dado  +1)
    
    def lancar_dados_raiz(self):
        return math.sqrt(random.randrange(1, self.lados_do_dado  +1))
    
d20 = Dado(10)

# inclui as duas atividades de dados aqui