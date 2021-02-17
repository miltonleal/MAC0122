from buscapalavra import BoyerMoore1, Adaptado

### TESTE 1

print("=== TESTE 1 ===\n")
b = "abc"
a = "abc"
print("B =",b)
print("A =",a)
print("\n*** BoyerMoore 1 ***\n")
i, j = BoyerMoore1(a, b)
print("Deslocamentos")
print("Correto =", 1)
print("Obtido =", j)
print("\nVezes")
print("Correto =", 1)
print("Obtido =", i)

print("\n*** Adaptado ***\n")
p, q = Adaptado(a, b)
print("Deslocamentos")
print("Correto =", 1)
print("Obtido =", q)
print("\nVezes")
print("Correto =", 1)
print("Obtido =", p)

### TESTE 2

print("\n=== TESTE 2 ===\n")
b = "abacacbabcdcdabd"
a = "abcd"
print("B =",b)
print("A =",a)
print("\n*** BoyerMoore 1 ***\n")
i, j = BoyerMoore1(a, b)
print("Deslocamentos")
print("Correto =", 4)
print("Obtido =", j)
print("\nVezes")
print("Correto =", 1)
print("Obtido =", i)

print("\n*** Adaptado ***\n")
p, q = Adaptado(a, b)
print("Deslocamentos")
print("Correto =", 13)
print("Obtido =", q)
print("\nVezes")
print("Correto =", 1)
print("Obtido =", p)

### TESTE 3

print("\n=== TESTE 3 ===\n")
b = "abacacbabcdcdabd"
a = "aba"
print("B =",b)
print("A =",a)
print("\n*** BoyerMoore 1 ***\n")
i, j = BoyerMoore1(a, b)
print("Deslocamentos")
print("Correto =", 6)
print("Obtido =", j)
print("\nVezes")
print("Correto =", 1)
print("Obtido =", i)

print("\n*** Adaptado ***\n")
p, q = Adaptado(a, b)
print("Deslocamentos")
print("Correto =", 14)
print("Obtido =", q)
print("\nVezes")
print("Correto =", 1)
print("Obtido =", p)

### TESTE 4

print("\n=== TESTE 4 ===\n")
b = "abacabcaabcaba"
a = "bca"
print("B =",b)
print("A =",a)
print("\n*** BoyerMoore 1 ***\n")
i, j = BoyerMoore1(a, b)
print("Deslocamentos")
print("Correto =", 5)
print("Obtido =", j)
print("\nVezes")
print("Correto =", 2)
print("Obtido =", i)

print("\n*** Adaptado ***\n")
p, q = Adaptado(a, b)
print("Deslocamentos")
print("Correto =", 12)
print("Obtido =", q)
print("\nVezes")
print("Correto =", 2)
print("Obtido =", p)

### TESTE 5

print("\n=== TESTE 5 ===\n")
b = "abacabcaabcaba"
a = "ababa"
print("B =",b)
print("A =",a)
print("\n*** BoyerMoore 1 ***\n")
i, j = BoyerMoore1(a, b)
print("Deslocamentos")
print("Correto =", 7)
print("Obtido =", j)
print("\nVezes")
print("Correto =", 0)
print("Obtido =", i)

print("\n*** Adaptado ***\n")
p, q = Adaptado(a, b)
print("Deslocamentos")
print("Correto =", 10)
print("Obtido =", q)
print("\nVezes")
print("Correto =", 0)
print("Obtido =", p)

### TESTE 6

print("\n=== TESTE 6 ===\n")
b = "abacabcaabcaba"
a = "abx"
print("B =",b)
print("A =",a)
print("\n*** BoyerMoore 1 ***\n")
i, j = BoyerMoore1(a, b)
print("Deslocamentos")
print("Correto =", 4)
print("Obtido =", j)
print("\nVezes")
print("Correto =", 0)
print("Obtido =", i)

print("\n*** Adaptado ***\n")
p, q = Adaptado(a, b)
print("Deslocamentos")
print("Correto =", 12)
print("Obtido =", q)
print("\nVezes")
print("Correto =", 0)
print("Obtido =", p)

### TESTE 7

print("\n=== TESTE 7 ===\n")
b = "abacabcaabcaba"
a = "abaca"
print("B =",b)
print("A =",a)
print("\n*** BoyerMoore 1 ***\n")
i, j = BoyerMoore1(a, b)
print("Deslocamentos")
print("Correto =", 4)
print("Obtido =", j)
print("\nVezes")
print("Correto =", 1)
print("Obtido =", i)

print("\n*** Adaptado ***\n")
p, q = Adaptado(a, b)
print("Deslocamentos")
print("Correto =", 10)
print("Obtido =", q)
print("\nVezes")
print("Correto =", 1)
print("Obtido =", p)

### TESTE 8

print("\n=== TESTE 8 ===\n")
b = "abacabcaabcaba"
a = "xyzt"
print("B =",b)
print("A =",a)
print("\n*** BoyerMoore 1 ***\n")
i, j = BoyerMoore1(a, b)
print("Deslocamentos")
print("Correto =", 3)
print("Obtido =", j)
print("\nVezes")
print("Correto =", 0)
print("Obtido =", i)

print("\n*** Adaptado ***\n")
p, q = Adaptado(a, b)
print("Deslocamentos")
print("Correto =", 11)
print("Obtido =", q)
print("\nVezes")
print("Correto =", 0)
print("Obtido =", p)

### TESTE 9

print("\n=== TESTE 9 ===\n")
b = "ababacbbbababbab"
a = "abb"
print("B =",b)
print("A =",a)
print("\n*** BoyerMoore 1 ***\n")
i, j = BoyerMoore1(a, b)
print("Deslocamentos")
print("Correto =", 8)
print("Obtido =", j)
print("\nVezes")
print("Correto =", 1)
print("Obtido =", i)

print("\n*** Adaptado ***\n")
p, q = Adaptado(a, b)
print("Deslocamentos")
print("Correto =", 9)
print("Obtido =", q)
print("\nVezes")
print("Correto =", 1)
print("Obtido =", p)

### TESTE 10

print("\n=== TESTE 10 ===\n")
b = "ababacbbbababbab"
a = "aab"
print("B =",b)
print("A =",a)
print("\n*** BoyerMoore 1 ***\n")
i, j = BoyerMoore1(a, b)
print("Deslocamentos")
print("Correto =", 10)
print("Obtido =", j)
print("\nVezes")
print("Correto =", 0)
print("Obtido =", i)

print("\n*** Adaptado ***\n")
p, q = Adaptado(a, b)
print("Deslocamentos")
print("Correto =", 11)
print("Obtido =", q)
print("\nVezes")
print("Correto =", 0)
print("Obtido =", p)

### TESTE 11

print("\n=== TESTE 11 ===\n")
b = "ababacbbbababbab"
a = "aabb"
print("B =",b)
print("A =",a)
print("\n*** BoyerMoore 1 ***\n")
i, j = BoyerMoore1(a, b)
print("Deslocamentos")
print("Correto =", 7)
print("Obtido =", j)
print("\nVezes")
print("Correto =", 0)
print("Obtido =", i)

print("\n*** Adaptado ***\n")
p, q = Adaptado(a, b)
print("Deslocamentos")
print("Correto =", 8)
print("Obtido =", q)
print("\nVezes")
print("Correto =", 0)
print("Obtido =", p)

### TESTE 12

print("\n=== TESTE 12 ===\n")
b = "ababacbbbababbab"
a = "bbcaabb"
print("B =",b)
print("A =",a)
print("\n*** BoyerMoore 1 ***\n")
i, j = BoyerMoore1(a, b)
print("Deslocamentos")
print("Correto =", 6)
print("Obtido =", j)
print("\nVezes")
print("Correto =", 0)
print("Obtido =", i)

print("\n*** Adaptado ***\n")
p, q = Adaptado(a, b)
print("Deslocamentos")
print("Correto =", 6)
print("Obtido =", q)
print("\nVezes")
print("Correto =", 0)
print("Obtido =", p)