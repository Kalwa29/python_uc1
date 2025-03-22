import sys 
def calculadora(a, b, op):
    print(f"{a}, {b}, {op}")
    #print (f"{a} {op} {b}")
    if op =="+":
        resultado=a+b
    elif op =="-":
        resultado=a-b
    elif op == "*":
        resultado=a*b
    elif op == "/":
        resultado== a/b

    print(f"{a} {op} {b} = {resultado}")

if __name__ == "__main__":
        argumentos=sys.argv[1:]
a=float(argumentos[0])
b=float(argumentos[1])
op=argumentos[2]
calculadora (a, b, op)


