# Exercícios IV - Inserção em tabela ordenada e busca binária

from inserebb import InsereBB

# testes
t = [1, 10, 100]
print("original:", t)

# a esquerda
a, b = InsereBB(t, 0)
print("\nInsere 0000:", "pos = ",a, "comp = ", b, " - ",  t)
if t != [0,1,10,100]: print("* * * Erro * * *")
# a direita
a, b = InsereBB(t, 1000)
print("\ninsere 1000:", "pos = ",a, "comp = ", b, " - ",  t)
if t != [0,1,10,100,1000]: print("* * * Erro * * *")

# no meio
a, b = InsereBB(t, 5)
print("\ninsere 0005:", "pos = ",a, "comp = ", b, " - ",  t)
if t != [0,1,5,10,100,1000]: print("* * * Erro * * *")
# no meio
a, b = InsereBB(t, 50)
print("\ninsere 0050:", "pos = ",a, "comp = ", b, " - ",  t)
if t != [0,1,5,10,50,100,1000]: print("* * * Erro * * *")
# no meio
a, b = InsereBB(t, 500)
print("\ninsere 0500:", "pos = ",a, "comp = ", b, " - ",  t)
if t != [0,1,5,10,50,100,500,1000]: print("* * * Erro * * *")
# iguais
a, b = InsereBB(t, 0)
print("\ninsere 0000:", "pos = ",a, "comp = ", b, " - ",  t)
if t != [0,0,1,5,10,50,100,500,1000]: print("* * * Erro * * *")
# iguais
a, b = InsereBB(t, 1000)
print("\ninsere 1000:", "pos = ",a, "comp = ", b, " - ",  t)
if t != [0,0,1,5,10,50,100,500,1000,1000]: print("* * * Erro * * *")
# iguais
a, b = InsereBB(t, 100)
print("\ninsere 0100:", "pos = ",a, "comp = ", b, " - ",  t)
if t != [0,0,1,5,10,50,100,100,500,1000,1000]: print("* * * Erro * * *")
