ordem = [2,0,1]
lista = [["0","1", "1"], ["0","1", "1"], ["1","1", "2"], ["2","0", "1"], ["2","2", "0"]]


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


print(Quick_Sort(lista, ordem))