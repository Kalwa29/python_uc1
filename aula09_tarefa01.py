#valores da lista
vet_dados=[10, 20, 30, 40, 50, 29]
vet_dados_2=[10, 20, 30, 40, 50, 29, 99, 33, 65, 77]

#criando e imprimindo lista
def criar_imprimir_lista(lista2):
    lista=[10,20,30,40,50,]
    print(f"\n\ta nossa lista é {lista}\n")

#criando e imprimindo lista2
def criar_imprimir_lista_02(lista):
    print (f"\n\ta nossa lista é {lista}\n")

#alterando uma lista
def alterar_uma_lista(lista2):
    for elemento in vet_dados_2:
        print(f"\n\tOs elementos da nossa lista é {vet_dados_2}\n")

def alterar_uma_lista_02(lista2):
    print(f"\n\tOs elementos da nossa lista é {lista2}")


def maior_ou_menor_da_lista(lista2):
    # Passo 2: Utilizar as funções max() e min() para encontrar os valores.
    maior = max(lista2)
    menor = min(lista2)
    # Passo 3: Imprimir os resultados.
    print(f"\n\tMaior valor da nossa lista é {maior}")
    print(f"\tMenor valor da nossa lista é {menor}")


def invertendo_a_ordem_dos_elementos_da_lista(lista2):
    # Passo 2: Inverter o vetor utilizando slicing.
    vetor_invertido = vet_dados_2[::-1]
    # Passo 3: Imprimir o vetor invertido.
    print(f"\n\tA nossa lista invertida é {vetor_invertido}\n")


def multiplicar_elementos_da_lista_por_2(lista2):
# Passo 1: Definir o vetor original.

# Passo 2: Definir o multiplicador.
    multiplicador = 2
# Passo 3: Utilizar list comprehension para multiplicar cada elemento.
    lista2 = [elemento * multiplicador for elemento in vet_dados_2]
# Passo 4: Imprimir o novo vetor.
    print(f"\n\tA multiplicação da nossa lista é {lista2} ")



def contagem_do_valor_3_na_lista(vet_dados_2, valor=3):
    # Passo 1: Definir o vetor.
    lista2 = vet_dados_2
# Passo 2: Utilizar o método count() para contar o valor 3.
ocorrencias = vet_dados_2.count(3)
# Passo 3: Imprimir o resultado.
print(f"\n\tO valor 3 aparece {ocorrencias} vezes\n")


if __name__ == "__main__":
    #criar_imprimir_lista()
    #criar_imprimir_lista_02 (lista2)
    #alterar_uma_lista()
    #alterar_uma_lista_02(lista2)
    #maior_ou_menor_da_lista (vet_dados)
    #maior_ou_menor_da_lista (vet_dados_2)
    #invertendo_a_ordem_dos_elementos_da_lista()
    #multiplicar_elementos_da_lista_por_2(vet_dados_2)
    contagem_do_valor_3_na_lista(vet_dados_2)