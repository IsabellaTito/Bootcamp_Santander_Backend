class Animal:
    def __init__(self,num_patas):
        self.num_patas = num_patas
    
    def __str__(self):
        return f"{self.__class__.__name__}:{', '.join([f"{chave}={valor}" for chave, valor in self.__dict__.items()])}" 
    
class Mamifero(Animal):
    def __init__(self, cor_pelo,**kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw) #Esse trecho pega os argumentos da classe pai
        #super().__init__(num_patas = kw["num_patas"]) #Esse é mais limitado
    
    def __str__(self):
        return "Mamifero"

class Ave(Animal):
    def __init__(self, cor_bico,**kw):
         self.cor_bico = cor_bico
         super().__init__(**kw) #melhor, pois qualquer novo atributo ele identifica
    
    def __str__(self):
        return "ave 42"

class Cachorro(Mamifero):
     pass

class Gato(Mamifero):
     pass

class Leao(Mamifero):
     pass

class Ornitorrinco(Mamifero,Ave):
    def __init__(self, cor_bico, cor_pelo, num_patas):
        #print(Ornitorrinco.__mro__) 
        # ou
        # print(Ornitorrinco.mro()) 
        # tras a ordem de resolução para encontrar os atributos e métodos
        super().__init__(cor_pelo = cor_pelo,cor_bico=cor_bico,num_patas = num_patas)

    def __str__(self):
        return "Ornitorrinco"

gato = Gato(num_patas = 4,cor_pelo="laranja")
print(gato)

#utilizar o kw faz com que os argumentos sejam passados de forma nomeada, não mais posicional como abaixo
''' 
pery = Ornitorrinco(2,"verde","laranja")
print(pery)
'''

pery = Ornitorrinco(num_patas = 2,cor_pelo="verde", cor_bico = "laranja")
print(pery)