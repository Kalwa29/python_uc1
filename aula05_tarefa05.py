SENHA_CORRETA="1234a"

idade=int(input("informe a sua idade :"))
if (idade>=18):
    senha=input("informe a senha de acesso:")
    if(senha==SENHA_CORRETA):
        print("!!!  ACESSO_LIBERADO !!!")
    else:
        print("!!! ACESSO_NEGADO !!!")
    else:
    print("!!! ACESSO_NEGADO_IDADE !!!")