class Bicicleta: #classe
    def __init__(self, cor, modelo, ano, valor): #construtor
        #atributos da classe (são públicos, então os metódos get não são necessários)
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    # Métodos da classe

    def buzinar(self):
        print("plim plim...")
    
    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")
    
    def correr(self):
        print("Vruuummmmmmm...")

    def getcor(self): #não é muito usual
        return self.cor
    
    #----- Métodos para a representação de classe -----------
    #Método menos automatizado
    #metódo para exibir nossa instância de uma forma mais intuitiva
    '''
    def __str__(self): 
        return f"Bicicleta: {self.cor}, {self.modelo}, {self.ano}, {self.valor}"
    '''

    #Método mais automatizado
    def __str__(self):
        return f"{self.__class__.__name__}:{', '.join([f"{chave}={valor}" for chave, valor in self.__dict__.items()])}" 
    #(self.__class__.__name__)Um atributo do pyhton que permite acesso aos campos independente do nome da classe mudar
    # ', '.join([f"{chave}={valor}" for chave, valor in self.__dict__.items()]) -> Para printar os atributos
    #Fica mais automatizado, pois se aumentar os atributos, ele já reconheceria para a leitura.

b1 = Bicicleta("Azul", "caloi", 2024, 600)
b1.correr()
b1.buzinar()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("verde", "monark", 2000, 200)
Bicicleta.buzinar(b2) #Assim funciona, mas bicicleta.buzinar() falha, pois ele precisa da instancia b2

# Bicicleta.buzinar(b2) é equivalente a b2.buzinar()

#Como temos o método __str__ podemos vizualizar melhor colocando a seguinte linha
print(b1)
print(b2)
