class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acrodado = acordado

    def __del__(self):
        print("Removendo a instância da classe.")

    def falar(self):
        print("auauau")


c = Cachorro("Baron","caramelo",True)
c.falar()

del c #remove de forma forçada a instância da classe
#Sem essa linha o destrutor só remove a instância ao fim do código
