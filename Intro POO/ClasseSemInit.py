class sem_init:

    def f1(x,y):
        print ("entrou em f1:", x, y)

    def f2(a,self,b):
        print("entrou em f2:", a, self, b)


sem_init.f1(5,4)
sem_init.f2(1,2,3)