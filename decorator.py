def meu_decorator(fat):
    def fat(x):
        total, c = x, x
        
        for c in range(x - 1, 1, -1):
            total *= c

        # funcao(x)
        return(total)
        
    return fat
    

@meu_decorator
def dobro(x):
    return 2 * x



print(dobro(27))