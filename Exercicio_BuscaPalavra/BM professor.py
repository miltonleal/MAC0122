def BoyerMoore1(a, b):
    m, n = len(a), len(b)
    conta = 0
    ndesloc = 0
    # tabela de últimas ocorrências de cada caractere em a
    ult = [-1] * 256
    # varrer a e definir as últimas ocorrências de cada caractere
    for k in range(m): ult[ord(a[k])] = k
    # procura a em b - da esquerda para a direita
    k = m - 1
    while k < n:
        j, i = k, m - 1
        while i >= 0:
            if a[i] != b[j]: break
            j, i = j - 1, i - 1
        # comparação chegou ao fim
        if i < 0: conta += 1
        # caso particular - se k é n-1 (último de b)
        # então k+1 é índice inválido
        # o if abaixo evita esse caso
        if k + 1 >= n: break
        # desloca baseado no valor de b[k+1]
        k = k + m - ult[ord(b[k + 1])]
        ndesloc +=1
    return conta, ndesloc

print("\n=== TESTE 2 ===\n")
b = "abacacbabcdcdabd"
a = "abcd"
print("B =",b)
print("A =",a)
print("\n*** BoyerMoore 1 ***\n")
i, j = BoyerMoore1(a, b)
print("Deslocamentos")
print("Correto =", 4)
print("Obtido =", j)
print("\nVezes")
print("Correto =", 1)
print("Obtido =", i)