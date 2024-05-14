import random

# 12 e 12.3 e 12.4 pois esse código sempre gera 6 numeros diferentes
numeros_random = []
for i in range(6):
    numero_gerado = random.randint(1,61)
    while numero_gerado in numeros_random:
        numero_gerado = random.randint(1,61)
    numeros_random.append(numero_gerado)

# 12.1
numeros_random.sort()
print(numeros_random)

#12.2
print(f"maior:{max(numeros_random)}, menor: {min(numeros_random)}")