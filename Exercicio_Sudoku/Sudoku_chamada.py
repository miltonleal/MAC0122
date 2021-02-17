from sudoku import *

def MostreMatriz(Mat, tit):
    print("\n", tit)
    for i in range (9):
        print()
        for j in range (9):
            print(Mat[i][j], end = " ")
    print()

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
        Sudoku(mats,0,0)
# executa o main()
main()

