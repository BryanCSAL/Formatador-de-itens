import numpy as np

# Cria uma matriz 2x3 com tipo de dado string (object)
matriz = np.empty((2, 3), dtype=object)

# Preenchendo a matriz com inputs
for i in range(2):
    for j in range(3):
        if j == 0:
            entrada = input("Digite o Nome: ")
        elif j == 1:
            entrada = input("Digite a Quantidade: ")
        else:
            entrada = input("Digite o Valor: ")
        matriz[i, j] = entrada

# Criar lista para armazenar os textos formatados
itens = [None] * 2

# Montando a string para cada item
for i in range(2):
    nome = matriz[i, 0]
    quantidade = matriz[i, 1]
    valor = matriz[i, 2]
    itens[i] = "Item número " + str(i+1) + " | Nome: " + nome + " | Quantidade: " + quantidade + " | Valor: " + valor

# Exibindo os itens
for item in itens:
    print(item)
