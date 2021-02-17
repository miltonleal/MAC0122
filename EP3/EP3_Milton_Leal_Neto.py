#Nome: Milton Leal Neto
# NUSP: 8973974
# Exercício Programa III – 13/12/2020

def cria_lista_original(): #função que cria a tabela original dos dados

    while True:

        #Solicita o nome do arquivo de entrada
        arquivo = input("\nEntre com o nome do arquivo: ")
        if arquivo.lower() == "fim": #se usuário digitar "fim", termina o programa
            quit()

        while True:

            # tenta abrir o arquivo de entrada
            try:
                with open(arquivo, "r") as arq:  # abre o arquivo

                    linhas = arq.readlines()  # retorna uma lista que contém cada linha do arquivo como um item da lista
            except:
                print("\nErro na abertura do arquivo de entrada. Insira novamente o nome do arquivo.")
                break

            lista_original = []  # cria lista para receber o conteúdo da lista original
            for linha in linhas:  # lê cada linha da lista "linhas"
                try:
                    lin = linha[
                          :len(linha) - 1]  # variável que recebe cada linha do arquivo de texto original como uma string
                    v = linha.rstrip('\n').split(',')  # separa o conteúdo pela vírgula
                    lista_original.append(v)
                except:
                    pass
            return lista_original

def separa_nome(original): # cria lista com os nomes e sobrenomes separados

    lista_nomes_separados = [] #cria lista para receber os nomes separados
    for i in range(len(original)):
        lista_nomes_separados.append(original[i][1].lower().split()) #splita de acordo com o espaço
    return lista_nomes_separados

def proximo_primo(n): #função que devolve o próximo número primo a partir de um número n
    prox_primo = n + 1 #estabelece como possível próximo primo o número seguinte a n
    primo = True
    while True:
        for i in range(2, prox_primo):
            if prox_primo%i ==0: #verifica se é primo
                primo = False
                break
        if primo: # se for primo, retorn
            return prox_primo
        else: #se não for primo, continua procurando
            prox_primo = prox_primo + 1
            if prox_primo % 2 == 0:
                prox_primo = prox_primo + 1
            primo = True

def hash1(elemento,tab_hash): #função de hash
    #módulo entre o elemento e próximo primo em relação ao tamanho da tabela hash // 2
    return elemento % proximo_primo(len(tab_hash)//2)

def hash2(): #função do hash duplo
    return 17 #passo

def insere_hash(tab_hash_vazia,nomes_sep): #insere os elementos na tabela vazia de acordo com o hash

    for p in range(len(nomes_sep)): #varre os elementos da lista de nomes separados

        for q in range(len(nomes_sep[p])): #varre cada um dos nomes dos elementos da lista de nomes separados

            # s conterá a soma dos valores numéricos dos caracteres
            s = 0 #inicia a soma do valor do nome

            for letra in nomes_sep[p][q]:
                s = s + ord(letra) #soma os valores das letras de acordo com a tabela ASCII

            #determina o índice do hash
            i = hash1(s, tab_hash_vazia)
            #faz o hash duplo
            k = hash2()

            # procura a próxima posição livre
            while tab_hash_vazia[i] is not None:
                i = (i + k) % len(tab_hash_vazia)  # tabela circular

            # achamos uma posição livre - coloque x nesta posição
            tab_hash_vazia[i] = nomes_sep[p][q].lower(), p

    return tab_hash_vazia

def busca_hash(tabela_hash,elemento_buscado): #realiza a busca na tabela de acordo com o hash

    # s conterá a soma dos valores numéricos dos caracteres
    s = 0 #inicia a soma do valor do nome

    for letra in elemento_buscado:
        s = s + ord(letra) #soma os valores das letras de acordo com a tabela ASCII

    # cria uma lista para receber os índices da tabela original associados ao hash
    lista_indices_print = []

    # inicia o contador de comparações
    cont = 0

    # determina o índice do hash
    i = hash1(s, tabela_hash)
    # faz o hash duplo
    k = hash2()


    while True:

        if tabela_hash[i] is None: #se encontrar um elemento None é porque não existe ou a busca terminou
            break

        cont += 1
        #se o elemento na tabela hash for igual ao buscado e o índice associado ainda não estiver
        #na lista de índices, append na lista de indices
        if tabela_hash[i][0] == elemento_buscado and tabela_hash[i][1] not in lista_indices_print:
            lista_indices_print.append(tabela_hash[i][1])

        i = (i + k) % len(tabela_hash)  # tabela circular

    return lista_indices_print, cont

def main (): #programa principal

    print("\n*** Busca em tabela com duplo hash ***")

    lista_original = cria_lista_original() #cria a lista original

    nomes_separados = separa_nome(lista_original) #separa os nomes e sobrenomes

    #cria uma tabela vazia com um número de 2 x tamanho original da tabela x 4 nomes por elemento
    #ou seja, temos uma tabela vazia 8 vezes maior que a tabela inicial, devido à separação dos nomes e sobrenomes
    tab_hash_vazia = [None] * proximo_primo((8 * len(nomes_separados)))

    tabela_hash = insere_hash(tab_hash_vazia,nomes_separados) #insere os nomes na tabela hash

    while True: #loop principal

        buscado = input("\nEntre com um valor: ") #usuário insere elemento a ser buscado
        buscado = buscado.lower() #transforma elemento em caixa baixa
        if buscado.lower() == "fim":
            break

        #chamada principal do programa
        lista_indice_print, comparacoes = busca_hash(tabela_hash,buscado)

        #se o elemento não estiver na tabela original
        if not lista_indice_print:
            print("\nValor não encontrado na tabela")

        else:
            print()
            #se o elemento estiver na tabela, printa as linhas da tabela original
            for r in range(len(lista_indice_print)):
                print('%s' % ','.join(map(str,lista_original[lista_indice_print[r]])))
            print("\n***", comparacoes,"comparações para localizar os nomes")

main()







