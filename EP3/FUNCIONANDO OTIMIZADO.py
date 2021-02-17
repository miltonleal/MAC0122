#Nome: Milton Leal Neto
# NUSP: 8973974
# Exercício Programa III – 13/12/2020

def cria_lista_original():

    while True:

        #Solicita o nome dos arquivos
        arquivo = input("\nEntre com o nome do arquivo: ") #pede ao usuário nome do arquivo de entrada
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
                    v = linha.rstrip('\n').split(',')  # variável que recebe a linha acima e a transforma e
                    lista_original.append(v)

                except:
                    pass

            # print("lista separada", lista_original)
            return lista_original

def separa_nome(original):

    lista_nomes_separados = []
    for i in range(len(original)):
        lista_nomes_separados.append(original[i][1].lower().split())
    #print("lista_nomes_separados",lista_nomes_separados)

    return lista_nomes_separados

def prime(n):
    next_prime = n + 1
    prime = True
    while True:
        for i in range(2, next_prime):
            if next_prime%i ==0:
                prime = False
                break
        if prime:
            return next_prime
        else:
            next_prime = next_prime + 1
            if next_prime % 2 == 0:
                next_prime = next_prime + 1
            prime = True

def hashh(elemento, var):
    return elemento % var

def hash2():
    return 17

def insere_hash(tab_hash_empty,nomes_sep):

    #cont = 0

    for p in range(len(nomes_sep)):

        for q in range (4):

            s = 0
            # s conterá a soma dos valores numéricos dos caracteres

            for letter in nomes_sep[p][q]:

                s = s + ord(letter)

            i = hashh(s, prime(len(tab_hash_empty)))
            #print("i =", i)
            k = hash2()

            # procura a próxima posição livre
            while tab_hash_empty[i] is not None:
                #print("olá")
                i = (i + k) % len(tab_hash_empty)  # tabela circular
                #print(i)
            # achamos uma posição livre - coloque x nesta posição
            tab_hash_empty[i] = nomes_sep[p][q].lower(), p
    return tab_hash_empty

def busca_hash(tabela_hash, elemento_buscado):

    s = 0
    # s conterá a soma dos valores numéricos dos caracteres

    for letter in elemento_buscado:
        s = s + ord(letter)

    lista_indices_print = []
    cont = 0
    i = hashh(s, prime(len(tabela_hash)))
    k = hash2()

    while True:

        cont += 1
        if tabela_hash[i] is None:
            #cont += 1
            break

        cont += 1
        if tabela_hash[i][0] == elemento_buscado and tabela_hash[i][1] not in lista_indices_print:
            lista_indices_print.append(tabela_hash[i][1])

        i = (i + k) % len(tabela_hash)  # tabela circular

    return lista_indices_print, cont

def main ():

    print("\n*** Busca em tabela com duplo hash ***")

    lista_original = cria_lista_original()
    print("lista original",lista_original)

    nomes_separados = separa_nome(lista_original)
    print("nomes separados", nomes_separados)

    if len(lista_original) < 60:

        tab_hash_vazia = [None] * prime((16 * len(nomes_separados)))

    elif len(lista_original) >= 60:
        tab_hash_vazia = [None] * prime((8 * len(nomes_separados)))

    print("tabela hash vazia", tab_hash_vazia)
    tabela_hash = insere_hash(tab_hash_vazia,nomes_separados)
    print("tabela hash", tabela_hash)

    while True:

        buscado = input("\nEntre com um valor: ")
        buscado = buscado.lower()
        if buscado.lower() == "fim":
            break
        lista_indice_print, comparacoes = busca_hash(tabela_hash,buscado)

        if not lista_indice_print:
            print("\nValor não encontrado na tabela")
            print("Número de comparações: ", comparacoes)

        else:

            print()
            for r in range(len(lista_indice_print)):
                print('%s' % ','.join(map(str,lista_original[lista_indice_print[r]])))
            print("\n***", comparacoes,"comparações para localizar os nomes")

main()







