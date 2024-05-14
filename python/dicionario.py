#pais1 = input("digite o país e sua capital: ")
#pais2 = input("digite o país e sua capital: ")
#pais3 = input("digite o país e sua capital: ")
#pais4 = input("digite o país e sua capital: ")
#pais5 = input("digite o país e sua capital: ")

#Paises = {"pais1": pais, "pais2": pais2, "pais3": pais3, "pais4": pais4, "pais5": pais5}

#print(Paises)

aluno = []

while True:

    nome_aluno = input("insira seu nome:" )
    if nome_aluno == "inicio" :
        break
    parcial_aluno = input("Insira a parcial do aluno: ")
    bimestral_aluno = input("Insira a bimestral do aluno: ")
    aluno.append({"Nome": nome_aluno, "parcial": parcial_aluno, "bimestral": bimestral_aluno})

    print(aluno)
    