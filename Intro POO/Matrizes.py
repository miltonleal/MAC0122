class Matriz:

    def __init__(self, n, m):

        #cria uma lista de listas
        self.elementos = [m * [0] for k in range(n)]

    def __setitem__(self, linha, conteudo_linha):
        self.elementos[linha] = conteudo_linha[:]

    def __str__(s):
        lin = ''
        for i in range(len(s.elementos)):
            for j in range(len(s.elementos[i])):
                lin += str(s.elementos[i][j]) + ' '
        lin += '\n'
        return lin

if __name__ == "__main__":

    matriz1 = Matriz(3,3)
    matriz1[1] = [1,1,1]
    print(matriz1)

