1-
a=int(input("digite um numero :"))
b=int(input("digite outro numero :"))
media=(a+b)
print(f"a soma dos numeros é :{media}")

2-
numero=int(input("digite um numero :"))
resultado=numero%2
if resultado==0 :
    print("este numero é par")
else:
    print("este numero é impar")

3-
a=input("me de um numero :")
valor=int(a)
a=float(a)
b=input("Me de a mais um numero :")
valor=(b)
b = float(b)

if a > b:
    print(f"o numero maior e {a}")

elif b > a:
    print(f"o numero maior e {b}")

else:
    print("esses numeros sao iguais")"

5-
numero=input("Digite um numero :")
numero=float(numero)
fatorial=1
while numero>0:
    fatorial=fatorial*numero
    numero=numero-1
    print(fatorial)


6-
a = 0
b = 1
fibonacci_sequence = []
for i in range(10):
    fibonacci_sequence.append(a)
    numeros = a + b
    a = b
    b = numeros

print(fibonacci_sequence)"

7-
numero=int(input("Digite um numero :"))
if numero <= 1:
    print(f"{numero} não é um numero primo.")
else:
    primo=True

for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break
if primo:
    print(f"{numero} é um numero primo")
else:
    print(f"{numero} não é numero primo")"

9-
a=input("Me de a primeira nota :")
a = float(a)
b=input("Me de a segunda nota :")
b = float(b)
c=input("Me de a terceira nota :")
c = float(c)
d=input("Me de a quarta nota :")
d = float(d)
e=input("Me de a quinta nota :")
e = float(e)

menor_nota=a
soma = a+b+c+d+e
for nota in [b, c, d, e]:
    if nota < menor_nota:
        menor_nota=nota
media=(soma - menor_nota)/4
print(f"A média aritmética das notas é : {media:.2f}, excluindo a menor nota que é {menor_nota}")




portugol


1- Soma de Dois Números
algoritmo "Soma"
var
    a, b, soma: inteiro
inicio
    escreva("Digite um número: ")
    leia(a)
    escreva("Digite outro número: ")
    leia(b)
    soma := a + b
    escreva("A soma dos números é: ", soma)
fimalgoritmo

2- Verificação de Par ou Ímpar
algoritmo "ParOuImpar"
var
    numero: inteiro
inicio
    escreva("Digite um número: ")
    leia(numero)
    se numero % 2 = 0 entao
        escreva("Este número é par.")
    senao
        escreva("Este número é ímpar.")
    fimse
fimalgoritmo

3- Comparação de Dois Números
algoritmo "Comparacao"
var
    a, b: real
inicio
    escreva("Me dê um número: ")
    leia(a)
    escreva("Me dê mais um número: ")
    leia(b)
    se a > b entao
        escreva("O número maior é: ", a)
    senao se b > a entao
        escreva("O número maior é: ", b)
    senao
        escreva("Esses números são iguais.")
    fimse
fimalgoritmo

5- Cálculo do Fatorial
algoritmo "Fatorial"
var
    numero, fatorial: inteiro
inicio
    escreva("Digite um número: ")
    leia(numero)
    fatorial := 1
    enquanto numero > 0 faca
        fatorial := fatorial * numero
        numero := numero - 1
    fimenquanto
    escreva("O fatorial é: ", fatorial)
fimalgoritmo

6- Sequência de Fibonacci
algoritmo "Fibonacci"
var
    a, b, temp, i: inteiro
inicio
    a := 0
    b := 1
    escreva("A sequência de Fibonacci é: ")
    para i de 1 ate 10 faca
        escreva(a, " ")
        temp := a
        a := b
        b := temp + b
    fimpara
fimalgoritmo

7- Verificação de Número Primo
algoritmo "NumeroPrimo"
var
    numero, i: inteiro
    primo: booleano
inicio
    escreva("Digite um número: ")
    leia(numero)
    se numero <= 1 entao
        escreva(numero, " não é um número primo.")
    senao
        primo := verdadeiro
        para i de 2 ate numero - 1 faca
            se numero % i = 0 entao
                primo := falso
                pare
            fimse
        fimpara
        se primo entao
            escreva(numero, " é um número primo.")
        senao
            escreva(numero, " não é um número primo.")
        fimse
    fimse
fimalgoritmo

9- Média Aritmética com Exclusão
algoritmo "MediaExclusao"
var
    a, b, c, d, e, menor_nota: real
    soma: real
inicio
    escreva("Me dê a primeira nota: ")
    leia(a)
    escreva("Me dê a segunda nota: ")
    leia(b)
    escreva("Me dê a terceira nota: ")
    leia(c)
    escreva("Me dê a quarta nota: ")
    leia(d)
    escreva("Me dê a quinta nota: ")
    leia(e)
    
    menor_nota := a
    soma := a + b + c + d + e
    se b < menor_nota entao
        menor_nota := b
    fimse
    se c < menor_nota entao
        menor_nota := c
    fimse
    se d < menor_nota entao
        menor_nota := d
    fimse
    se e < menor_nota entao
        menor_nota := e
    fimse
    
    escreva("A média aritmética das notas é: ", (soma - menor_nota) / 4, ", excluindo a menor nota que é ", menor_nota)
fimalgoritmo
