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

# testes
P = PilhaLista()
P.push(1)
P.push("tipo de elemento")
P.push((5, 4, 3))
P.push(True)
print("tamanho da pilha = ", len(P))
print("elemento do topo da pilha = ", P.top())
print(P.pop())
print(P.pop())
print(P.pop())
print(P.pop())
# os comandos abaixo geram uma excessão
