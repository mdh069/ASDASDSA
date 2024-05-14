# class Pessoa: 
#     def __init__(self, nome, idade, email):
#         self.nome = nome
#         self.idade = idade
#         self.email = email

#     def saudar(self):
#         print(f"ola sou {self.nome} tenho {self.idade} anos e email {self.email}")

# marcos = Pessoa("Marcos friz", 28, "friz@gmail.com")
# marcos.saudar()

# class Livro:
#     def __init__(self, titulo, autor, ano_publicacao):
#         self.titulo = titulo
#         self.autor = autor
#         self.ano_publicacao = ano_publicacao
    
#     def detalhes(self):
#         print(f"O livro {self.titulo}, foi escrito por {self.autor} no ano {self.ano_publicacao}")

# livroFriz = Livro("Familia feliz", "Raphael Montes", 2024)
# livroFriz.detalhes()

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
        self.PI = 3.14

    def area(self):
        print(f"A area do círculo é {self.PI * (self.raio ** 2)}")

    def perimtero(self):
        print(f"O perimetro do circulo e {2 * self.PI * self.raio} ")

circulo = Circulo("circulo", 20, 29, 3)
circulo.perimtero()

class Retangulo(FiguraGeometrica):

    def __init__(self, nome, base, altura, raio):
        super().__init__(nome, base, altura, raio)

    def area(self):
        print(f"A area do retangulo é {(self.base * self.altura)}")

    def perimetro(self):
        print(f"O perimetro do reatangulo e {2*(self.base + self.altura)} ")

retangulo = Retangulo("retangulo",10,5)
retangulo.perimetro()











        
        