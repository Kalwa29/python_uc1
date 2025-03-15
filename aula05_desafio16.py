idade=input("Digite a sua idade")
idade=int(idade)
renda=input("Digite a sua renda")
renda=int(renda)
nao_ter_nome_sujo=input("Voce tem nome sujo <s/n> : ")
nao_ter_nome_sujo=nao_ter_nome_sujo.lower()

if (nao_ter_nome_sujo == "n") and (idade >= 21) and (renda>=2000):
    print("Voce pode retirar o emprestimo!!!")

else:
    print("Voce nao pode tirar emprestimo!!")
