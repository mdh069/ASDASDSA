#14
contatos = {}
print("\nPara parar de adicionar contatos coloque o nome do contanto como 'fim'")

while True:
    nome = input("nome do contato: ")
    if nome == "fim":
        break
    else:
        numero = input("numero do contato: ")
        contatos[nome] = numero
    contatos[nome] = numero

print(contatos)