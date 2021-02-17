

def MostreMatriz(Mat, tit):
    print("\n", tit)
    for i in range (9):
        print()
        for j in range (9):
            print(Mat[i][j], end = " ")
    print()

def ProcuraElementoLinha(Mat, x, lin):
    #retorna -1 se não encontrar x na linha lin ou a coluna
    for j in range (9):
        if x == Mat[lin][j]: return j
    return -1

def ProcuraElementoColuna(Mat, x, col):
    #retorna -1 se não encontrar x na coluna col ou a linha
    for j in range (9):
        if x == Mat[j][col]: return j
    return -1

def ProcuraElementoQuadrado(Mat, x, lin, col):
    #retorna -1, -1 se não encontrar x em Mat[lin...lin+2]
    for i in range (lin, lin + 3):
        for j in range (col, col + 3):
            if Mat[i][j] == x: return i, j
    return -1, -1

def DefineQuadrado(lin, col):
    #define quadrado interno para o elemento [lin][col]
    #devolve linha, coluna desse quadrado
    if lin <= 2: ii=0
    elif lin <=5: ii = 3
    else: ii = 6
    if col <= 2: jj = 0
    elif col <= 5: jj=3
    else: jj= 6
    return ii, jj

def TestaElemento (Mat, x, lin, col):
    #verifica se x é um candidato a ocupar a posição [i][j]
    #retorna True ou False
    if ProcuraElementoLinha(Mat, x, lin) >= 0: return False
    if ProcuraElementoColuna(Mat, x, col) >= 0: return False
    k1, k2 = DefineQuadrado(lin, col)
    if ProcuraElementoQuadrado(Mat, x, k1, k2) == (-1,-1):
        #x não está na linha, na coluna e no quadrado
        return True

def ProcuraCasaLivre(mat, nlin, ncol):
    #Varre a matriz sudoku mat a partir do elemento [nlin][ncol]
    #até achar uma casa livre. Devolve (i,j) ou (-1,-1)

    for i in range (nlin, 9):
        if i == nlin: ncol_inic = ncol #linha incompleta
        else: ncol_inic = 0 #linha completa
        for j in range (ncol_inic,9):
            if mat[i][j] == 0: return i, j
    #se chegou aqui, não há casa livre
    return -1, -1

def Sudoku(ms, lin, col):
    #recebe a matriz sudoku ms e tenta preenchela a partir do elemento [lin][col]

    liv_lin, liv_col = ProcuraCasaLivre(ms, lin, col)

    if (liv_lin, liv_col) == (-1,-1):
        MostreMatriz(ms, "\n\n*** Matriz Completa")
        return

    for k in range (1,10):
        #k é um candidato a esta casa vazia?

        if TestaElemento(ms, k, liv_lin, liv_col):
            #k é um candidato - preenche
            ms[liv_lin][liv_col] = k
            #continua preenchendo com esta casa já definida
            #MostreMatriz(ms, "\n\nNovaMatriz a Preencher")
            Sudoku(ms, liv_lin, liv_col)

    #neste ponto já testou com todas as possibilidades
    #zera novamente para retroceder a busca
    ms[liv_lin][liv_col] = 0

    return


def LeiaMatriz(Mat, NomeArq):
    # retorna True se conseguiu ler o arquivo e False caso contrário
    # abrir o arquivo para leitura
    try:
        arq = open(NomeArq, "r")
    except:
        return False
    # ler cada uma das linhas
    i = 0
    for linha in arq:
        v = linha.split()
        # transforma os strings em números
        for j in range(len(v)):
            Mat[i][j] = int(v[j])
        i = i + 1
    # fechar arquivo
    arq.close()
    return True


def main():
    # inicia matriz sudoku
    mats = [9 * [0] for i in range(9)]
    # repita até ser digitado fim como nome do arquivo
    while True:
        # nome do arquivo
        while True:
            nomearq = input("\n\nEntre com o nome do arquivo:")
            if nomearq == "fim": return
            # ler e mostrar a matriz inicial
            if LeiaMatriz(mats, nomearq): break
            else: print("* * * Arquivo inválido * * *")
        MostreMatriz(mats, "\n\n* * * Matriz inicial * * *")
        # Chamada da função Sudoku
        # Encontra todas as soluções para esta matriz
        Sudoku(mats, 0,0)
# executa o main()
main()





