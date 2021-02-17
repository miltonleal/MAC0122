def transforma_data (matrix):

    for i in range(len(matrix)):
        data = matrix[i][2].split("/")
        matrix[i][2] = data
        matrix[i][2][0], matrix[i][2][2] = matrix[i][2][2], matrix[i][2][0]
        matrix[i][2] = matrix[i][2][0] + "/" + matrix[i][2][1] + "/" + matrix[i][2][2]



    return matrix

def Bubble(matrix, order):

    n = len(matrix)

    for i in range(1, n):

        j = i
        while j > 0:

            if matrix[j][order[0]] < matrix[j - 1][order[0]]:
                matrix[j], matrix[j - 1] = matrix[j - 1], matrix[j]
                j = j - 1
                continue

            elif matrix[j][order[0]] == matrix[j - 1][order[0]] and len(order) != 1:

                if len(order) == 2:

                    if matrix[j][order[1]] < matrix[j-1][order[1]]:
                        matrix[j], matrix[j - 1] = matrix[j - 1], matrix[j]
                        j = j - 1

                    elif matrix[j][order[1]] >= matrix[j - 1][order[1]]:
                        break

                if len(order) == 3:

                    if matrix[j][order[1]] < matrix[j-1][order[1]]:
                        matrix[j], matrix[j - 1] = matrix[j - 1], matrix[j]
                        j = j - 1

                    elif matrix[j][order[1]] == matrix[j-1][order[1]]:

                        if matrix[j][order[2]] < matrix[j-1][order[2]]:
                            matrix[j], matrix[j - 1] = matrix[j - 1], matrix[j]
                            j = j - 1

                        elif matrix[j][order[2]] >= matrix[j - 1][order[2]]:
                            break

                    elif matrix[j][order[1]] >= matrix[j - 1][order[1]]:
                        break

            elif matrix[j][order[0]] >= matrix[j - 1][order[0]]:
                break

    return matrix

#def Quick(matrix, order):

######### MAIN

while True:

    arquivo_entrada = input("Entre com o nome do arquivo de entrada: ") #pede ao usuário nome do arquivo de entrada
    if arquivo_entrada.lower() == "fim": #se usuário digitar "fim", termina o programa
        quit()

    arquivo_saida = input("\nEntre com o nome do arquivo de saída: ") #pede ao usuário nome do arquivo de saída
    if arquivo_saida.lower() == "fim":  # se usuário digitar "fim", termina o programa
        quit()

    while True:

        while True:

            ordem = input("\nInsira a ordem de classificação dos valores: ")
            if ordem.lower() == "fim":  # se usuário digitar "fim", termina o programa
                quit()

            lista_ordem = ordem.split(',')

            lista_ordem_int = list(map(int, lista_ordem))

            set_ordem = set(lista_ordem_int)

            try:
                if set_ordem <= {0, 1, 2}:
                    break
                else:
                    print("\nErro! Insira a ordem de clasificação corretamente. Exemplo: 1 ou 1,2 ou 0,2,3\n")
                    continue
            except:
                pass
        #PRINT INTERMEDIARIO
        print("Classificação da Ordem", lista_ordem_int)

        try:
            with open(arquivo_entrada, "r") as arq: #abre o arquivo

                linhas = arq.readlines()  #retorna uma lista que contém cada linha do arquivo como um item da lista

        except:
            print("\nErro na abertura do arquivo de entrada. Insira novamente o nome do arquivo.\n")
            break

        lista_separada = []
        for linha in linhas: #lê cada linha da lista "linhas"

            try:
                lin = linha[:len(linha) - 1]  # variável que recebe cada linha do arquivo de texto original como uma string
                v = linha.rstrip('\n').split(',')  # variável que recebe a linha acima e a transforma e
                lista_separada.append(v)

            except: pass

        #print(lista_separada)
        print(transforma_data(Bubble(transforma_data(lista_separada), lista_ordem_int)))
        final = transforma_data(Bubble(transforma_data(lista_separada), lista_ordem_int))

        with open(arquivo_saida, 'w') as filehandle:
            for listitem in final:
                filehandle.write('%s\n' % listitem)

        break
