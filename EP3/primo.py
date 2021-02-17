def proximo_primo(n): #função que devolve o próximo número primo a partir de um número n
    prox_primo = n + 1 #estabelece como possível próximo primo o número seguinte a n
    primo = True
    while True:
        for i in range(2, prox_primo):
            if prox_primo % i ==0: #verifica se é primo
                primo = False
                break
        if primo: # se for primo, retorn
            return prox_primo
        else: #se não for primo, continua procurando
            prox_primo = prox_primo + 1
            if prox_primo % 2 == 0:
                prox_primo = prox_primo + 1
            primo = True

print(proximo_primo(44))
