class Pessoa():

    """ Existem apenas dois modos de acesso: público e privado.
        O privado utiliza dois underscores "__" no inicio do atributo.

        As definições de getter e setter em python são de acordo com o exemplo abaixo:
    """

    
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, idade):
        if idade >= 18:
            self.__idade = idade



p = Pessoa('Ian', 20)
print(p.nome)
print(p.idade)

p.idade = 16
print(p.idade)
print(dir(Pessoa))