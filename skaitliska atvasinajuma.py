#print(vars())
import sys
sys.path.append("/user/local/anaconda3/lib/python3.6/site-packages")
#print(vars())

from numpy import sin, linspace
#print(vars())

def f(x):
    return sin(x)


x = linspace(0,4,11)
#print(vars())

y = sin(x)

legend =[]
#print(legend)

from matplotlib import pyplot as plt
#print(plt.plot.__doc__)
plt.axis([0, 4, -1, 1])
plt.grid()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Funkcija $sin(x)$ un taas atvasinaajumi")
plt.plot(x,y,"k")
legend.append("$sin(x)$ - defaul - viss ir savienots ar taisnaam liinijam")
#print(legend)
plt.plot(x,y,"ro")
legend.append("$sin(x)$ - tikai dazhi punkti")
#print(legend)

N=len(x)
deltax = x[1] - x[0]
atvasinajums = []
for i in range(N):
    temp =(f(x[i] + deltax) - f(x[i])) / deltax
    atvasinajums.append(temp)

plt.plot(x,atvasinajums,"y")
legend.append("$sin(x)$ atvasinajums - viss ir savienots ar taisnaam liinijam")
plt.plot(x,atvasinajums,"go")
legend.append("$sin(x) atvasinajums - tiaki dazhi punkti")

derivative_through_array = []
for i in range(N-1):
    temp = (y[i+1] - y[i]) / (x[i+1] - x[i])
    derivative_through_array.append(temp)

plt.plot(x[0:-1],derivative_through_array, "m")
legend.append("$sin(x)$ atvasinajums, izmantojot masiiva veertiibas - viss ir savienots ar taisnaam liinijam")
plt.plot(x[0:N-1],derivative_through_array, "bo")
legend.append("$sin(x)$ atvasinajums, izmantojot masiiva veertiibas - tiaki dazhi punkti")







    
plt.plot(0.67,0.620, "ch", markersize = 10)
#print(plt.legend__doc__)
#plt.legend(legend, loc = "lower left")
#plt.legend(legend, loc = 3, fancybox=True, framealpha=0.5, facecolor="green")
plt.legend(legend, loc = 3, fancybox=True, framealpha=0.5)
plt.show()
