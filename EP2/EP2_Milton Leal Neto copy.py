#Nome: Milton Leal Neto
# NUSP: 8973974
# Exercício Programa II – 22/11/2020

import time

def transforma_data(tabela):

    #função que transforma a data DD/MM/AAAA para AAAA/MM/DD
    # e também faz o reverso AAAA/MM/DD para DD/MM/AAAA)
    for i in range(len(tabela)):
        # lista que recebe a terceira coluna da tabela splitada em dia, mês e ano
        data = tabela[i][2].split("/")
        # substitui a terceira coluna da tabela pela lista data
        tabela[i][2] = data
        # troca elemento ANO pelo elemento DIA ou vice versa
        tabela[i][2][0], tabela[i][2][2] = tabela[i][2][2], tabela[i][2][0]
        # Transforma em string novamente no formato AAAA/MM/DD ou DD/MM/AAAA
        tabela[i][2] = tabela[i][2][0] + "/" + tabela[i][2][1] + "/" + tabela[i][2][2]

    return tabela

def bubble_sort(tabela,ordem):

    n = len(tabela)

    for i in range(1, n):

        j = i
        while j > 0:
            # verifica se o primeiro elemento é menor que anterior
            if tabela[j][ordem[0]] < tabela[j - 1][ordem[0]]:
                tabela[j], tabela[j - 1] = tabela[j - 1], tabela[j] #se for, troca
                j = j - 1
                continue

            # se primeiro elemento for igual ao anterior e a ordem de classificação for maior que uma coluna
            elif tabela[j][ordem[0]] == tabela[j - 1][ordem[0]] and len(ordem) != 1:

                if len(ordem) == 2: #caso em que a ordem de classificação envolve duas colunas

                    if tabela[j][ordem[1]] < tabela[j-1][ordem[1]]: #se o segundo elemento da ordem for menor
                        tabela[j], tabela[j - 1] = tabela[j - 1], tabela[j] #troca
                        j = j - 1
                    # se o segundo for maior que o anterior, dá o break
                    elif tabela[j][ordem[1]] >= tabela[j - 1][ordem[1]]:
                        break

                if len(ordem) == 3: #caso em que a ordem de classificação envolve três colunas

                    if tabela[j][ordem[1]] < tabela[j-1][ordem[1]]: #se o segundo elemento da ordem for menor
                        tabela[j], tabela[j - 1] = tabela[j - 1], tabela[j] #troca
                        j = j - 1

                    elif tabela[j][ordem[1]] == tabela[j-1][ordem[1]]: #se segundo elemento for igual

                        if tabela[j][ordem[2]] < tabela[j-1][ordem[2]]: #verifica se o terceiro elemento é menor
                            tabela[j], tabela[j - 1] = tabela[j - 1], tabela[j] #se for, troca
                            j = j - 1
                        #se terceiro elemento for menor que o anterior, dá o break
                        elif tabela[j][ordem[2]] >= tabela[j - 1][ordem[2]]:
                            break
                    #se o se segundo for maior que anterior, dá o break
                    elif tabela[j][ordem[1]] >= tabela[j - 1][ordem[1]]:
                        break
            #se o primeiro elemento for maior que anterior, dá o break
            elif tabela[j][ordem[0]] >= tabela[j - 1][ordem[0]]:
                break

    return tabela

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

def quick_sort(lista,ordem):
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

def partition(lista,inicio,fim,ordem):

    pivot = lista[fim] #inicia o pivô como último da lista
    i,j = inicio, fim #ponteiros

    while True:
        if len(ordem) == 1: #caso com ordenação de uma coluna

            #se elemento for menor ou igual ao pivô
            while i < j and lista[i][ordem[0]] <= pivot[ordem[0]]:
                i = i + 1 #avança o i para a direita
            if i < j:
                lista[i], lista[j] = pivot, lista[i] #troca elemento com o pivô
                j = j-1 #avança o j para esquerda
            else:
                break
            #se elemento for maior ou igual ao pivô
            while i < j and lista[j][ordem[0]] >= pivot[ordem[0]]:
                j = j - 1 #avança j para esquerda
            if i < j:
                lista[i], lista[j] = lista[j], pivot #troca elemento com pivô
                i = i + 1 #avança o i para a direita
            else:
                break

        if len(ordem) == 2: #caso com ordenação de uma coluna

            while i < j:
                if lista[i][ordem[0]] < pivot[ordem[0]]:#se elemento for menor ou igual ao pivô
                    i = i + 1 #avança o i para a direita
                #se o primeiro é igual e o segundo é menor ou igual
                elif lista[i][ordem[0]] == pivot[ordem[0]] and \
                    lista[i][ordem[1]] <= pivot[ordem[1]]:
                    i = i + 1 #avança o i para a direita
                else:
                    break

            if i < j:
                lista[i], lista[j] = pivot, lista[i] #troca elemento com pivô
                j = j - 1 #avança j para esquerda
            else:
                break

            while i < j:
                if lista[j][ordem[0]] > pivot[ordem[0]]: #se elemento for maior ou igual ao pivô
                    j = j - 1 #avança j para esquerda

                #se o primeiro elemento é igual e o segundo é maior ou igual
                elif lista[j][ordem[0]] == pivot[ordem[0]] and \
                    lista[j][ordem[1]] >= pivot[ordem[1]]:
                    j = j - 1 #avança j para esquerda
                else:
                    break

            if i < j:
                lista[i], lista[j] = lista[j], pivot #troca elemento com pivô
                i = i + 1 #avança o i para a direita
            else:
                break

        if len(ordem) == 3:

            while i < j:
                # se elemento for menor que o pivô
                if lista[i][ordem[0]] < pivot[ordem[0]]:
                    i = i + 1 #avança o i para a direita
                # se o primeiro é igual e o segundo é menor
                elif lista[i][ordem[0]] == pivot[ordem[0]] and \
                    lista[i][ordem[1]] < pivot[ordem[1]]:
                    i = i + 1 #avança o i para a direita
                #se o primeiro e segundo são iguais e o terceiro é menor ou igual
                elif lista[i][ordem[0]] == pivot[ordem[0]] and \
                    lista[i][ordem[1]] == pivot[ordem[1]] and \
                    lista[i][ordem[2]] <= pivot[ordem[2]]:
                    i = i + 1 #avança o i para a direita
                else:
                    break

            if i < j:
                lista[i], lista[j] = pivot, lista[i] #troca elemento com pivô
                j = j - 1 #avança j para esquerda
            else:
                break

            while i < j:
                # se elemento for maior que o pivô
                if lista[j][ordem[0]] > pivot[ordem[0]]:
                    j = j - 1 #avança j para esquerda
                # se o primeiro é igual e o segundo é maior
                elif lista[j][ordem[0]] == pivot[ordem[0]] and \
                    lista[j][ordem[1]] > pivot[ordem[1]]:
                    j = j - 1 #avança j para esquerda
                # se o primeiro e segundo são iguais e o terceiro é maior ou igual
                elif lista[j][ordem[0]] == pivot[ordem[0]] and \
                    lista[j][ordem[1]] == pivot[ordem[1]] and \
                    lista[j][ordem[2]] >= pivot[ordem[2]]:
                    j = j - 1 #avança j para esquerda
                else:
                    break

            if i < j:
                lista[i], lista[j] = lista[j], pivot #troca elemento com pivô
                i = i + 1 #avança o i para a direita
            else:
                break
    return i

def main():

    print("*** CLASSIFICADOR DE TABELAS ***")
    while True:

        #Solicita o nome dos arquivos

        arquivo_entrada = input("\nNome do arquivo de origem: ") #pede ao usuário nome do arquivo de entrada
        if arquivo_entrada.lower() == "fim": #se usuário digitar "fim", termina o programa
            quit()

        arquivo_saida1 = input("\nNome do arquivo de destino 1: ") #pede ao usuário nome do arquivo de saída 1
        if arquivo_saida1.lower() == "fim":  # se usuário digitar "fim", termina o programa
            quit()

        arquivo_saida2 = input("\nNome do arquivo de destino 2: ")  # pede ao usuário nome do arquivo de saída 2
        if arquivo_saida2.lower() == "fim":  # se usuário digitar "fim", termina o programa
            quit()

        while True:

            while True:

                #Solicita a ordem de classificação

                ordem = input("\nInsira a ordem de classificação dos valores: ")
                if ordem.lower() == "fim":  # se usuário digitar "fim", termina o programa
                    quit()

                lista_ordem = ordem.split(',') #splita a ordem de classificação em uma lista

                set_ordem = set(lista_ordem) #cria um conjunto com os elementos da ordem

                #consistência dos dados de entrada da ordem de classificação
                try:
                    if set_ordem <= {"0", "1", "2"} and len(lista_ordem) <= 3:
                        break
                    else:
                        print("\nErro! Insira a ordem de clasificação corretamente. Exemplo: 1 ou 1,2 ou 0,2,3")
                        continue
                except:
                    pass

            #transforma os elementos da lista da ordem em inteiros
            lista_ordem_int = list(map(int, lista_ordem))

            #tenta abrir o arquivo de entrada
            try:
                with open(arquivo_entrada, "r") as arq: #abre o arquivo

                    linhas = arq.readlines()  #retorna uma lista que contém cada linha do arquivo como um item da lista
            except:
                print("\nErro na abertura do arquivo de entrada. Insira novamente o nome do arquivo.")
                break

            #printa a ordem de classificação
            print("\nOrdem de classificação:", ','.join(map(str, lista_ordem_int)))

            lista_separada = [] #cria lista para receber o conteúdo da lista original
            for linha in linhas: #lê cada linha da lista "linhas"

                try:
                    lin = linha[:len(linha) - 1]  #variável que recebe cada linha do arquivo de texto original como uma string
                    v = linha.rstrip('\n').split(',')  #variável que recebe a linha acima e a transforma e
                    lista_separada.append(v)

                except: pass

            lista_bubble = lista_separada.copy() #copia a lista original e nova lista
            lista_quick = lista_separada.copy() #copia a lista original e nova lista

            #Chamada do algoritmo Quick Sort
            if 2 not in lista_ordem_int: #se não houver classificação por data
                start = time.process_time() #inicia contagem do tempo
                b_quick = quick_sort(lista_quick, lista_ordem_int) #chama a função
                print("Tempo de classificação - Quick Sort (Hoare) = ", time.process_time() - start) #printa o tempo

            else: #se houver classificação por data
                a_quick = transforma_data(lista_quick) #transforma a data
                start = time.process_time() #inicia contagem do tempo
                aux_quick = quick_sort(a_quick, lista_ordem_int) #chamada da função
                print("Tempo de classificação - Quick Sort (Hoare) = ", time.process_time() - start) #printa o tempo
                b_quick = transforma_data(aux_quick) #transforma a data

            # Chamada do algoritmo da Bolha
            if 2 not in lista_ordem_int: #se não houver classificação por data
                start = time.process_time() #inicia contagem do tempo
                b_bubble = bubble_sort(lista_bubble, lista_ordem_int) #chama a função
                print("Tempo de classificação - Bolha = ", time.process_time() - start) #printa o tempo

            else:
                a_bubble = transforma_data(lista_bubble) #transforma a data
                start = time.process_time() #inicia contagem do tempo
                aux_bubble = bubble_sort(a_bubble, lista_ordem_int) #chamada da função
                print("Tempo de classificação - Bolha = ", time.process_time() - start) #printa o tempo
                b_bubble = transforma_data(aux_bubble) #transforma a data

            #gravação dos arquivos
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
