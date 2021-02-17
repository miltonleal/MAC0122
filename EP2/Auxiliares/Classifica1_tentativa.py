#Método Bolha

c = [['32343245100', 'Jose de Castro', '10/12/2001'], ['43456790236', 'Maria das Dores e Silva', '05/01/2005'], ['22589349476', 'Antonio Paixao dos Santos', '30/05/2012'], ['32343245111', 'Jose de Castro', '10/12/2010'], ['43456790222', 'Maria da Silva', '25/01/2015'], ['22589348876', 'Antonio dos Santos', '30/06/2002'], ['32343245144', 'Jose de Campos', '15/15/2007'], ['43453330236', 'Maria da Rocha', '27/11/2000'], ['22555549476', 'Armando da Silva', '20/06/2002 ']]

#c = [["3", "Maria", "2017"], ["3", "Maria", "2016"], ["1", "Maria", "2017"], ["5","João", "2017"], ["0", "Maria", "2017"]]
#c = [["3", "Maria"], ["3", "Maria"]]

ordem2 = [1]

#def Classifica1(tab, ordem):
def Bolha(a, ordem):
    n = len(a)
    # i = 1, 2, ..., n - 1
    for i in range(1, n):
        # sobe com a[i] até encontrar o lugar adequado
        j = i
        while j > 0 and a[j][ordem[0]] < a[j - 1][ordem[0]]: #coluna domeio
        # troca com o seu vizinho
                a[j], a[j - 1] = a[j - 1], a[j]
        # continua subindo
                j = j - 1
    print(a)

    if len(ordem2) == 2:
        for i in range(1, n):

            j = i
            while j > 0:
                if a[j][ordem[0]] == a[j - 1][ordem[0]] and a[j][ordem[1]] < a[j-1][ordem[1]]: #analisa a primeira coluna
                    a[j], a[j - 1] = a[j - 1], a[j]
                j = j - 1

        print(a)

    if len(ordem2) == 3:

        for i in range(1, n):

            j = i
            while j > 0:
                if a[j][ordem[0]] == a[j - 1][ordem[0]] and a[j][ordem[1]] == a[j - 1][ordem[1]] and a[j][ordem[2]] < a[j - 1][ordem[2]]: #analisa a terceira coluna
                    a[j], a[j - 1] = a[j - 1], a[j]
                j = j - 1
        print(a)

    return a

print(Bolha(c,ordem2))


