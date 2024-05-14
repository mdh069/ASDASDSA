import random 
class JogoAdivinha(): 
    def __init__(self, num_min, num_max): 
        self.num_min = num_min 
        self.num_max = num_max 
    
    def jogar(self): 
        num_tentativa = 0 
        numero_gerado = random.randrange(self.num_min, self.num_max) 
        while(True): 
            numero_digitado = int(input("De um palpite de numero: ")) 
            num_tentativa += 1 
            if numero_digitado == numero_gerado: 
                print(f"Voce acertou o numero era {numero_digitado}, voce tentou {num_tentativa} vezes") 
                break 
            elif numero_digitado > numero_gerado: 
                print("O numero para adivinhar é menor") 
            else: 
                print("O numero para adivinhar é maior") 
                
jogo1 = JogoAdivinha(1, 100) 
jogo1.jogar()
