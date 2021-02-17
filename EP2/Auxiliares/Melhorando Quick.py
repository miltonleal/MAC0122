import time

def transforma_data (matrix):

    for i in range(len(matrix)):
        data = matrix[i][2].split("/")
        matrix[i][2] = data
        matrix[i][2][0], matrix[i][2][2] = matrix[i][2][2], matrix[i][2][0]
        matrix[i][2] = matrix[i][2][0] + "/" + matrix[i][2][1] + "/" + matrix[i][2][2]

    return matrix

class Empty(Exception):
    pass

class PilhaLista:

#Pilha como uma lista
    # Construtor da classe PilhaLista
    def __init__(self):
        self._pilha = [] # lista que conterá a pilha

    # retorna o tamanho da pilha
    def __len__ (self):
        return len(self._pilha)

    def __str__(self):
        return str(self._pilha)

    # retorna True se pilha vazia
    def is_empty(self):
        return len(self._pilha) == 0

    # empilha novo elemento e
    def push(self, e):
        self._pilha.append(e)

        # retorna o elemento do topo da pilha sem retirá-lo
        # exceção se pilha vazia
    def top(self):
        if self.is_empty():
            raise Empty("Pilha vazia")
        return self._pilha[-1]

    # desempilha elemento
    # excessão se pilha vazia
    def pop(self):
        if self.is_empty():
            raise Empty("Pilha vazia")
        return self._pilha.pop( )

def Quick_Sort(lista, ordem):
    # Cria a pilha de sub-listas e inicia com lista completa
    Pilha = PilhaLista()
    Pilha.push((0, len(lista) - 1))
    # Repete até que a pilha de sub-listas esteja vazia
    while not Pilha.is_empty():
        inicio, fim = Pilha.pop()
        # Só particiona se há mais de 1 elemento
        if fim - inicio >= 0:
            k = partition(lista, inicio, fim, ordem)
            # Empilhe as sub-listas resultantes
            Pilha.push((inicio, k - 1))
            Pilha.push((k + 1, fim))
    return lista

def partition (lista, inicio, fim, ordem):

    #print(ordem)

    pivot = lista[fim]
    i,j = inicio, fim
    #print(pivot)

    if len(ordem) == 1:
        while True:
            ### i
            while i < j and lista[i][ordem[0]] <= pivot[ordem[0]]: i = i + 1
            if i < j:
                lista[i], lista[j] = pivot, lista[i]
                j = j-1
            else:
                break
            ### j
            while i < j and lista[j][ordem[0]] >= pivot[ordem[0]]: j = j + 1
            if i < j:
                lista[i], lista[j] = lista[j], pivot
                i = i - 1
            else:
                break
        return i

    if len(ordem) == 2:
        while True:
            ### i
            while i < j:
                if lista[i][ordem[0]] < pivot[ordem[0]]: i = i + 1
                if i < j:
                    lista[i], lista[j] = pivot, lista[i]
                    j = j-1
                else:
                    break
                if lista[i][ordem[0]] == pivot[ordem[0]]:
                    if lista[i][ordem[1]] < pivot[ordem[1]]: i = i + 1
                    if i < j:
                        lista[i], lista[j] = pivot, lista[i]
                        j = j - 1
                    else:
                        break
                    if lista[i][ordem[1]] == pivot[ordem[1]]:
                        break
            ### j
            while i < j:
                if lista[j][ordem[0]] > pivot[ordem[0]]: j = j + 1
                if i < j:
                    lista[i], lista[j] = lista[j], pivot
                    i = i-1
                else:
                    break
                if lista[j][ordem[0]] == pivot[ordem[0]]:
                    if lista[j][ordem[1]] < pivot[ordem[1]]: j = j + 1
                    if i < j:
                        lista[i], lista[j] = lista[j], pivot
                        i = i - 1
                    else:
                        break
                    if lista[j][ordem[1]] == pivot[ordem[1]]:
                        break
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
        #print("Quick", transforma_data(Quick_Sort(transforma_data(lista_separada), lista_ordem_int)))
        #a = transforma_data(lista_separada)
        #start = time.process_time()

        #final2 = transforma_data(Quick_Sort(transforma_data(lista_separada), lista_ordem_int))
        #final2 = (Quick_Sort(a, lista_ordem_int))
        #print("Quick time = ", time.process_time() - start)
        #b = transforma_data(final2)
        ########
        print("oi")


        ######## CHAMADA BOLHA
        #print("Bolha", transforma_data(Bubble(transforma_data(lista_separada), lista_ordem_int)))
        #start = time.process_time()
        #final = transforma_data(Bubble(transforma_data(lista_separada), lista_ordem_int))
        #print("Bubble time = ", time.process_time() - start)
        #########

        #if transforma_data(Bubble(transforma_data(lista_separada), lista_ordem_int)) == transforma_data(Quick_Sort(transforma_data(lista_separada), lista_ordem_int)):
            #print("iguais")

        #with open(arquivo_saida, 'w') as filehandle:
            #for listitem in final:
                #filehandle.write('%s\n' % listitem)

        #with open(arquivo_saida, 'w') as filehandle:
            #for listitem in final2:
                #filehandle.write('%s\n' % listitem)

        break

#main()