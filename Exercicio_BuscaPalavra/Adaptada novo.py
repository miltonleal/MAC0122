
def Desloc (a):

    tabela = []

    for t in range (len(a)-1, -1, -1):
        for p in range(t, -1,-1):

            if a[t] != a[p]:
                tabela.append(t-p)
                break

            if t == 0 and p == 0:
                tabela.append(1)

    if len(tabela) != len(a):
        tabela = [1] * len(a)

    tabela.reverse()
    return tabela

def Adaptado(a,b):

    conta = 0
    conta_desloc = 1

    ponteiro_b = len(a)-1

    deslocamentos = Desloc(a)

    while ponteiro_b < len(b): #enquanto o ponteiro do b não chega no final do b

        ponteiro_a = len(a)-1
        ponteiro_b_auxiliar = ponteiro_b

        while ponteiro_a >= 0: #controla o ponteiro varrendo o a. enquanto a string a não é igual a b

            if a[ponteiro_a] != b[ponteiro_b_auxiliar]:  # se o caractere de a for diferente de b
                ponteiro_b += deslocamentos[ponteiro_a]
                conta_desloc += 1
                break

            else: #se os caracteres de a e b forem iguais
                ponteiro_a -= 1 #diminui um do ponteiro do a
                ponteiro_b_auxiliar -= 1

        if ponteiro_a < 0: #se todos os caracteres forem iguais

            ponteiro_b += 1
            conta += 1

    return conta,conta_desloc

b= "ababacbbbababbab"
a = "abb"

print(b)
print(a)
i, j = Adaptado(a, b)
print("BM1=", i, "vezes - ", j, "deslocamentos")