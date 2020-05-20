from random import randint, uniform,random
class instrumento:
    def tocar(self):
        return("Tocando Instrumento")
    def preparar(self):
        return("Preparando instrumento")
class guitarra(instrumento):
    nombre = 'Guitarra'
    def __init__(self):
        pass
class bajo(instrumento):
    nombre = 'Bajo'
    def __init__(self):
        pass
class piano(instrumento):
    nombre = 'Piano'
    def __init__(self):
        pass
class caja (instrumento):
    nombre = 'Caja'
    def __init__(self):
        pass
class flauta (instrumento):
    nombre = 'Flauta'
    def __init__(self):
        pass
class acordeon (instrumento):
    nombre = 'Acordeon'
    def __init__(self):
        pass
class gaita (instrumento):
    nombre = 'Gaita'
    def __init__(self):
        pass
class guacharaca (instrumento):
    nombre = 'Guacharaca'
    def __init__(self):
        pass
class llamador (instrumento):
    nombre = 'Llamador'
    def __init__(self):
        pass
class bateria (instrumento):
    nombre = 'Bateria'
    def __init__(self):
        pass
class banda():
    def nuevabanda(self,numeromusicos):
        instrumentos = [guitarra(),bajo(),piano(),caja(),flauta(),acordeon(),gaita(),guacharaca(),llamador(),bateria()]
        banda = []
        for i in range(0,numeromusicos):
            ins = randint(1,4)
            obj =instrumentos[ins]
            banda.append(obj)
        j = 1
        for i in banda:
            print("Instrumento",j," : ",i.nombre)
            j = j+1
        return banda
    def afinarbanda(self, banda, numeromusicos ):
        j = 1
        for i in banda:
            print(i.preparar()," ",j," :",i.nombre)
            j = j+1
    def tocarbanda(self, banda, numeromusiscos):
        j = 1
        for i in banda:
            print(i.tocar()," ",j," :",i.nombre)
            j = j+1
banda = banda()
numero = 0
b = []
while numero != 4:
    numeromusicos = randint(5,10)
    print("1. Crear Nueva Banda"+"\n"+"2. Afinar Banda"+"\n"+"3. Tocar Serenata"+"\n"+"4. Salir")
    numero = int(input("Seleccione: "))
    if(numero == 1):
        print("Numero de Musicos: ", numeromusicos)
        b = banda.nuevabanda(numeromusicos)
    if(numero == 2):
        banda.afinarbanda(b,numeromusicos)
    if(numero == 3):
        banda.tocarbanda(b,numeromusicos)
print("Gracias por su colaboración")