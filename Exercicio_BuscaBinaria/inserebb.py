# Nome: Milton Leal neto
# NUSP: 8973974
# Exercício IV – 06/12/2020

def BuscaBinaria(TAB,V): #realiza a busca binária da posição que será incluído o novo elemento

    count = 0 #conta o número de comparações
    n = len(TAB)

    # se o elemento V a ser inserido estiver fora da tabela
    count += 1 #conta as comparações
    if V <= TAB[0]: #caso V seja menor que o primeiro elemento
        return 0, count #retorna índice 0 e 1 comparação

    count += 1 #conta as comparações
    if V > TAB[n-1]: #caso V seja maior que o último elemento
        return n, count #retorna índice n e 1 comparação

    # se o elemento V estiver dentro da tabela
    start = 0 #inicia variável com o primeiro índice
    end = n-1 #inicia variável com o último índice

    while end - start > 1:
        count += 1 #conta as comparações
        middle = (end + start) // 2 #encontra o meio da tabela
        if V <= TAB[middle]: end = middle #se V for menor que o meio, o fim passa a ser o meio
        else: start = middle #senão, o começo passa a ser o meio

    return end, count #retorna o índice e o número de comparações

def InsereBB(TAB,V): #função que insere o novo elemento na tabela ordenada

    j, count = BuscaBinaria(TAB,V) #guarda nas variáveis o índice e o total de comparações

    TAB[:] = TAB[:j] + [V] + TAB[j:] #inclui V na tabela

    return j, count




