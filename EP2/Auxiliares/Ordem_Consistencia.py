
while True:

    ordem = input("Insira a order de classificação dos valores: ")
    try:
        if ordem == "1" or ordem == "2" or ordem == "3" or ordem == "1,2" or ordem == "1,3" or \
            ordem == "2,3" or ordem == "2,1" or ordem == "3,1" or ordem == "3,2" or ordem == "1,2,3" \
                or ordem == "1,3,2" or ordem == "2,1,3" or ordem == "2,3,1" or ordem == "3,2,1" or ordem == "3,1,2":
            lista_Ordem = ordem.split(",")
            break

        else:
            print("\nErro! Insira a order de clasificação corretamente. Exemplo: 1 ou 1,2 ou 1,2,3\n")
            continue
    except:
        pass

print(lista_Ordem)




