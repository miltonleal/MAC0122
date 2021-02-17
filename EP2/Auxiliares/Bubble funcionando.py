#Método Bolha

#matrix = [['32343245100', 'Jose de Castro', '10/12/2001'], ['43456790236', 'Maria das Dores e Silva', '05/01/2005'], ['22589349476', 'Antonio Paixao dos Santos', '30/05/2012'], ['32343245111', 'Jose de Castro', '10/12/2010'], ['43456790222', 'Maria da Silva', '25/01/2015'], ['22589348876', 'Antonio dos Santos', '30/06/2002'], ['32343245144', 'Jose de Campos', '15/15/2007'], ['43453330236', 'Maria da Rocha', '27/11/2000'], ['22555549476', 'Armando da Silva', '20/06/2002 ']]

#matrix = [["3", "Mary", "2017"], ["3", "Mary", "2016"], ["1", "Mary", "2017"], ["5","John", "2017"], ["0", "Mary", "2017"]]

matrix = [["2", "Maria", "0"], ["1", "Maria","1" ], ["5", "Joao", "2"], ["6", "Abreu", "2"], ["0", "Maria", "3"]]

#matrix = [["2", "Maria", '10/12/2001'], ["1", "Maria", '8/12/2001'], ["5", "Joao", '10/12/2003']]
order = [2]

def Bubble(matrix, order):

    n = len(matrix)

    for i in range(1, n):

        j = i
        while j > 0:

            if matrix[j][order[0]] < matrix[j - 1][order[0]]:
                matrix[j], matrix[j - 1] = matrix[j - 1], matrix[j]
                j = j - 1
                continue

            elif matrix[j][order[0]] == matrix[j - 1][order[0]]:

                if len(order) == 1:
                    break

                if len(order) == 2:

                    if matrix[j][order[1]] < matrix[j-1][order[1]]:
                        matrix[j], matrix[j - 1] = matrix[j - 1], matrix[j]
                        j = j - 1

                if len(order) == 3:

                    if matrix[j][order[1]] < matrix[j-1][order[1]]:
                        matrix[j], matrix[j - 1] = matrix[j - 1], matrix[j]
                        j = j - 1
                        if j == 0:
                            break

                    elif matrix[j][order[1]] == matrix[j-1][order[1]]:

                        if matrix[j][order[2]] < matrix[j-1][order[2]]:
                            matrix[j], matrix[j - 1] = matrix[j - 1], matrix[j]
                            j = j - 1
                            if j == 0:
                                break

                    elif matrix[j][order[1]] > matrix[j - 1][order[1]]:
                        break

            elif matrix[j][order[0]] > matrix[j - 1][order[0]]:
                break
    return matrix

print(Bubble(matrix,order))


