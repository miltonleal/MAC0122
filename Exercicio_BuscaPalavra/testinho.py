from consertandoAdap import BoyerMoore1, Adaptado

### TESTE 1

print("=== TESTE 1 ===\n")
b = "abc"
a = "abc"
print("B =",b)
print("A =",a)
print("\n*** BoyerMoore 1 ***\n")
i, j = BoyerMoore1(a, b)
print("Deslocamentos")
if 1 == j:
    print("OK")
print("\nVezes")
if 1 == i:
    print("OK")

print("\n*** Adaptado ***\n")
p, q = Adaptado(a, b)
if 1 == q:
    print("OK")
print("\nVezes")
if 1 == p:
    print("OK")

### TESTE 2

print("\n=== TESTE 2 ===\n")
b = "abacacbabcdcdabd"
a = "abcd"
print("B =",b)
print("A =",a)
print("\n*** BoyerMoore 1 ***\n")
i, j = BoyerMoore1(a, b)
print("Deslocamentos")
if 4 == j:
    print("OK")
print("\nVezes")
if 1 == i:
    print("OK")

print("\n*** Adaptado ***\n")
p, q = Adaptado(a, b)
if 13 == q:
    print("OK")
print("\nVezes")
if 1 == p:
    print("OK")

### TESTE 3

print("\n=== TESTE 3 ===\n")
b = "abacacbabcdcdabd"
a = "aba"
print("B =",b)
print("A =",a)
print("\n*** BoyerMoore 1 ***\n")
i, j = BoyerMoore1(a, b)
print("Deslocamentos")
if 6 == j:
    print("OK")
print("\nVezes")
if 1 == i:
    print("OK")

print("\n*** Adaptado ***\n")
p, q = Adaptado(a, b)
if 14 == q:
    print("OK")
print("\nVezes")
if 1 == p:
    print("OK")

### TESTE 4

print("\n=== TESTE 4 ===\n")
b = "abacabcaabcaba"
a = "bca"
print("B =",b)
print("A =",a)
print("\n*** BoyerMoore 1 ***\n")
print("\n*** BoyerMoore 1 ***\n")
i, j = BoyerMoore1(a, b)
print("Deslocamentos")
if 5 == j:
    print("OK")
print("\nVezes")
if 2 == i:
    print("OK")

print("\n*** Adaptado ***\n")
p, q = Adaptado(a, b)
if 12 == q:
    print("OK")
print("\nVezes")
if 2 == p:
    print("OK")

### TESTE 5

print("\n=== TESTE 5 ===\n")
b = "abacabcaabcaba"
a = "ababa"
print("B =",b)
print("A =",a)
print("\n*** BoyerMoore 1 ***\n")
i, j = BoyerMoore1(a, b)
print("Deslocamentos")
if 7 == j:
    print("OK")
print("\nVezes")
if 0 == i:
    print("OK")

print("\n*** Adaptado ***\n")
p, q = Adaptado(a, b)
if 10 == q:
    print("OK")
print("\nVezes")
if 0 == p:
    print("OK")

### TESTE 6

print("\n=== TESTE 6 ===\n")
b = "abacabcaabcaba"
a = "abx"
print("B =",b)
print("A =",a)
print("\n*** BoyerMoore 1 ***\n")
i, j = BoyerMoore1(a, b)
print("Deslocamentos")
if 4 == j:
    print("OK")
print("\nVezes")
if 0 == i:
    print("OK")

print("\n*** Adaptado ***\n")
p, q = Adaptado(a, b)
if 12 == q:
    print("OK")
print("\nVezes")
if 0 == p:
    print("OK")

### TESTE 7

print("\n=== TESTE 7 ===\n")
b = "abacabcaabcaba"
a = "abaca"
print("B =",b)
print("A =",a)
print("\n*** BoyerMoore 1 ***\n")
i, j = BoyerMoore1(a, b)
print("Deslocamentos")
if 4 == j:
    print("OK")
print("\nVezes")
if 1 == i:
    print("OK")

print("\n*** Adaptado ***\n")
p, q = Adaptado(a, b)
if 10 == q:
    print("OK")
print("\nVezes")
if 1 == p:
    print("OK")

### TESTE 8

print("\n=== TESTE 8 ===\n")
b = "abacabcaabcaba"
a = "xyzt"
print("B =",b)
print("A =",a)
print("\n*** BoyerMoore 1 ***\n")
i, j = BoyerMoore1(a, b)
print("Deslocamentos")
if 3 == j:
    print("OK")
print("\nVezes")
if 0 == i:
    print("OK")

print("\n*** Adaptado ***\n")
p, q = Adaptado(a, b)
if 11 == q:
    print("OK")
print("\nVezes")
if 0 == p:
    print("OK")

### TESTE 9

print("\n=== TESTE 9 ===\n")
b = "ababacbbbababbab"
a = "abb"
print("B =",b)
print("A =",a)
print("\n*** BoyerMoore 1 ***\n")
i, j = BoyerMoore1(a, b)
print("Deslocamentos")
if 8 == j:
    print("OK")
print("\nVezes")
if 1 == i:
    print("OK")

print("\n*** Adaptado ***\n")
p, q = Adaptado(a, b)
if 9 == q:
    print("OK")
print("\nVezes")
if 1 == p:
    print("OK")

### TESTE 10

print("\n=== TESTE 10 ===\n")
b = "ababacbbbababbab"
a = "aab"
print("B =",b)
print("A =",a)
print("\n*** BoyerMoore 1 ***\n")
i, j = BoyerMoore1(a, b)
print("Deslocamentos")
if 10 == j:
    print("OK")
print("\nVezes")
if 0 == i:
    print("OK")

print("\n*** Adaptado ***\n")
p, q = Adaptado(a, b)
if 11 == q:
    print("OK")
print("\nVezes")
if 0 == p:
    print("OK")

### TESTE 11

print("\n=== TESTE 11 ===\n")
b = "ababacbbbababbab"
a = "aabb"
print("B =",b)
print("A =",a)
print("\n*** BoyerMoore 1 ***\n")
i, j = BoyerMoore1(a, b)
print("Deslocamentos")
if 7 == j:
    print("OK")
print("\nVezes")
if 0 == i:
    print("OK")

print("\n*** Adaptado ***\n")
p, q = Adaptado(a, b)
if 8 == q:
    print("OK")
print("\nVezes")
if 0 == p:
    print("OK")

### TESTE 12

print("\n=== TESTE 12 ===\n")
b = "ababacbbbababbab"
a = "bbcaabb"
print("B =",b)
print("A =",a)
print("\n*** BoyerMoore 1 ***\n")
i, j = BoyerMoore1(a, b)
print("Deslocamentos")
if 6 == j:
    print("OK")
print("\nVezes")
if 0 == i:
    print("OK")

print("\n*** Adaptado ***\n")
p, q = Adaptado(a, b)
if 6 == q:
    print("OK")
print("\nVezes")
if 0 == p:
    print("OK")

