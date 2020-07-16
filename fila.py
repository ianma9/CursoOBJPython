import heapq

class FilaDePrioridade:
    
    def __init__(self):
        self.fila = []
        self.indice = 0

    def inserir(self, item, prioridade):
        heapq.heappush(self.fila, (-prioridade, self.indice, item))
        self.indice =+ 1

    def remover(self):
        return heapq.heappop(self.fila)[-1]



class Item:

    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return self.nome



fila = FilaDePrioridade()
fila.inserir(Item('Ian'), 19)
fila.inserir(Item('Ikaro'), 16)
fila.inserir(Item('Clautenes'), 41)


print(fila.remover())
print(fila.remover())