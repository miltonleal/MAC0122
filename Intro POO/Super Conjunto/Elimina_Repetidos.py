a = [1,1,2]

def Elimina_Repetidos(lista):
    nova_lista = []
    for k in range(0, len(lista)):
        tem_rep = False
        print("tem_rep antes do for", tem_rep)
        # procura lista[k] nos elementos à frente
        for j in range(k + 1, len(lista)):
            if lista[k] == lista[j]:
                tem_rep = True
                print("tem_rep depois do for", tem_rep)
            break
# se não tem repetidos inclua na nova lista
        print ("valor do not tem_rep", not tem_rep)
        if not tem_rep: nova_lista.append(lista[k])
    return nova_lista

print(Elimina_Repetidos(a))

b = False
print (not b)