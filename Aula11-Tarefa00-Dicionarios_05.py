# Definindo uma classe chamada 'Carro'

class Carro:
# Método construtor (__init__) para inicializar os atributos
    def __init__ (self,marca,modelo,ano):
        self.marca=marca # Atributo
        self.modelo=modelo # Atributo
        self.ano=ano # Atributo
        self.ligado=False # Atributo com valor padrão

    def ligar(self):
        self.ligado=True
        print(f" O carro está ligado")


    def desligado(self):
        self.ligado= False
        print(f" O carro está desligado")

    def exibir_info(self):
    
        if self.ligado==True :
            status="ligado"
        
        else:
            status="desligado"
        print(f"{self.marca} {self.modelo} ({self.ano}) está {status}")






if __name__ == "__main__":
    # Criando um objeto da classe Carro
    print(f"Criando um objeto da classe carros")
    meu_carro = Carro ("Toyota", "corolla",2020)
    meu_carro.exibir_info()
    meu_carro.ligar()
    meu_carro.desligado
