#Nome: Milton Leal Neto
# NUSP: 8973974
# Exercício Programa II – 22/11/2020

import time

def transforma_data (matrix):

    for i in range(len(matrix)):
        data = matrix[i][2].split("/")
        matrix[i][2] = data
        matrix[i][2][0], matrix[i][2][2] = matrix[i][2][2], matrix[i][2][0]
        matrix[i][2] = matrix[i][2][0] + "/" + matrix[i][2][1] + "/" + matrix[i][2][2]

    return matrix

def Bubble(matrix, order):

    n = len(matrix)

    for i in range(1, n):

        j = i
        while j > 0:

            if matrix[j][order[0]] < matrix[j - 1][order[0]]:
                matrix[j], matrix[j - 1] = matrix[j - 1], matrix[j]
                j = j - 1
                continue

            elif matrix[j][order[0]] == matrix[j - 1][order[0]] and len(order) != 1:

                if len(order) == 2:

                    if matrix[j][order[1]] < matrix[j-1][order[1]]:
                        matrix[j], matrix[j - 1] = matrix[j - 1], matrix[j]
                        j = j - 1

                    elif matrix[j][order[1]] >= matrix[j - 1][order[1]]:
                        break

                if len(order) == 3:

                    if matrix[j][order[1]] < matrix[j-1][order[1]]:
                        matrix[j], matrix[j - 1] = matrix[j - 1], matrix[j]
                        j = j - 1

                    elif matrix[j][order[1]] == matrix[j-1][order[1]]:

                        if matrix[j][order[2]] < matrix[j-1][order[2]]:
                            matrix[j], matrix[j - 1] = matrix[j - 1], matrix[j]
                            j = j - 1

                        elif matrix[j][order[2]] >= matrix[j - 1][order[2]]:
                            break

                    elif matrix[j][order[1]] >= matrix[j - 1][order[1]]:
                        break

            elif matrix[j][order[0]] >= matrix[j - 1][order[0]]:
                break

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
    #print(i,j)
    #print(pivot)

    while True:
        if len(ordem) == 1:
            #print("oi")

            ### i
            while i < j and lista[i][ordem[0]] <= pivot[ordem[0]]: i = i + 1
            if i < j:
                lista[i], lista[j] = pivot, lista[i]
                j = j - 1
            else:
                break
            ### j
            while i < j and lista[j][ordem[0]] >= pivot[ordem[0]]: j = j - 1
            if i < j:
                lista[i], lista[j] = lista[j], pivot
                i = i + 1
            else:
                break


        if len(ordem) == 2:

            ### i
            while i < j:
                if lista[i][ordem[0]] < pivot[ordem[0]]:
                    i = i + 1

                elif lista[i][ordem[0]] == pivot[ordem[0]] and \
                    lista[i][ordem[1]] <= pivot[ordem[1]]:
                    i = i + 1
                else:
                    break

            if i < j:
                lista[i], lista[j] = pivot, lista[i]
                j = j - 1
            else:
                break

            ### j
            while i < j:
                if lista[j][ordem[0]] > pivot[ordem[0]]:
                    j = j - 1

                elif lista[j][ordem[0]] == pivot[ordem[0]] and \
                    lista[j][ordem[1]] >= pivot[ordem[1]]:
                    j = j - 1
                else:
                    break

            if i < j:
                lista[i], lista[j] = lista[j], pivot
                i = i + 1
            else:
                break

        if len(ordem) == 3:

            ### i
            while i < j:
                if lista[i][ordem[0]] < pivot[ordem[0]]:
                    i = i + 1

                elif lista[i][ordem[0]] == pivot[ordem[0]] and \
                    lista[i][ordem[1]] < pivot[ordem[1]]:
                    i = i + 1

                elif lista[i][ordem[0]] == pivot[ordem[0]] and \
                    lista[i][ordem[1]] == pivot[ordem[1]] and \
                    lista[i][ordem[2]] <= pivot[ordem[2]]:
                    i = i + 1
                else:
                    break

            if i < j:
                lista[i], lista[j] = pivot, lista[i]
                j = j - 1
            else:
                break

            ### j
            while i < j:
                if lista[j][ordem[0]] > pivot[ordem[0]]:
                    j = j - 1

                elif lista[j][ordem[0]] == pivot[ordem[0]] and \
                    lista[j][ordem[1]] > pivot[ordem[1]]:
                    j = j - 1

                elif lista[j][ordem[0]] == pivot[ordem[0]] and \
                    lista[j][ordem[1]] == pivot[ordem[1]] and \
                    lista[j][ordem[2]] >= pivot[ordem[2]]:
                    j = j - 1
                else:
                    break

            if i < j:
                lista[i], lista[j] = lista[j], pivot
                i = i + 1
            else:
                break
    return i

def main():

    print("*** CLASSIFICADOR DE TABELAS ***")
    while True:

        arquivo_entrada = input("\nNome do arquivo de origem: ") #pede ao usuário nome do arquivo de entrada
        if arquivo_entrada.lower() == "fim": #se usuário digitar "fim", termina o programa
            quit()

        arquivo_saida1 = input("\nNome do arquivo de destino 1: ") #pede ao usuário nome do arquivo de saída
        if arquivo_saida1.lower() == "fim":  # se usuário digitar "fim", termina o programa
            quit()

        arquivo_saida2 = input("\nNome do arquivo de destino 2: ")  # pede ao usuário nome do arquivo de saída
        if arquivo_saida2.lower() == "fim":  # se usuário digitar "fim", termina o programa
            quit()

        while True:

            while True:

                ordem = input("\nInsira a ordem de classificação dos valores: ")
                if ordem.lower() == "fim":  # se usuário digitar "fim", termina o programa
                    quit()

                lista_ordem = ordem.split(',')

                set_ordem = set(lista_ordem)

                try:
                    if set_ordem <= {"0", "1", "2"}:
                        break
                    else:
                        print("\nErro! Insira a ordem de clasificação corretamente. Exemplo: 1 ou 1,2 ou 0,2,3")
                        continue
                except:
                    pass

            lista_ordem_int = list(map(int, lista_ordem))

            #PRINT INTERMEDIARIO

            try:
                with open(arquivo_entrada, "r") as arq: #abre o arquivo

                    linhas = arq.readlines()  #retorna uma lista que contém cada linha do arquivo como um item da lista

            except:
                print("\nErro na abertura do arquivo de entrada. Insira novamente o nome do arquivo.")
                break

            print("\nOrdem de classificação:", ','.join(map(str, lista_ordem_int)))

            lista_separada = []
            for linha in linhas: #lê cada linha da lista "linhas"

                try:
                    lin = linha[:len(linha) - 1]  # variável que recebe cada linha do arquivo de texto original como uma string
                    v = linha.rstrip('\n').split(',')  # variável que recebe a linha acima e a transforma e
                    lista_separada.append(v)

                except: pass

            lista_bubble = lista_separada.copy()
            lista_quick = lista_separada.copy()

            ####### CHAMADA QUICK
            #print("Quick", transforma_data(Quick_Sort(transforma_data(lista_separada), lista_ordem_int)))

            if 2 not in lista_ordem_int:
                start = time.process_time()
                b_quick = Quick_Sort(lista_quick, lista_ordem_int)
                print("Tempo de classificação - Quick Sort (Hoare) = ", time.process_time() - start)

            else:
                a_quick = transforma_data(lista_quick)
                start = time.process_time()
                aux_quick = Quick_Sort(a_quick, lista_ordem_int)
                print("Tempo de classificação - Quick Sort (Hoare) = ", time.process_time() - start)
                b_quick = transforma_data(aux_quick)
            ########


            ######## CHAMADA BOLHA
            # print("Bolha", transforma_data(Bubble(transforma_data(lista_separada), lista_ordem_int)))

            if 2 not in lista_ordem_int:
                start = time.process_time()
                b_bubble = Bubble(lista_bubble, lista_ordem_int)
                print("Tempo de classificação - Bolha = ", time.process_time() - start)

            else:
                a_bubble = transforma_data(lista_bubble)
                start = time.process_time()
                aux_bubble = (Bubble(a_bubble, lista_ordem_int))
                print("Tempo de classificação - Bolha = ", time.process_time() - start)
                b_bubble = transforma_data(aux_bubble)

            with open(arquivo_saida1, 'w') as filehandle:
                filehandle.write('\nTabela classificada pelo algoritmo Bolha\n\n')
                for listitem in b_bubble:
                    filehandle.write('%s\n' % ', '.join(map(str, listitem)))

            with open(arquivo_saida2, 'w') as filehandle:
                filehandle.write('\nTabela classificada pelo algoritmo Quick Sort (Hoare)\n\n')
                for listitem in b_quick:
                    filehandle.write('%s\n' % ', '.join(map(str, listitem)))

            break

main()
