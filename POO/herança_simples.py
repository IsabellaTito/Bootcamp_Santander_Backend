class Veiculo:
    def __init__(self,cor,placa,n_rodas):
        self.cor = cor
        self.placa = placa
        self.n_rodas = n_rodas

    def ligar_motor(self):
        print("Ligando o motor")

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhão(Veiculo):
    def __init__(self, cor, placa, n_rodas, carregado):  
        super().__init__(cor, placa, n_rodas) #Chama a implementação da classe
        self.cor = cor
        self.placa = placa
        self.n_rodas = n_rodas
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'}")        