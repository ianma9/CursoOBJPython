from abc import ABCMeta, abstractmethod

class Animal(metaclass = ABCMeta):
    @abstractmethod
    def som(self):
        pass

class Cachorro(Animal):
    def som(self):
        print('au au au')

class Gato(Animal):
    def som(self):
        print('miau miau')

class Factory(object):
    def produzir_som(self, object_type):
        return eval(object_type)().som()


if __name__ == '__main__':
    f = Factory()
    f.produzir_som('Gato')
    f.produzir_som('Cachorro')