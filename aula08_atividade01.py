"""
Função saudacao
"""
def sauldacao():
    print("ola, seja bem vindo(a) ao curso de python!!!")

"""
Exercício 2: Função soma
"""
def soma(a, b):
    return a + b

def testar_funcao_soma():
# Exemplo de chamada
    resultado = soma(5, 7)
    print("A soma é:", resultado)

"""
Exercício 3: Função par_ou_impar
"""
def par_ou_impar(n):
    if n % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

def testar_funcao_par_ou_imapar():
# Exemplo de chamada
    print("O número 4 é", par_ou_impar(4))
    print("O número 7 é", par_ou_impar(7))

"""
Exercício 4: Função fatorial
"""
def fatorial(n):
    if n < 0:
        return "Número inválido para fatorial."
    elif n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

def testar_funcao_fatorial():
# Exemplo de chamada
    numero=int(input("informe um numero :"))
    resultado=fatorial(numero)
    print(f"\n\n\tfatorial de {numero} e igual a {resultado}\n\n")

"""Exercício 5: Função maior_elemento
"""
def maior_elemento(lista):
    return max(lista)

def testar_funcao_maior_elemento():
# Exemplo de chamada
    numeros = [3, 8, 1, 20, 7]
    print("O maior elemento é:", maior_elemento(numeros))

"""Exercício 6: Função media"""
def media(lista):
    return sum(lista) / len(lista)

def testar_funcoa_media():
# Exemplo de chamada
    valores = [10, 20, 30, 40]
    print("A média é:", media(valores))

"""Exercício 7: Função eh_palindromo"""
def eh_palindromo(palavra):
    return palavra == palavra[::-1]

def testar_funcao_eh_palindromo():
# Exemplos de chamada
    print("ana é palíndromo?", eh_palindromo("ana"))
print("python é palíndromo?", eh_palindromo("python"))

"""Exercício 8: Função contar_vogais"""
def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    contador = 0
    for char in texto:
        if char in vogais:
            contador += 1
    return contador

def testar_contar_vogais ():
# Exemplo de chamada
    print("Número de vogais em 'Python':", contar_vogais("Python"))

"""Exercício 9: Função tabuada"""
def tabuada(n):
    resultado = []
    for i in range(1, 11):
        resultado.append(n * i)
    return resultado

def testar_funcao ():
# Exemplo de chamada
 print("Tabuada do 5:", tabuada(5))

"""Exercício 10: Função ordenar_por_segundo"""

def ordenar_por_segundo(lista_tuplas):
    return sorted(lista_tuplas, key=lambda x: x[1])

def testar_lista ():
# Exemplo de chamada
    lista_exemplo = [("a", 3), ("b", 1), ("c", 2)]
    print("Lista ordenada:", ordenar_por_segundo(lista_exemplo))




if __name__ == "__main__":
# chamar função
 testar_funcao_fatorial()