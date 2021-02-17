class Duplas:

    #construtor da classe
    def __init__(self, p1, p2):
        self.primeiro = p1
        self.segundo = p2

    #Método que soma as duplas
    def SomaDuplas(self,d1, d2):
        pri = d1.primeiro + d2.primeiro
        seg = d1.segundo + d2.segundo
        return Duplas(pri, seg)

    def Mostre(param):
        print("/", param.primeiro, param.segundo, "/")



x = Duplas(1,2)
x.Mostre()

y = Duplas(0,1)
y.Mostre()

z = Duplas(0,0)
z.Mostre()

Duplas(0,0).SomaDuplas(x,y).Mostre()

z.SomaDuplas(Duplas(3,4),Duplas(3,5))
z.Mostre()

z = Duplas(0,0).SomaDuplas(Duplas(5,5),Duplas(6,6))
z.Mostre()


