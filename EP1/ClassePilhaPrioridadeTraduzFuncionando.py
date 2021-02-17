#exp1 = ["@", 1,"*", 1]
exp1 = ["(",2, "*", 3, ")",]
#exp2 = [1,"+", 2, "+", 3]
#exp3 = [1,"*", 2, "+", 3]
#exp4 = [1,"+", 2, "*", 3]
#exp5 = [1,"*", "(", 2, "+", 3, ")"]
#exp6 = ["(",1,"+", 2,")", "*", 3]
#exp7 = [1,"*","(",1,"+","(",1,"*", "(", 2, "+", 3, ")", ")", ")"]
#exp8 = [1, "/", "(", 1, "*", 2, ")", "*", 3]


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

def PrioridadeOperadores (x):

    if x == '**':  return 6
    elif x == '@': return 5
    elif x == '*': return 4
    elif x == '/': return 4
    elif x == '%': return 4
    elif x == '//':return 4
    elif x == '+': return 3
    elif x == '-': return 3
    elif x == ')': return 2 # caso particular
    elif x == '(': return 7 # caso particular
    else:
        return 0

def TraduzPosFixa (exp):

    PosFixaTraduzida = []

    Pilha = PilhaLista()

    for k in range (len(exp)):
        print(PosFixaTraduzida)
        print(vars(Pilha))

        if type(exp[k]) is float or type(exp[k]) is int:
            PosFixaTraduzida.append(exp[k])

        if type(exp[k]) is str and exp[k] != ")":

            if not Pilha.is_empty():

                while PrioridadeOperadores(Pilha.top()) >= PrioridadeOperadores(exp[k]):
                    if PrioridadeOperadores(Pilha.top()) != 7:
                        PosFixaTraduzida.append(Pilha.pop())
                    break
            Pilha.push(exp[k])

        if exp[k] == ")":
            #print("depois que encontra o fecha", vars(Pilha))
            while Pilha.top() != "(":
                PosFixaTraduzida.append(Pilha.pop())
            Pilha.pop()
    while True:
        if not Pilha.is_empty():
            PosFixaTraduzida.append(Pilha.pop())
        else: break

    return PosFixaTraduzida

print(TraduzPosFixa(exp1))
#print(TraduzPosFixa(exp2))
#print(TraduzPosFixa(exp3))
#print(TraduzPosFixa(exp4))
#print(TraduzPosFixa(exp5))
#print(TraduzPosFixa(exp6))
#print(TraduzPosFixa(exp7))
#print(TraduzPosFixa(exp8))


