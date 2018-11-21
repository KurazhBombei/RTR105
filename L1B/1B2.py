import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')

from numpy import *
                         # Importē skaitlisko metožu bibliotēkas funkcij
x = linspace(0, 4, 70)   # Trešais arguments ir ģenerējamo elementu skaits
y = x
y1= x**3/(3*2)
y2=x-x**3/(3*2)+x**5/(5*4*3*2)
y3=x-x**3/(3*2)+x**5/(5*4*3*2)-x**7/(7*6*5*4*3*2)
y4=sin(x)
from matplotlib import pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija')
plt.plot(x, y)
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.plot(x, y4)
plt.show()
