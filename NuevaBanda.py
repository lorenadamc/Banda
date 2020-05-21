from random import randint, uniform,random
def nuevabanda():
        r = randint(5,10)
        instrumentos = ["Guitarra","Bajo","Piano","Maracas","Flauta","Acordeon","Gaita","Guacharaca","Llamador","Bateria"]
        banda = []
        for i in range(0,r):
            ins = randint(0,9)
            obj =instrumentos[ins]
            banda.append(obj)
        j = 1
        return banda
