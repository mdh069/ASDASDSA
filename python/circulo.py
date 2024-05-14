import math

class FiguraGeometrica:
    def __init__(self, nome, base, altura, raio):
        self.nome = nome
        self.base = base
        self.altura = altura
        self.raio = raio
    
    def area(self):
        pass
     
    def perimtero(self):
        pass

class Circulo(FiguraGeometrica):
    def __init__(self, nome, base, altura, raio):
        super().__init__(nome, base, altura, raio)

    def area(self):
        print(f"A area do círculo é {math.pi * (self.raio ** 2)}")

    def perimtero(self):
        print(f"O perimetro do circulo e {2 * self.PI * self.raio} ")