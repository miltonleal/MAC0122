#import seaborn as sns
#import matplotlib.pyplot as plt
from collections import Counter

def main():

    global lista_valores_ascii
    while True:

        #Solicita o nome dos arquivos

        arquivo_entrada = input("\nNome do arquivo de origem: ") #pede ao usuário nome do arquivo de entrada
        if arquivo_entrada.lower() == "fim": #se usuário digitar "fim", termina o programa
            quit()

        while True:

            #tenta abrir o arquivo de entrada
            try:
                with open(arquivo_entrada, "r") as arq: #abre o arquivo

                    linhas = arq.readlines()  #retorna uma lista que contém cada linha do arquivo como um item da lista
            except:
                print("\nErro na abertura do arquivo de entrada. Insira novamente o nome do arquivo.")
                break

            lista_original = [] #cria lista para receber o conteúdo da lista original
            for linha in linhas: #lê cada linha da lista "linhas"

                try:
                    lin = linha[:len(linha) - 1]  #variável que recebe cada linha do arquivo de texto original como uma string
                    v = linha.rstrip('\n').split(',') #variável que recebe a linha acima e a transforma e
                    #v[1] = linha.rstrip('\n').split()
                    lista_original.append(v)

                except: pass

            print("lista separada", lista_original)

            lista_nomes_separados =[]
            for i in range(len(lista_original)):
                lista_nomes_separados.append(lista_original[i][1].split())
            print(lista_nomes_separados)

            lista_valores_ascii = []
            for j in range (len(lista_nomes_separados)):
                for i in range(4):
                    s = 0
                    # s conterá a soma dos valores numéricos dos caracteres

                    for letter in lista_nomes_separados[j][i]:
                        #print(j)
                        s = s + ord(letter)
                    lista_valores_ascii.append(s)

            break

        lista_valores_ascii.sort()
        print("lista valores ascii",lista_valores_ascii)

        a = dict(Counter(lista_valores_ascii))
        count2 = 0
        for i in a.values():
            if i == 1:
                count2 +=1
        print("elementos únicos na lista de valores ascii =", count2)

        # lista_repeticoes =[]
        # for i in a.values():
        #     lista_repeticoes.append(i)
        # lista_repeticoes.sort()
        # max_repeticoes = lista_repeticoes[len(lista_repeticoes)-1]
        # print("maior numero de repetições =", max_repeticoes)
        # #print(a)
        #
        # print("tamanho ótimo da tabela M = ", 2*(max_repeticoes*(len(lista_valores_ascii))))


        soma = 0
        for i in range(len(lista_valores_ascii)):
            soma += lista_valores_ascii[i]

        media = soma//len(lista_valores_ascii)
        mediana = lista_valores_ascii[len(lista_valores_ascii) // 2]
        menor = lista_valores_ascii[0]
        maior = lista_valores_ascii[len(lista_valores_ascii)-1]
        variacao = maior - menor


        #print("media =", media)
        #print("mediana =", mediana)
        print("menor =", menor)
        print("maior =", maior)
        print("range =", variacao)

        #depois da funcao
        lista_hash = []
        # lista_modulo = [10,50,100,200,400,600,650, 700, 704, 705,706, 707, 720, 800,1000,1500,2000,2500,3000,3500,7000]
        # for j in lista_modulo:
        for i in range (len(lista_valores_ascii)):
            lista_hash.append(lista_valores_ascii[i] % (variacao+1))
        lista_hash.sort()
        print("lista hash = ", lista_hash)

        count = 0
        for i in range(len(lista_hash)):
            b = lista_hash.count(lista_hash[i])
            if b != 1:
                continue
            count += 1
            b = 0
        print("elementos únicos na lista de hashes =", count)
        print("tamanho da lista =", len(lista_hash))
        #lista_hash=[]
        #print(lista_hash[i], "numero de ocorrencias", lista_hash.count(lista_hash[i]))

        #grafico = sns.displot(lista_hash)
        #plt.xlim([0,800])
        #plt.xlim([0,800])
        #plt.show()

        #break

main()

