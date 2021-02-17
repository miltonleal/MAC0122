#Nome: Milton Leal Neto
# NUSP: 8973974
# Exercício II – 15/10/2020


def MostreMatriz(Mat, tit):
    print(tit)
    for i in range (9):
        print()
        for j in range (9):
            print(Mat[i][j], end = " ")
    print()

def Verifica_Candidato(matriz, candidato, linha, coluna):

    for j in range(9): #verifica se existe número igual ao candidato na linha
        if candidato == matriz[linha][j]: return False

    for i in range(9): #verifica se existe número igual ao candidato na coluna
        if candidato == matriz[i][coluna]: return False

    #define em qual quadrado 3x3 do Sudoku irá realizar a busca.
    # Utiliza as posições (0,0), (0,3),(0,6), (3,0), (3,3), (3,6), (6,0), (6,3), (6,6) como "âncoras"
    if linha <= 2:
        quadrado_i = 0
    elif linha <= 5:
        quadrado_i = 3
    else:
        quadrado_i = 6
    if coluna <= 2:
        quadrado_j = 0
    elif coluna <= 5:
        quadrado_j = 3
    else:
        quadrado_j = 6

    ##verifica se existe número igual no quadrado 3x3 especificado
    for i in range(quadrado_i, quadrado_i + 3):
        for j in range(quadrado_j, quadrado_j + 3):
            if matriz[i][j] == candidato: return False

    return True

def Encontra_Posicao_Livre(matriz, i_linha, j_coluna):

    for i in range (i_linha, 9): #varre as linhas
        if i == i_linha: #caso inicial
            inicia_coluna = j_coluna #variável que serve pra coordenar o FOR que varre a coluna
        else:
            inicia_coluna = 0

        for j in range (inicia_coluna,9): #varre as colunas
            if matriz[i][j] == 0: return i, j #retorna a posição que está zerada

    return False

#variáveis globais que verificam se não existe solução para o Sudoku
solucao = False
contador = 0

#contador para ordenar as soluções na saída
numero_solucao=0

def Sudoku(matriz, linha, coluna):

    global contador
    global solucao
    global numero_solucao

    contador += 1

    if not Encontra_Posicao_Livre(matriz,linha,coluna): #caso base, quando o Sudoku estiver resolvido
        numero_solucao += 1
        print("\n\n*** SOLUÇÃO", numero_solucao, "***")
        MostreMatriz(matriz, "")

        solucao = True
        contador -= 1

        return

    else: #se não estiver resolvido, atribui às variáveis a posição que está livre
        i_livre, j_livre = Encontra_Posicao_Livre(matriz, linha, coluna)

    for p in range (1,10): #testa os candidatos a serem preenchidos
        if Verifica_Candidato(matriz, p, i_livre, j_livre):

            matriz[i_livre][j_livre] = p #aloca o possível candidato

            Sudoku(matriz, i_livre, j_livre) #chama a função novamente

    matriz[i_livre][j_livre] = 0 #zera a posição para buscar novas soluções

    contador -= 1
    if not solucao and contador == 0:
        print("\nSUDOKU SEM SOLUÇÃO")
    if contador == 0:
        solucao = False
        numero_solucao = 0

    return





