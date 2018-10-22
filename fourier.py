import matplotlib.pyplot as plt
import numpy
from math import pi, cos, sin
from scipy.integrate import quad

def f(x):
    if x > -pi and x < -pi/2:
        return 0
    elif x >= -pi/2 and x <= pi/2:
        return 1
    elif x > pi/2 and x < pi:
        return 0

T = 2*pi

anArray = []
bnArray = []

def fCos(x, n):
    return f(x)*cos((n*2*pi)/T*x)


def fSin(x, n):
    return f(x)*sin((n*2*pi)/T*x)

def a0():
    return (1/T)*(quad(f,-T/2, T/2)[0])

def an(n):
    return (2/T)*(quad(fCos, -T/2, T/2, args=(n), limit=500)[0])

def bn(n):
    return (2/T)*(quad(fSin, -T/2, T/2, args=(n), limit=500)[0])

def mapInputs(x,n):
    y = []
    for i in range (0, len(x)):
        y.append(fourier(x[i], n))
    return y

def fourier(x, n):
    tmp = 0
    for i in range(1,n):
        if i == 1:
            tmp = a0()
        elif i != n:
            j = i - 1
            tmp += ( anArray[j] * cos(2*j * pi * x / T )) + ( bnArray[j] * sin(2*j * pi * x / T) )

    return tmp

x = numpy.linspace(-15,15,1000)

for i in range(0, 500):
    anArray.append(an(i))
    bnArray.append(bn(i))


for i in range(1, 500, 2):
    plt.plot(x, mapInputs(x,i+1))
    plt.pause(0.1)

plt.show()
