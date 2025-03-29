"""
# criando matriz 3x3
matriz=[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Elemento (0,0):",matriz[0][0]) #Saída: 1
print("Elemento (2,1):",matriz[2][1]) #Saída: 8

for linha in matriz:
    for elemento in linha:
        print(f"|{elemento}|", end=' ')
    print()


def imprimir_matriz():

    matriz = [[int(input(f"Digite o valor para [{i}][{j}]: ")) for j in range(4)] for i in range(4)]

for linha in matriz:
    print(linha)


def imprimir_matriz_2():

    matriz=[]
for i in range(4):
    linha=[]
    for j in range(4):
        valor=int(input(f"Digite o valor para [{i}][{j}]: "))
        linha.append(linha)
    matriz.append(linha)

for linha in matriz:
    print(linha)
"""



matriz_4_4=[
    [1, 2, 3, 4,],
    [5, 6, 7, 8,],
    [9, 10, 11, 12,],
    [13, 14, 15, 16]
]


def soma_dos_elemntos():
    soma = 0
    for i in range(4):
        for j in range(4):
            soma=soma + matriz_4_4[i][j]

    print(f"Soma dos elementos acima da diagonal principal: {soma}")


def soma_de_elementos_v2():
    soma=0
    for i in range(4):
        soma=soma+sum(matriz_4_4[i])
    print(f"Soma dos elementos acima da diagonal principal: {soma}")


def soma_de_elementos_v3():
    soma=0
    for linha in matriz_4_4:
        soma=soma+sum(linha)
    print(f"Soma dos elementos acima da diagonal principal: {soma}")

#criar kista para armazenar os maiores valores da Linha

def maior_valor_de_cada_linha():
    lista=[]
    for i in range(4):
        maior=max(matriz_4_4[i])
        #lista recebe o maior valor da linha
        print(f"Maior valor da linha {i}: [{maior}]")
        

def contagem_de_pares():
    pares = 0
    impares = 0
    vet_pares=[]
    vet_impares=[]
    for i in range(4):
        for j in range(4):
            if matriz_4_4[i][j] % 2 == 0:
                pares = pares + 1
                vet_pares.append(matriz_4_4[i][j])
            else:
                impares = impares + 1
                vet_impares.append(matriz_4_4[i][j])
    print(f"Quantidade de números pares: {pares}")
    print(f"Quantidade de números impares: {impares}")

    print(f"Os numeros pares são : {vet_pares}")
    print(f"Os numeros impares são : {vet_impares}")


def multiplicação_de_linhas():
    num = int(input("Digite o número para multiplicação: "))
linha_escolhida = int(input("Digite a linha a ser multiplicada (0-3): "))

linha=matriz_4_4[linha_escolhida]

for j in range(4):
    linha=[j]=linha[j]
    matriz_4_4[linha_escolhida] * num

for linha in matriz_4_4:
    print(linha)













if __name__ == "__main__":
    #imprimir_matriz()
    #imprimir_matriz_2()
    #soma_dos_elemntos()
    #soma_de_elementos_v2()
    #soma_de_elementos_v3()
    #maior_valor_de_cada_linha()
    contagem_de_pares()