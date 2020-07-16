class Pessoa:
    nome = "Ian"
    
    def __init__(self, sobrenome):
        self.sobrenome = sobrenome


    def imprimirNome(self):
        print(self.nome + self.sobrenome)