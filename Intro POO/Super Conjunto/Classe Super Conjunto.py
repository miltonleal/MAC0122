def Elimina_Repetidos(lista):
    nova_lista = []
    for k in range(0, len(lista)):
        tem_rep = False
        # procura lista[k] nos elementos à frente
        for j in range(k + 1, len(lista)):
            if lista[k] == lista[j]:
                tem_rep = True
            break
        # se não tem repetidos inclua na nova lista
        if not tem_rep: nova_lista.append(lista[k])
    return nova_lista

class Sset:

    def __init__(self, lista = []):

        self.conjunto = Elimina_Repetidos(lista)
        self.conjunto.sort()

    def __add__(cj1, cj2):

        return Sset(cj1.conjunto + cj2.conjunto)

    def __len__(cj1):

        return len(cj1.conjunto)

    def __str__(cj1):

        return "*" + str(cj1.conjunto)

if __name__ == "__main__":
    x = Sset([1, 2, 25, 5, 72, 5, 1])
    print(len(x))
    print(x)
    y = Sset([])
    print(len(y))
    print(y)
    z = Sset([1, 9, 113, 5, 9, 2, 22, 12, 2, 11])
    print(len(z))
    print(z)
    t = x + z
    print(t)
    print(x + z)