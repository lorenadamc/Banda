from random import randint, uniform,random
class instrumento:
    def tocar(self):
        return("Tocando Instrumento")
    def preparar(self):
        return("Preparando instrumento")
class guitarra(instrumento):
    nombre = 'guitarra'
    def __init__(self):
        self = self
class bajo(instrumento):
    nombre = 'bajo'
    def __init__(self):
        self = self        
class piano(instrumento):
    nombre = 'piano'
    def __init__(self):
        self = self
class caja (instrumento):
    nombre = 'caja'
    def __init__(self):
        self = self
class flauta (instrumento):
    nombre = 'flauta'
    def __init__(self):
        self = self
class acordeon (instrumento):
    nombre = 'acordeon'
    def __init__(self):
        self = self
class gaita (instrumento):
    nombre = 'gaita'
    def __init__(self):
        self = self
class guacharaca (instrumento):
    nombre = 'guacharaca'
    def __init__(self):
        self = self
class llamador (instrumento):
    nombre = 'llamador'
    def __init__(self):
        self = self
class bateria (instrumento):
    nombre = 'bateria'
    def __init__(self):
        self = self        
class banda():
    def nuevabanda(self,numeromusicos):
        instrumentos = [guitarra(),bajo(),piano(),caja(),flauta(),acordeon(),gaita(),guacharaca(),llamador(),bateria()]
        banda = []
        for i in range(0,numeromusicos):
            ins = randint(1,4)
            obj =instrumentos[ins]
            banda.append(obj)
        print(-Ba)
        for i in banda:

        return banda
    def afinarbanda(self, banda, numeromusicos ):
        for i in banda:
            print(i.preparar(),i.nombre)
    def tocarbanda(self, banda, numeromusiscos):
        print("Tocando")
           
numeromusicos = randint(1,10)
banda = banda()
b = banda.nuevabanda(numeromusicos)
print("Afinar")
banda.afinarbanda(b,numeromusicos)






