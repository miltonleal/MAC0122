count = 0

TAB = [1,2,3,6,20,60,80,90]
def binariaP(x, a):

    global count

    n = len(a)
    # se x está fora da tabela
    if x <= a[0]:
        count +=1
        return 0
    if x > a[n-1]:
        count += 1
        return n
    # x pode estar dentro da tabela
    L = 0
    R = n-1
    while R - L > 1:
        M = (R + L) // 2
        if x <= a[M]:
            count += 1
            R = M
        else:
            count += 1
            L = M
    return R

def InserreBB(TAB,V):
    for i in range(0, len(TAB)):

        j = binariaP(V,TAB)
        print("TAB[:j]", TAB[:j])
        print("[V]", [V])
        print("TAB[j:i+1]", TAB[j:i+1])
        print("TAB[i+1:]", TAB[i+1:])
        print(i)

        arr = TAB[:j] + [V] + TAB[j:]
        return arr, "indice =",j

print(InserreBB(TAB,93))
print("comparações = ",count)


