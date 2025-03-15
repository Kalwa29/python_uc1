l1=input("me de o valor do primeiro lado do triângulo :")
l1=float(l1)
l2=input("me de o valor do segundo lado do triângulo :")
l2=float(l2)
l3=input("me de o valor do terceiro lado do triângulo :")
l3=float(l3)

if (l3==l2) and (l3==l1) :
    print("o triângulo é Equilátero")

elif (l1==l2) or (l1==l3) or (l2==l3) :
    print("o triângulo é Isóceles")

else:
    print("o triângulo é Escaleno")