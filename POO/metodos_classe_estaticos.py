class Pessoa:
    def __init__(self,nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"nome: {self.nome} \nidade: {self.idade}"
    
    @classmethod #Decorador que transforma a função em um método de classe
    #Métodos de classe usam cls ao invés do self
    def criar_de_data_nascimento(cls, ano, nome):
        idade = 2025 - ano
        return Pessoa(nome,idade)
    
    @staticmethod 
    def e_maior_idade(idade):
        return idade >= 18



'''
Depois de fazer o classmethod, eu não preciso fazer da seguinte forma
p = Pessoa().criar_de_data_nascimento(2000,"Isabella")
Aqui ocorrem duas instanciações, em p=Pessoa() e no return da função
Com a classmethod isso não ocorre e fica da seguinte forma
'''

p = Pessoa.criar_de_data_nascimento(2000,"Isabella")
print(p)

print(Pessoa.e_maior_idade(15))
print(Pessoa.e_maior_idade(21))

'''
Preciso ter o contexto da classe? Método de classe
Não preciso nem do contexto, nem de classe, nem da instancia do objeto? metodo estático
'''