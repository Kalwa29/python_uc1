import sys
def main(args):
    for arg in args:
        print(arg)

def soma (numeros) :
    somatorio=0
    for valor in numeros:
        somatorio=somatorio+float (valor)

    #print(f"o valor da soma dos numeros e :{somatorio}")
    return somatorio

if __name__ == "__main__":
    resultado=soma(sys.argv[1:])
print(f"o valor da soma dos numeros e :{resultado}")