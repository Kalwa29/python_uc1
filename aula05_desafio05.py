nome=input("digite seu nome:")
senha=input("digite sua senha:")

if ( len(nome) < 3):
    print ("nome invalido!!!")

elif ( len(senha) < 6):
    print("senha invalida!!!")

elif (senha=="123456") or (senha=="senha") :
    print("senha muito fraca")

else :
    print ("cadastro concluido!!!")