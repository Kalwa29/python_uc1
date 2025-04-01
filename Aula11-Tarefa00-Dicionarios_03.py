#Contato de frequencia
frase="Trabalhamos nas sombras para servir a luz, nada é verdade tudo é permitido, nós somos assassinos"
palavras=frase.split()
contagem={}


for palavra in palavras:
    contagem[palavra]=contagem.get(palavra, 0)+1
print(contagem)