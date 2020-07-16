def obter_mais_longa_substring(s):
    '''
    s: string que será passada
    
    Essa função retorna a mais longa substring de texto em ordem alfabética.
    '''
    maior_substring = '' #Conterá a maior substring
    caractere = s[0] #Pega a primeira letra da string s para iniciar as comparações
    substring = '' #Conterá as substrings
    for letra in s[1::]: #Faz iteração em cada letra da string s começando no segundo elemento
        if caractere <= letra: #Compara para ver se caract é menor (vem antes no alfabeto) do que a próxima letra da string (contida em x)
            if substring == '': #Se caract vier antes de x,  verifica se a variável substring está vazia
                substring += caractere + letra #Se estiver, adiciona caract e x a variál substring
            else:
                substring += letra #Se já contiver algo, só x será adicionado
        else: #Se caract foi maior que x...
            if len(substring) > len(maior_substring): #Verifica se a substring encontrada agora é maior que a anterior
                maior_substring = substring #Se for, troca a antiga pela nova
            substring = '' #Limpa a variável
            
        caractere = letra #Atualiza a variavel caract com a próxima letra da string s (contido em x)
    
    return maior_substring #retorna a maior substring






palavra = input("Insira a sua sequência de caracteres: ")


print(obter_mais_longa_substring(palavra))