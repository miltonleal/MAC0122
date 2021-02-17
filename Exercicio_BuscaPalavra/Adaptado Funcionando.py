
def desloc (a):

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

    tamanho_a, tamanho_b = len(a), len(b)
    conta = 0
    conta_desloc = 1

    #inicializa o ponteiro do b pra ser o último índice do a
    ponteiro_b = tamanho_a-1

    deslocamentos = desloc(a)

    j = tamanho_a-1

    while ponteiro_b < tamanho_b: #enquanto o ponteiro do b não chega no final do b

        ponteiro_a = tamanho_a - 1
        j = ponteiro_b

        while ponteiro_a >= 0: #controla o ponteiro varrendo o a. enquanto a string a não é igual a b

            if ponteiro_b > tamanho_b - 1:
                break

            if a[ponteiro_a] != b[j]:  # se o caractere de a for diferente de b
                ponteiro_b += deslocamentos[ponteiro_a]
                j = ponteiro_b
                break

            else: #se os caracteres de a e b forem iguais
                ponteiro_a -=1 #diminui um do ponteiro do a
                j = j - 1

            if ponteiro_a < 0: #se todos os caracteres forem iguais

                ponteiro_b += 1
                conta += 1

                if ponteiro_b > tamanho_b - 1:
                    break

    return conta,conta_desloc


b= "abacabcaabcaba"
a = "a"

print(b)
print(a)
i, j = Adaptado(a, b)
print("BM1=", i, "vezes - ", j, "deslocamentos")