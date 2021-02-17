class Duplas:

    #construtor da classe
    def __init__(self, p1=0, p2=0):
        self.primeiro = p1
        self.segundo = p2

    #retorna a soma de dois elementos da classe
    def __add__(d1, d2):
        pri = d1.primeiro + d2.primeiro
        seg = d1.segundo + d2.segundo
        return Duplas(pri,seg)

    #transforma uma dupla em string para poder imprimir
    def __str__(self):
        return "/" + str(self.primeiro) + " " + str(self.segundo) + "/"


x = Duplas (3,4)
print (x)

y = Duplas(1,2)

z = x + y + x + Duplas(10,20)
print (z+y+Duplas(-130))