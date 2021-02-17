import re

def BuscaUnarios(exp):
    if exp[0] == "-":
        exp[0] = "@"
    elif exp[0] == "+":
        del exp[0]

    for j in range(2, len(exp) - 1):
        if exp[j] == "+":
            if exp[j - 1] == "(" or exp[j - 1] == ")" or exp[j - 1] == "*" or exp[j - 1] == "/" \
                    or exp[j - 1] == "%" or exp[j - 1] == "//" or exp[j - 1] == "**":
                del exp[j]

    for j in range(2, len(exp) - 1):
        if exp[j] == "-":
            if exp[j - 1] == "(" or exp[j - 1] == ")" or exp[j - 1] == "+" or exp[j - 1] == "*" or \
                    exp[j - 1] == "/" or exp[j - 1] == "%" or exp[j - 1] == "//" or exp[j - 1] == "**":
                exp[j] = "@"

    return exp

def Transforma_Int_Float(exp):
    for j in range(len(exp)):
        if '.' in exp[j]:
            exp[j] = float(exp[j])
        elif '0' in exp[j] or '1' in exp[j] or '2' in exp[j] or '3' in exp[j] or \
                '4' in exp[j] or '5' in exp[j] or '6' in exp[j] or '7' in exp[j] or \
                '8' in exp[j] or '9' in exp[j]:
            exp[j] = int(exp[j])
    return exp

class Empty(Exception):
    pass

class PilhaLista: #COMENTADO

    def __init__(self): #Construtor da classe PilhaLista
        self._pilha = []  #Lista que conterá a pilha

    def __len__(self): #Retorna o tamanho da pilha
        return len(self._pilha)

    def is_empty(self): #Retorna True se pilha vazia
        return len(self._pilha) == 0

    def push(self, elemento): #Empilha novo elemento
        self._pilha.append(elemento)

    def top(self): #Retorna o elemento do topo da pilha sem retirá-lo
        if self.is_empty():
            raise Empty("Pilha vazia")#Exceção se pilha vazia
        return self._pilha[-1]

    def pop(self): #Desempilha elemento
        if self.is_empty():
            raise Empty("Pilha vazia") #Excessão se pilha vazia
        return self._pilha.pop()


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
        #print(PosFixaTraduzida)
        #print(vars(Pilha))

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
    print("PosFixa Traduzida", PosFixaTraduzida)
    return PosFixaTraduzida

def CalculaPosFixa(expressao):
    #print("expressao que entra na calculaposfixa", expressao)
    Pilha_Numeros = PilhaLista()

    for j in range (len(expressao)):
        if expressao[j] == "**" and len(expressao) > j + 2:
            if expressao[j+2] == "@":
                expressao[j], expressao[j+2] = expressao[j+2], expressao[j]
                expressao[j], expressao[j+1] = expressao[j+1], expressao[j]
    #print("expressao ajustada", expressao)

    for i in range (len(expressao)):

        if type(expressao[i]) == int or type(expressao[i]) == float:
            Pilha_Numeros.push(expressao[i])

            #print("pilha de numeros", vars(Pilha_Numeros))
        else:
            if expressao[i] != "@":
                operando1 = Pilha_Numeros.pop()
                operando2 = Pilha_Numeros.pop()
                Pilha_Numeros.push(Calcula(expressao[i],operando2,operando1))

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

while True:
    exp = input(">>> ")
    if exp.lower() == "fim":
        print("\n*** Fim do programa ***")
        quit()

    exp_lista = re.findall(r"(\b\w*[\.]?\w+\b|//|\*\*|[()+\-*/%])", exp)

    #a = TraduzPosFixa(Transforma_Int_Float(BuscaUnarios(exp_lista)))

    print(CalculaPosFixa(TraduzPosFixa(Transforma_Int_Float(BuscaUnarios(exp_lista)))))
