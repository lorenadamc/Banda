from random import randint, uniform,random
def nuevabanda():
        r = randint(5,10)
        instrumentos = ["guitarra","bajo","piano","caja","flauta","acordeon","gaita","guacharaca","llamador","bateria"]
        banda = []
        for i in range(0,r):
            ins = randint(0,9)
            obj =instrumentos[ins]
            banda.append(obj)
        j = 1
        return banda
