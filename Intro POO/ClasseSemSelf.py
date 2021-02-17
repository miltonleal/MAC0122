class com_init:

    def __init__(outro, valor):
        outro.val = valor

    def f (a,b,self):
        print("entrou em f1:", a.val, b.val, self.val)

if __name__ == "__main__":

    x = com_init(-5)
    y = com_init(-4)
    z = com_init(-3)

    y.f(x,x)