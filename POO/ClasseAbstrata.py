from abc import ABCMeta, abstractmethod


class IAnimal(metaclass=ABCMeta):

    @abstractmethod
    def andar(self):
        pass


class Cachorro(IAnimal):

    def andar(self):
        print("Eu andei")



rex = Cachorro()
rex.andar()