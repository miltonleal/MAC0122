a = [ 2,"@",2, "*"]


class Empty(Exception):
    pass

class PilhaLista:

    # Pilha como uma lista
    # Construtor da classe PilhaLista
    def __init__(self):
        self._pilha = []  # lista que conterá a pilha

    # retorna o tamanho da pilha
    def __len__(self):
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
        return self._pilha.pop()

def CalculaPosFixa(expressao):

    Pilha_Numeros = PilhaLista()


    for i in range (len(expressao)):
        if type(expressao[i]) == int or type(expressao[i]) == float:
            Pilha_Numeros.push(expressao[i])
            print(vars(Pilha_Numeros))
        else:
            if expressao[i] != "@":
                operando1 = Pilha_Numeros.pop()
                operando2 = Pilha_Numeros.pop()
                Pilha_Numeros.push(Calcula(expressao[i],operando1,operando2))
            else:
                operando1 = Pilha_Numeros.pop()
                Pilha_Numeros.push(-1*operando1)
    return Pilha_Numeros.top()


def Calcula(operador, operando1, operando2):

    if operador == "**":
        return operando1 ** operando2
    elif operador == "*":
        return operando1 * operando2
    elif operador == "/":
        return operando1 / operando2
    elif operador == "//":
        return operando1 // operando2
    elif operador == "+":
        return operando1 + operando2
    elif operador == "-":
        return operando1 - operando2
    else:
        return operando1 % operando2

print(CalculaPosFixa(a))

