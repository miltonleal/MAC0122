# Nome: Milton Leal neto
# NUSP: 8973974
# Exercício I – 01/10/2020

class Fração:

    def __init__(self, numerador = 0, denominador = 1):

        #Consistência dos dados de entrada
        if denominador == 0:
            raise ZeroDivisionError("Denominador não pode ser igual a zero.")

        if type(numerador) != int or type(denominador) != int:
            raise TypeError("Entrada não numérica. Insira apenas números inteiros.")

        mdc = Fração.max_divisor_comum (numerador, denominador) #chama a função do MDC

        self.num = numerador // mdc #constrói o numerador da fração
        self.den = denominador // mdc #constrói o denominador da fração

    def __str__(self): #redefine o print

        return str(self.num) + "/" + str(self.den)

    def __add__(self, fracao2): #redefine o operador +

        Fração.verifica_tipo(fracao2) #chama a função que verifica se o segundo parâmetro é da classe Fração

        novo_numerador = self.num * fracao2.den + self.den * fracao2.num
        novo_denominador = self.den * fracao2.den

        return Fração(novo_numerador, novo_denominador)

    def __sub__(self, fracao2): #redefine o operador -

        Fração.verifica_tipo(fracao2)

        novo_numerador = self.num * fracao2.den - self.den * fracao2.num
        novo_denominador = self.den * fracao2.den

        return Fração(novo_numerador, novo_denominador)

    def __mul__(self, fracao2): #redefine o operador *

        Fração.verifica_tipo(fracao2)

        novo_numerador = self.num * fracao2.num
        novo_denominador = self.den * fracao2.den

        return Fração(novo_numerador, novo_denominador)

    def __truediv__(self, fracao2): #redefine o operador /

        Fração.verifica_tipo(fracao2)

        novo_numerador = self.num * fracao2.den
        novo_denominador = self.den * fracao2.num

        return Fração(novo_numerador, novo_denominador)

    def __pow__(self, expoente): #redefine o operador **

        if expoente == 0:
            return Fração(1,1)

        elif expoente > 0:

            novo_numerador = self.num
            novo_denominador = self.den

            for i in range (1, expoente):

                novo_numerador *= self.num
                novo_denominador *= self.den

            return Fração(novo_numerador, novo_denominador)

        else: #caso do expoente ser negativo
            novo_numerador = self.den
            novo_denominador = self.num

            for i in range (1, expoente*(-1)):

                novo_numerador *= self.den
                novo_denominador *= self.num

            return Fração(novo_numerador, novo_denominador)

    def __eq__(self, fracao2): #redefine o operador ==

        Fração.verifica_tipo(fracao2)

        return (self.num * fracao2.den) == (self.den * fracao2.num)

    def __ne__(self, fracao2): #redefine o operador !=

        Fração.verifica_tipo(fracao2)

        return (self.num * fracao2.den) != (self.den * fracao2.num)

    def __lt__(self, fracao2): #redefine o operador <

        Fração.verifica_tipo(fracao2)

        return self.num * fracao2.den < self.den * fracao2.num

    def __le__(self, fracao2): #redefine o operador <=

        Fração.verifica_tipo(fracao2)

        return self.num * fracao2.den <= self.den * fracao2.num

    def __gt__(self, fracao2): #redefine o operador >

        Fração.verifica_tipo(fracao2)

        return self.num * fracao2.den > self.den * fracao2.num

    def __ge__(self, fracao2): #redefine o operador >=

        Fração.verifica_tipo(fracao2)

        return self.num * fracao2.den >= self.den * fracao2.num

    def verifica_tipo (fracao2): #função que verifica se o parâmetro é do tipo Fração

        if type(fracao2) != Fração:
            raise TypeError("Tipos diferentes")

    def max_divisor_comum (numerador, denominador): #função que encontra o MDC entre as frações

        while numerador % denominador != 0:
            num_atual = numerador
            den_atual = denominador

            numerador = den_atual
            denominador = num_atual % den_atual

        return denominador

