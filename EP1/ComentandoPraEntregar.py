#Nome: Milton Leal Neto
# NUSP: 8973974
# Exercício Programa I – 25/10/2020

import re

def BuscaUnarios(exp): #verifica existência de operadores unários
    if exp[0] == "-":
        exp[0] = "@" #substitui o - unário por @

    elif exp[0] == "+":
        del exp[0]

    for j in range(2, len(exp) - 1):
        if exp[j] == "-":
            if exp[j - 1] in "(+*/%//**":
                exp[j] = "@"
    return exp

def Transforma_Int_Float(exp): #transforma elementos em int ou float

    for j in range(len(exp)):
        if '.' in exp[j]: # encontrar um . no elemento, é float
            exp[j] = float(exp[j])
        #se encontrar um número dentro da string, transforma em int
        elif exp[j] in '0123456789':
            exp[j] = int(exp[j])

    return exp

class Empty(Exception): #cria exceção para palavra Empty
    pass

class PilhaLista:

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

def PrioridadeOperadores (x): #define a prioridade dos operadores

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

    PosFixaTraduzida = [] #inicia lista vazia para receber expressão pós-fixa
    Pilha = PilhaLista() #inicia pilha para os operadores

    for k in range (len(exp)): #varre a expressão

        if type(exp[k]) is float or type(exp[k]) is int: # se for int ou float, coloca na posfixa
            PosFixaTraduzida.append(exp[k])

        if type(exp[k]) is str and exp[k] != ")": #se for operador e não for )

            if not Pilha.is_empty(): #caso a pilha não esteja vazia

                #checa a prioridade de quem está chegando e quem está no topo da pilha
                while PrioridadeOperadores(Pilha.top()) >= PrioridadeOperadores(exp[k]):
                    if PrioridadeOperadores(Pilha.top()) != 7: #checa se o topo é != de (
                        PosFixaTraduzida.append(Pilha.pop()) #coloca na pilha
                    break

            #se a pilha estiver vazia, empilha
            Pilha.push(exp[k])

        if exp[k] == ")": #se chegar um fecha parênteses, coloca todos pra dentro da Pilha até o abre
            while Pilha.top() != "(":
                PosFixaTraduzida.append(Pilha.pop())
            Pilha.pop() #retira o ( da pilha

    while True:
        if not Pilha.is_empty():
            PosFixaTraduzida.append(Pilha.pop())
        else: break

    print("Pós-Fixa Traduzida =", PosFixaTraduzida)
    return PosFixaTraduzida

def CalculaPosFixa(expressao):

    Pilha_Numeros = PilhaLista() #inicia uma pilha vazia

    # consistência para o caso 2**-2. Procura o padrão ** elemento @, onde @ = - unário
    for j in range (len(expressao)):
        if expressao[j] == "**" and len(expressao) > j + 2:
            if expressao[j+2] == "@":
                #inverte as posições para sair correto na PosFixa Traduzida
                expressao[j], expressao[j+2] = expressao[j+2], expressao[j]
                expressao[j], expressao[j+1] = expressao[j+1], expressao[j]

    for i in range (len(expressao)): #varre a expressão
        if type(expressao[i]) == int or type(expressao[i]) == float: #empilha se for int ou float
            Pilha_Numeros.push(expressao[i])

        else:
            if expressao[i] != "@": #se for diferente do - unário
                operando1 = Pilha_Numeros.pop() #pega o último da pilha
                operando2 = Pilha_Numeros.pop() #pega o penúltimo da pilha
                Pilha_Numeros.push(Calcula(expressao[i],operando2,operando1)) #calcula entre os dois

            else: #se for - unário
                operando1 = Pilha_Numeros.pop() #pega o último da pilha
                Pilha_Numeros.push(-1*operando1) #transforma em -1

    return Pilha_Numeros.top()

def Calcula(operador, operando1, operando2): #realiza os cálculos

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

def main():

    print("\n*** Interpretador de Expressões Numéricas ***\n")
    while True:
        print("Insira o valor da expressão:")
        exp = input(">>> ") #recebe a expressão
        if exp.lower() == "fim": #termina o programa
            print("\n*** Fim do programa ***")
            quit()

        exp_lista = re.findall(r"(\b\w*[\.]?\w+\b|//|\*\*|[()+\-*/%])", exp) #separa a expressão em uma lista

        print("Resultado:", CalculaPosFixa(TraduzPosFixa(Transforma_Int_Float(BuscaUnarios(exp_lista)))),"\n")
        #print("\n")

main()