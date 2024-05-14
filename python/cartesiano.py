import math

class Cartesiano():
    def __init__(self, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y
    
    def distancia_origem(self):
        return math.sqrt((self.coord_x ** 2) + (self.coord_y ** 2))
    
ponto1 = Cartesiano()
print(ponto1.distancia_origem())