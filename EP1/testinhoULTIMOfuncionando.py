#Nome: Milton Leal Neto
# NUSP: 8973974
# Exercício Programa I – 25/10/2020

import re

def BuscaUnarios(exp): #verifica existência de operadores unários
    if exp[0] == "-":
        exp[0] = "@" #substitui o - unário por @

    elif exp[0] == "+":
        del exp[0] #deleta o + se for o primeiro elemento da expressão

    for j in range(2, len(exp) - 1):
        if exp[j] == "-": #se encontrar o - unário, transforma em @
            if exp[j - 1] in "(+*/%//**":
                exp[j] = "@"
    return exp

def Transforma_Int_Float(exp): #transforma elementos em int ou float

    for j in range(len(exp)):
        if '.' in exp[j]: # se encontrar um . no elemento, é float
            exp[j] = float(exp[j])

        #se encontrar um número dentro da string, transforma em int
        elif '0' in exp[j] or '1' in exp[j] or '2' in exp[j] or '3' in exp[j] or \
                '4' in exp[j] or '5' in exp[j] or '6' in exp[j] or '7' in exp[j] or \
                '8' in exp[j] or '9' in exp[j]:
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

def PrioridadeOperadores (x): #define a prioridade dos operadores em order decrescente

    if x == '**': return 5
    elif x == '@': return 4
    elif x == '*': return 3
    elif x == '/': return 3
    elif x == '%': return 3
    elif x == '//':return 3
    elif x == '+': return 2
    elif x == '-': return 2
    elif x == '(': return 1

def TraduzPosFixa (exp):

    PosFixaTraduzida = [] #inicia lista vazia para receber expressão pós-fixa
    Pilha = PilhaLista() #inicia pilha para os operadores

    for k in range (len(exp)): #varre a expressão

        if type(exp[k]) is float or type(exp[k]) is int: # se for int ou float, coloca na posfixa
            PosFixaTraduzida.append(exp[k])

        elif exp[k] == "(": #se encontrar um abre parênteses, empilha
            Pilha.push(exp[k])

        elif exp[k] == ")": #se encontrar um fecha parênteses, desempilha todos até o abre
            topo_pilha = Pilha.pop()

            while topo_pilha != "(":
                PosFixaTraduzida.append(topo_pilha)
                topo_pilha = Pilha.pop()

        else: #se não houver parênteses, empilha ou coloca na posfixa de acordo com a prioridade
            while (not Pilha.is_empty()) and (PrioridadeOperadores(Pilha.top()) >= PrioridadeOperadores(exp[k])):
                PosFixaTraduzida.append(Pilha.pop())
            Pilha.push(exp[k])

    while not Pilha.is_empty(): #desempilha todos que sobraram
        PosFixaTraduzida.append(Pilha.pop())

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
        expressao = input(">>> ") #recebe a expressão
        if expressao.lower() == "fim": #termina o programa
            print("\n*** Fim do programa ***")
            quit()

        exp = re.findall(r"(\b\w*[\.]?\w+\b|//|\*\*|[()+\-*/%])", expressao) #separa a expressão em uma lista

        #Chamada das funções
        Unarios = BuscaUnarios(exp) #recebe a lista com os ajustes relativos aos unários
        Int_Float = Transforma_Int_Float(Unarios) #recebe a lista com as transformações de int e float
        PosFixa = TraduzPosFixa(Int_Float) #recebe a lista com a pós-fixa traduzida

        try:
            if CalculaPosFixa(PosFixa):
                print("Expressão Pós-Fixa:", PosFixa)
                print("Resultado:", CalculaPosFixa(PosFixa), "\n")

        except:
            print("Expressão incorreta. Não foi possível calcular.\n")

main()