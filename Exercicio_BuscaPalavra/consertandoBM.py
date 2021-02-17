# Nome: Milton Leal neto
# NUSP: 8973974
# Exercício V – 23/12/2020

def BoyerMoore1(a, b):

    nvezes = 0 #inicia contador de igualdades na busca
    ndesloc = 1 #inicia contador dos deslocamentos

    lista_ultimas_ocorrencias = [-1] * 256 #tabela de últimas ocorrências de cada caractere em "a

    for i in range(len(a)): #varre "a" e define últimas ocorrências de cada caractere
        lista_ultimas_ocorrencias[ord(a[i])] = i #agrega à lista as devidas ocorrências

    ponteiro_b = len(a) - 1 #define ponteiro_b como tamanho de "a" - 1

    while ponteiro_b < len(b): # enquanto o ponteiro não chegar no último elemento de b

        #define e inicia ponteiro_b_auxiliar e ponteiro_a como tamanho de "a" - 1
        ponteiro_b_auxiliar = ponteiro_b
        ponteiro_a = len(a) - 1

        while ponteiro_a >= 0: #enquanto não terminar de verificar "a"

            if a[ponteiro_a] != b[ponteiro_b_auxiliar]: #se os caracteres forem diferentes
                break

            # se os caracteres forem iguais
            ponteiro_b_auxiliar -= 1
            ponteiro_a -= 1

        if ponteiro_a < 0: #se chegou aqui, é porque existe "a" em "b"
            nvezes += 1 #contabiliza uma igualdade

        # caso particular - se ponteiro_b_auxliar é n-1 (último de b)
        if ponteiro_b + 1 >= len(b):
            break

        # desloca baseado no valor de b[ponteiro_b_auxiliar + 1]
        ponteiro_b = ponteiro_b + len(a) - lista_ultimas_ocorrencias[ord(b[ponteiro_b + 1])]

        if ponteiro_b >= len(b):
            break

        ndesloc += 1 #contabiliza um deslocamento

    return nvezes,ndesloc

def Desloc(a): #função auxiliar para o algoritmo Adaptado

    tabela_deslocamentos = [] #incia a tabela de deslocamentos como vazia

    #dois for encaixados para varrer os elementos
    for t in range (len(a)-1, -1, -1):

        for p in range(t, -1,-1):

            if a[t] != a[p]: #se os elementos forem diferentes
                tabela_deslocamentos.append(t-p) #appenda a diferença entre os índices
                break

            if t == 0 and p == 0: #se chegar no último elemento da direita para esquerda, apenda 1 na tabela
                tabela_deslocamentos.append(1)

    if len(tabela_deslocamentos) != len(a): #caso particular, caso não existam caracteres diferentes em "a"
        tabela_deslocamentos = [1] * len(a)

    tabela_deslocamentos.reverse() #inverte a ordem da tabela para facilitar a leitura do algoritmo de busca

    return tabela_deslocamentos

def Adaptado(a,b):

    nvezes = 0 #inicia contador de igualdades na busca
    ndesloc = 1 #inicia contador dos deslocamentos

    ponteiro_b = len(a)-1 #define ponteiro_b como tamanho de "a" - 1

    deslocamentos = Desloc(a) #guarda a lista de deslocamentos na variável deslocamentos

    while ponteiro_b < len(b): # enquanto o ponteiro não chegar no último elemento de b

        # define e inicia ponteiro_b_auxiliar e ponteiro_a como tamanho de "a" - 1
        ponteiro_b_auxiliar = ponteiro_b
        ponteiro_a = len(a) - 1

        while ponteiro_a >= 0: #enquanto não terminar de verificar "a"

            if a[ponteiro_a] != b[ponteiro_b_auxiliar]:  #se os caracteres forem diferentes
                ponteiro_b += deslocamentos[ponteiro_a] #acrescenta ao ponteiro_b o número de deslocamentos
                ndesloc += 1 #contabiliza um deslocamento
                break

            else: #se os caracteres de a e b forem iguais
                ponteiro_a -= 1 #diminui um do ponteiro do a
                ponteiro_b_auxiliar -= 1 #diminui um do ponteiro_b_auxiliar

        if ponteiro_a < 0: #se todos os caracteres forem iguais

            ponteiro_b += 1 #desloca o ponteiro b uma unidade à direita
            nvezes += 1 #contabiliza uma igualdade

    return nvezes,ndesloc