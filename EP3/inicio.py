
def cria_lista_original():

    while True:

        #Solicita o nome dos arquivos
        arquivo = input("\nNome do arquivo de origem: ") #pede ao usuário nome do arquivo de entrada
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
        lista_nomes_separados.append(original[i][1].split())
    print("lista_nomes_separados",lista_nomes_separados)

    return lista_nomes_separados

def determina_variacao(nomes_separados):

    lista_valores_ascii = []
    for j in range (len(nomes_separados)):
        for i in range(4):
            s = 0
            # s conterá a soma dos valores numéricos dos caracteres

            for letter in nomes_separados[j][i]:
                #print(j)
                s = s + ord(letter)
            lista_valores_ascii.append(s)

    print("max=", max(lista_valores_ascii))
    print("min=", min(lista_valores_ascii))
    variation = ((max(lista_valores_ascii) - min(lista_valores_ascii)) + 1)

    return variation

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
    #print("elemento =", elemento)
    return elemento % var

def hash2():
    return 3

def insere_hash(tab_hash_empty,nomes_sep,var):

    #cont = 0

    for p in range(len(nomes_sep)):

        for q in range (4):

            s = 0
            # s conterá a soma dos valores numéricos dos caracteres

            for letter in nomes_sep[p][q]:

                s = s + ord(letter)

            i = hashh(s, var)
            print("i =", i)
            k = hash2()

            # procura a próxima posição livre
            while tab_hash_empty[i] is not None:
                #print("olá")
                i = (i + k) % len(tab_hash_empty)  # tabela circular
                #print(i)
            # achamos uma posição livre - coloque x nesta posição
            tab_hash_empty[i] = nomes_sep[p][q], p
    return tab_hash_empty

def busca_hash(tabela_hash, elemento_buscado, var):

    s = 0
    # s conterá a soma dos valores numéricos dos caracteres

    for letter in elemento_buscado:
        s = s + ord(letter)

    while True:
        lista_indices_print = []
        cont = 0
        i = hashh(s, var)
        k = hash2()

        if tabela_hash[i] is None:
            break

        while tabela_hash[i][0] == elemento_buscado and tabela_hash[i][1] not in lista_indices_print:
            lista_indices_print.append(tabela_hash[i][1])

            i = (i + k) % len(tabela_hash)  # tabela circular

            if tabela_hash[i] is None:
                break

        return lista_indices_print

    return -1

def main ():

    lista_original = cria_lista_original()

    nomes_separados = separa_nome(lista_original)

    tab_hash_vazia = [None] * prime((8 * len(nomes_separados)))

    hash_func = determina_variacao(nomes_separados)

    tabela_hash = insere_hash(tab_hash_vazia,nomes_separados,hash_func)

    print("tabela hash =",tabela_hash)

    while True:

        buscado = input("Insira o nome a ser buscado:")
        if buscado.lower() == "fim":
            break
        lista_indice_print = busca_hash(tabela_hash,buscado,hash_func)

        if lista_indice_print == -1:
            print("elemento não encontrado")

        else:
            for r in range(len(lista_indice_print)):
                print(lista_original[lista_indice_print[r]])
            break




main()







