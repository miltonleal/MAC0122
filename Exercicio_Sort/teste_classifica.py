from classifica import CLASSIFICA
import time

def main():

    print("*** CLASSIFICADOR DE TABELAS ***")
    while True:

        arquivo_entrada = input("\nInsira o nome do arquivo de entrada: ") #pede ao usuário nome do arquivo de entrada
        if arquivo_entrada.lower() == "fim": #se usuário digitar "fim", termina o programa
            quit()

        arquivo_saida = input("\nInsira o nome do arquivo de saída: ") #pede ao usuário nome do arquivo de saída
        if arquivo_saida.lower() == "fim":  # se usuário digitar "fim", termina o programa
            quit()

        while True:

            while True:

                ordem = input("\nInsira a ordem de classificação dos valores: ")
                if ordem.lower() == "fim":  # se usuário digitar "fim", termina o programa
                    quit()

                lista_ordem = ordem.split(',')

                set_ordem = set(lista_ordem)

                try:
                    if set_ordem <= {"0", "1", "2"}:
                        break
                    else:
                        print("\nErro! Insira a ordem de clasificação corretamente. Exemplo: 1 ou 1,2 ou 0,2,3")
                        continue
                except:
                    pass

            lista_ordem_int = list(map(int, lista_ordem))

            #PRINT INTERMEDIARIO

            try:
                with open(arquivo_entrada, "r") as arq: #abre o arquivo

                    linhas = arq.readlines()  #retorna uma lista que contém cada linha do arquivo como um item da lista

            except:
                print("\nErro na abertura do arquivo de entrada. Insira novamente o nome do arquivo.")
                break

            print("\nOrdem de classificação:", ','.join(map(str, lista_ordem_int)))

            lista_separada = []
            for linha in linhas: #lê cada linha da lista "linhas"

                try:
                    lin = linha[:len(linha) - 1]  # variável que recebe cada linha do arquivo de texto original como uma string
                    v = linha.rstrip('\n').split(',')  # variável que recebe a linha acima e a transforma e
                    lista_separada.append(v)

                except: pass

            lista_sort = lista_separada.copy()


            start = time.process_time()
            b_sort = CLASSIFICA(lista_sort, lista_ordem_int)
            print("Tempo de classificação - Sort = ", time.process_time() - start)

            with open(arquivo_saida, 'w') as filehandle:
                # add all items from b_bubble
                filehandle.write('\nTabela classificada pelo algoritmo Sort\n\n')
                for listitem in b_sort:
                    #filehandle.write(', '.join(map(str, b_bubble)))
                    filehandle.write('%s\n' % ', '.join(map(str, listitem)))

            break



main ()
