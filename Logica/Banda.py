from random import randint, uniform,random
from Guitarra import guitarra
from Bajo import bajo
from Piano import piano
from Caja import caja
from Flauta import flauta
from Acordeon import acordeon
from Gaita import gaita
from Guacharaca import guacharaca
from Llamador import llamador
from Bateria import bateria
class banda():
    def nuevabanda(self,numeromusicos):
        instrumentos = [guitarra(),bajo(),piano(),caja(),flauta(),acordeon(),gaita(),guacharaca(),llamador(),()]
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
