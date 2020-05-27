# Banda Aleatoria

_Programa para la creación de una banda aleatoria entre 1 a 10 musicos. Este programa permite afinar o tocar los instrumentos, asi como, realizar distintas bandas aleatorias._

### Pre-requisitos 📋

_Este programa se realizó con Flask en Pytho, por lo que es necesario tener, al menos, Python 2.6 o Python 3 instalado._

![alt text](https://blogs.masterhacks.net/wp-content/uploads/2020/01/masterhacks_fin_vida_python_2.7.jpeg)

### Instalación 🔧

_Para instalar Flask vamos a utilizar pip. Así que simplemente deberemos de escribir en nuestra línea de comandos lo siguiente:_

```
$ pip install Flask
```
_Puede ser que para la instalación necesites ser administrador. En ese caso ejecuta:_

```
$ sudo pip install Flask
```
_Dentro del entorno virtual podremos trabajar con diferentes versiones de Python y de las librerías que estemos utilizando._

_Para instalar virtualenv deberás de ejecutar lo siguiente_

```
$ pip install virtualenv
```
_Una vez instalado virtualenv deberás de crear un directorio para tu proyecto._

```
$ mkdir miproyecto $ cd miproyecto
```
_Ahora creamos el entorno virtual del proyecto:_

```
$ virtualenv mientornovirtual
```

_Se suele utilizar venv como nombre de los entornos virtuales. Ahora tenemos que saber hacer dos cosas. Por un lado activar el entorno virtual:_
```
$ . mientornovirtual/bin/activate
```
_Y desactivarlo una vez acabemos de utilizarlo_

```
$ deactivate
```
_Dentro del entorno virtual realizaremos la instalación de Flask._

## Principios de Diseño ⚙️

### The Open Closed Principle (OCP)

_Un módulo debe estar abierto para extensión pero cerrado para la modificación._

Esto significa que el comportamiento de un módulo puede ser extendido. Cuando los requerimientos de una aplicación cambien, debemos ser capaces de extender el módulo con nuevos comportamientos que satisfagan esos cambios, es decir, debemos ser capaces de cambiar lo que el módulo hace.

Eso pasa en las clases acordeon, guitarra, etc... que hereda de la clase instrumento.

### The Liskov Substitution Principle (LSP)

_las subclases deben ser sustituibles por sus clases base._

El principio define que los objetos de una superclase serán reemplazables por objetos de sus subclases sin interrumpir la aplicación. Eso requiere que los objetos de sus subclases se comporten de la misma manera que los objetos de su superclase.

Este principio se da entre las subclases acordeon, guitarra, etc... que pueden reemplazar la clase Instrumentos ya que posee los mismos metodos.

### The Dependency Inversion Principle (DIP)

_Depende de las abstracciones. No depende de las concreciones._

Los módulos de alto nivel, que proporcionan una lógica compleja, deberían ser fácilmente reutilizables y no verse afectados por los cambios en los módulos de bajo nivel, que proporcionan funciones de utilidad. Para lograrlo, debe introducir una abstracción que desacople los módulos de alto y bajo nivel entre sí.

Esta se ve aplicada en la clase Instrumentos a Banda.

## Autores ✒️

_Este trabajo fue realizado por:_

* **Daniel Arenas** 
* **Lorena Damián** 
