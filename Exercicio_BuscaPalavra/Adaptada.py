
def Adaptado(a,b):

    tamanho_a, tamanho_b = len(a), len(b)
    conta = 0
    conta_desloc = 1

    #inicializa o ponteiro do b pra ser o último índice do a
    ponteiro_b = tamanho_a - 1
    print("ponteiro B inicial =", ponteiro_b)

    while ponteiro_b < tamanho_b: #enquanto o ponteiro do b não chega no final do b

        #j é o o ponteiro auxiliar do b

        j, ponteiro_a = ponteiro_b, tamanho_a - 1
        print("j antes do segundo while =", j)

        while ponteiro_a >= 0: #controla o ponteiro varrendo o a. enquanto a string a não é igual a b

            if a[ponteiro_a] != b[j]: #se o caractere de a for diferente de b
                print("comparação", "caractere de a =", ponteiro_a, "caractere de b =", j)

                desloc = 0  # talvez seja fora do segundo while

                for p in range(len(a)-1,0,-1): #varre "a" para procurar caractere diferente

                    if a[p] == a[p - 1]:
                        #j = j + 1
                        ponteiro_b = ponteiro_b + 1

                    else:
                        #j = j + 1
                        ponteiro_b = ponteiro_b + 1
                        print("j depois que calculou deslocamento", j)
                        break

                if j > tamanho_b-1:
                    break

            else: #se os caracteres de a e b forem iguais
                ponteiro_a -=1 #diminui um do ponteiro do a
                j -=1 #diminui um do ponteiro do b


            if ponteiro_a < 0: #se todos os caracteres forem iguais

                conta += 1
                print("conta=", conta)
                print("se os elementos são iguais ponteiro b", ponteiro_b)
                print("se elementos sao iguai j=", j)
                #ponteiro_b = ponteiro_b - j



            if len(a) == 1:
                j = j +1
                if j > (len(b)-1):
                    break


    return conta,conta_desloc


#b= "abacabcaabcaba"
#a = "abac"

b = "abcabc"
a = "ab"
print(b)
print(a)
i, j = Adaptado(a, b)
print("BM1=", i, "vezes - ", j, "deslocamentos")