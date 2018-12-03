#Fails: 170.py
#Autors: ...................
#Apliecibas numurs: .................
#Datums: ........
#Sagatave funkcijas saknes mekleeshanai ar dihatomijas metodi
#-*- coding: utf -8 -*-
from math import sin, fabs
from time import sleep

def f(x):
    return sin(x)

#Definejam argumenta x robezhas:
a = 1.1
b = 3.2

#Aprekjinam funkcijas vertibas dotajos punktos:

funa = f(a)
funb = f(b)

#Paarbaudam, vai dotajaa intervaalaa ir saknes:
if( funa * funb > 0.0):
    print("Dotaja intervala [%s, %s] skanju nav"% (a,b))
    sleep(1); exit()  # Zinjo uz ekrana, gaida 1 sec. un darbu pabeidz
else:
    print("Dotaja intervala saknes (s) ir!")

# Definejam pricizitati, ar kadu meklesim sakni:
deltax = 0.01

# sashaurinam saknes mekleshanas robezhas:
while ( fabs(b-a) > deltax ):
    x=(a+b)/2; funx = f(x)
    if (funa*funx < 0. ):
        b=x
    else:
        a=x

print("Sakne ir: " , x)
