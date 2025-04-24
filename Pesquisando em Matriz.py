from random import randint

matriz = []

for m in range(10):
    lista_temporaria = []

    for n in range(10):
        lista_temporaria.append(randint(0, 1000))

    matriz.append(lista_temporaria)

maior = -1
pos_maior = -1
menor = 1000
pos_menor = -1

for linha in range(len(matriz)):
    print(matriz[linha])
    for coluna in range(len(matriz[linha])):
        if maior < matriz[linha][coluna]:
            maior = matriz[linha][coluna]
            pos_maior = linha, coluna
        if menor > matriz[linha][coluna]:
            menor = matriz[linha][coluna]
            pos_menor = linha, coluna
print('-----------------------------------------------------------------------')
print(f'O maior valor é {maior} e sua posição é {pos_maior}')
print(f'O menor valor é {menor} e sua posição é {pos_menor}')