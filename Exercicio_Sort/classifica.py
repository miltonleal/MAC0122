# Nome: Milton Leal neto
# NUSP: 8973974
# Exercício III – 22/11/2020

def CLASSIFICA(TAB,ordem):

    def transforma_data(matrix):

        # função que transforma a data DD/MM/AAAA para AAAA/MM/DD
        # e também faz o reverso AAAA/MM/DD para DD/MM/AAAA)
        for i in range(len(matrix)):
            # lista que recebe a terceira coluna da tabela splitada em dia, mês e ano
            data = matrix[i][2].split("/")
            # substitui a terceira coluna da tabela pela lista data
            matrix[i][2] = data
            # troca elemento ANO pelo elemento DIA ou vice versa
            matrix[i][2][0], matrix[i][2][2] = matrix[i][2][2], matrix[i][2][0]
            # Transforma em string novamente no formato AAAA/MM/DD ou DD/MM/AAAA
            matrix[i][2] = matrix[i][2][0] + "/" + matrix[i][2][1] + "/" + matrix[i][2][2]

        return matrix

    def ordena(x,y,ordem):

        #se o primeiro elemento da coluna for menor
        if x[ordem[0]] < y[ordem[0]]:
            return -1
        # se o primeiro elemento da coluna for maior
        elif x[ordem[0]] > y[ordem[0]]:
            return 1
        # se o primeiro elemento da coluna for igual e a classificação é para duas colunas
        elif x[ordem[0]] == y[ordem[0]] and len(ordem) > 1:
            # se o segundo elemento da coluna for menor
            if x[ordem[1]] < y[ordem[1]]:
                return -1
            # se o segundo elemento da coluna for maior
            elif x[ordem[1]] > y[ordem[1]]:
                return 1
            # se o primeiro elemento da coluna for igual e a classificação é para três colunas
            elif x[ordem[1]] == y[ordem[1]] and len(ordem) > 2:
                # se o terceiro elemento da coluna for menor
                if x[ordem[2]] < y[ordem[2]]:
                    return -1
                # se o terceiro elemento da coluna for maior
                elif x[ordem[2]] > y[ordem[2]]:
                    return 1
                # se o terceiro elemento da coluna for igual
                elif x[ordem[2]] == y[ordem[2]]:
                    return 0
            else:
                return 0
        else:
            return 0

    def cria_chave(chave):
        # Classe que cria mecanismo de ordenação com base na chave de classificação
        class Key:
            def __init__(self, obj, *args):
                self.obj = obj

            def __lt__(self, other):
                return chave(self.obj, other.obj, ordem) < 0

            def __gt__(self, other):
                return chave(self.obj, other.obj, ordem) > 0

            def __eq__(self, other):
                return chave(self.obj, other.obj, ordem) == 0

        return Key

    #Chamada da função
    if 2 not in ordem: # se não houver classificação por data
        TAB.sort(key=cria_chave(ordena))
        return TAB
    else: # se houver classificação por data
        a = transforma_data(TAB) #transforma a data
        TAB.sort(key=cria_chave(ordena))
        b = transforma_data(TAB) #transforma a data
        return TAB
