''' Criação da instancia unica '''

class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

s1 = Singleton()
print(s1)
s2 = Singleton()
print(s2)


''' Lazy Singleton '''
class LazySingleton:
    __instance = None
    def __init__(self):
        if not LazySingleton.__instance:
            print('__init foi chamado')
        else:
            print('instancia ja foi criada', self.obter_instancia())

    @classmethod
    def obter_instancia(cls):
        if not cls.__instance:
            cls.__instance = LazySingleton()
        return cls.__instance


s3 = LazySingleton()
print('Objeto criado ', LazySingleton.obter_instancia())
s4 = LazySingleton()


''' Singleton Monostate '''


class MinhaClasse:
    __estado_compartilhado = {'1':2}
    def __init__(self):
        self.x = 1
        self.__dict__ = self.__estado_compartilhado

b1 = MinhaClasse()
b2 = MinhaClasse()
b1.x = 5

print('b1 ', b1)
print('b2 ', b2)

print(b1.__dict__)
print(b1.__dict__)