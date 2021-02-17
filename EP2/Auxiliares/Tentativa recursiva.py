import time

def transforma_data (matrix):

    for i in range(len(matrix)):
        data = matrix[i][2].split("/")
        matrix[i][2] = data
        matrix[i][2][0], matrix[i][2][2] = matrix[i][2][2], matrix[i][2][0]
        matrix[i][2] = matrix[i][2][0] + "/" + matrix[i][2][1] + "/" + matrix[i][2][2]

    return matrix


def QuickSort (lista, ordem, inicio = 0, fim = None):

    if fim is None:
        fim = len(lista)-1
    if inicio < fim:
        p = partition(lista, inicio, fim, ordem)
        QuickSort(lista, ordem, inicio, p - 1)
        QuickSort(lista,ordem, p + 1, fim)

    return lista


def partition (lista, inicio, fim, ordem):

    pivot = lista[fim]
    i = inicio
    #print(pivot)

    for j in range (inicio, fim):


        if lista[j][ordem[0]] < pivot[ordem[0]]:
            lista[j], lista[i] = lista[i], lista[j]

            i = i + 1

        if lista[j][ordem[0]] == pivot[ordem[0]] and len(ordem) == 2:
            if lista[j][ordem[1]] < pivot[ordem[1]]:
                #lista[fim], lista[j] = lista[j], lista[fim]

                i = i+1

        if lista[j][ordem[0]] == pivot[ordem[0]] and len(ordem) == 3:
            if lista[j][ordem[1]] < pivot[ordem[1]]:
                i = i + 1
            if lista[j][ordem[1]] == pivot[ordem[1]]:
                if lista[j][ordem[2]] < pivot[ordem[2]]:
                    i = i + 1
                if lista[j][ordem[2]] == pivot[ordem[2]]:
                    break




    lista[i], lista[fim], = lista[fim], lista[i]
    return i

while True:

    arquivo_entrada = input("Entre com o nome do arquivo de entrada: ") #pede ao usuário nome do arquivo de entrada
    if arquivo_entrada.lower() == "fim": #se usuário digitar "fim", termina o programa
        quit()

    arquivo_saida = input("\nEntre com o nome do arquivo de saída: ") #pede ao usuário nome do arquivo de saída
    if arquivo_saida.lower() == "fim":  # se usuário digitar "fim", termina o programa
        quit()

    while True:

        while True:

            ordem = input("\nInsira a ordem de classificação dos valores: ")
            if ordem.lower() == "fim":  # se usuário digitar "fim", termina o programa
                quit()

            lista_ordem = ordem.split(',')

            lista_ordem_int = list(map(int, lista_ordem))

            set_ordem = set(lista_ordem_int)

            try:
                if set_ordem <= {0, 1, 2}:
                    break
                else:
                    print("\nErro! Insira a ordem de clasificação corretamente. Exemplo: 1 ou 1,2 ou 0,2,3\n")
                    continue
            except:
                pass
        #PRINT INTERMEDIARIO
        print("Classificação da Ordem", lista_ordem_int)

        try:
            with open(arquivo_entrada, "r") as arq: #abre o arquivo

                linhas = arq.readlines()  #retorna uma lista que contém cada linha do arquivo como um item da lista

        except:
            print("\nErro na abertura do arquivo de entrada. Insira novamente o nome do arquivo.\n")
            break

        lista_separada = []
        for linha in linhas: #lê cada linha da lista "linhas"

            try:
                lin = linha[:len(linha) - 1]  # variável que recebe cada linha do arquivo de texto original como uma string
                v = linha.rstrip('\n').split(',')  # variável que recebe a linha acima e a transforma e
                lista_separada.append(v)

            except: pass

        ####### CHAMADA QUICK
        print("Quick", transforma_data(QuickSort(transforma_data(lista_separada), lista_ordem_int)))
        start = time.process_time()
        final2 = transforma_data(QuickSort(transforma_data(lista_separada), lista_ordem_int))
        print("Quick time = ", time.process_time() - start)
        ########


        ######## CHAMADA BOLHA
        #print("Bolha", transforma_data(Bubble(transforma_data(lista_separada), lista_ordem_int)))
        #start = time.process_time()
        #final = transforma_data(Bubble(transforma_data(lista_separada), lista_ordem_int))
        #print("Bubble time = ", time.process_time() - start)
        #########


        #with open(arquivo_saida, 'w') as filehandle:
            #for listitem in final:
                #filehandle.write('%s\n' % listitem)

        #with open(arquivo_saida, 'w') as filehandle:
            #for listitem in final2:
                #filehandle.write('%s\n' % listitem)

        break
