idade=int(input("me de a sua idade : "))
habilitado=input("possui carteira de habilitação <s/n> : ")
habilitado=habilitado.lower()

if (idade >= 18) and (habilitado == "s"):
    print("voce pode dirigir!")
else:
    print("desculpe, sem carteira nao da!")