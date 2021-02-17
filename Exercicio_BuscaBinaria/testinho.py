count = 0

def InsereBB(TAB,V):

    global count

    n = len(TAB)
    # se x está fora da tabela
    if V <= TAB[0]:
        count +=1
        return 0
    if V > TAB[n-1]:
        count += 1
        return n
    # x pode estar dentro da tabela
    L = 0
    R = n-1
    while R - L > 1:
        M = (R + L) // 2
        if V <= TAB[M]:
            count += 1
            R = M
        else:
            count += 1
            L = M
    return R


    for i in range(0, len(TAB)):

        j = binariaP(V,TAB)

        arr = TAB[:j] + [V] + TAB[j:]
        return arr, "indice =",j


print("comparações = ",count)


