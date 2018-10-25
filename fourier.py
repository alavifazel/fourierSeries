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

x = numpy.linspace(-15,15,3000)

for i in range(0, 1000):
    anArray.append(an(i))
    bnArray.append(bn(i))

plt.figure(num="Fourier Series Visualization")

for i in range(1, 1000):
    plt.title("Iteration: " + str(i))

    plt.plot(x, mapInputs(x,2*i + 1), "m")

    plt.pause(0.000001)
    plt.clf() # Remove this line if you don't want your graph to become empty after each plotting
plt.show()
