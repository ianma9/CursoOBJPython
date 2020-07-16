class SomentePares(list):

    def append(self, inteiro):
        if not isinstance(inteiro, int):
            raise TypeError('Somente números inteiros')
        if inteiro % 2:
            raise ValueError('Somente números pares')

        super().append(inteiro)
    

lista = SomentePares()

lista.append(4)
lista.append(6)



