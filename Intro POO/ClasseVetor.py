class Vetor:

    def __init__(self,d):
        self._coords = [0] * d #cria vetor de dimensão = d

    def __len__(self): #retorna a dimensão do vetor
        return len(self._coords)

    def __getitem__(self, j):
        return self._coords[j]

    def __setitem__(self, j, val):
        self._coords[j] = val

    def __add__(self,v):
        if len(self) != len(v):
            raise ValueError ("dimensões devem ser as mesmas")

        result = Vetor(len(self))
        for j in range (len(self)):
            result[j] = self[j] + v[j]
        return result

    def __eq__(self, v):
        return self._coords == v._coords

    def __ne__(self,v):
        return not self == v

    def imprime(self):
        print (self._coords)

    def __str__(self):
        return str(self._coords)

v1 = Vetor(4)
v2 = Vetor(4)
v2[0] = 1

print (v2,v1,v2)
