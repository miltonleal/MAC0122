class Duplas:

    #construtor da classe
    def __init__(self, p1=0, p2=0):
        self.primeiro = p1
        self.segundo = p2

    #método que soma os elementos
    def SomaDuplas(self, d1, d2):
        self.primeiro = d1.primeiro + d2.primeiro
        self.segundo = d1.segundo + d2.segundo

    def SubtraiDuplas(self, d1, d2):
        self.primeiro = d1.primeiro - d2.primeiro
        self.segundo = d1.segundo - d2.segundo

    #método que imprime
    def Mostre(self):
        print("/", self.primeiro, self.segundo, "/")

if __name__ == "__main__":

    x = Duplas(1,2)
    #print (vars(x))
    #x.Mostre()

    #x.SomaDuplas(3,4)
    y = Duplas(3,3)
    z = Duplas()
    z.SomaDuplas(x,y)
    z.Mostre()
    #p = Duplas()
    #p.SubtraiDuplas(x,y)
    #p.Mostre()