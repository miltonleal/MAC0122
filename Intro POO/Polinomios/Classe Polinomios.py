class Polinomios:

    def __init__(self, lista_com_coeficientes):

        self.objeto_com_coeficientes = lista_com_coeficientes[:]

    def valor (polinomio, x):

        soma = 0
        for j in range (len(polinomio.objeto_com_coeficientes)):
            soma += polinomio.objeto_com_coeficientes[j] * pow(x,j)
        return soma

if __name__ == "__main__":

    p1 = Polinomios([1.0, -2.2, 3.5])
    v = p1.valor(1.0)
    print(v)

