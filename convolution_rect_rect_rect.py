import numpy as np
import matplotlib.pyplot as plt 

l = 3.0;
delta = 0.001;
x = np.arange(-l,l,delta)
rect01 = np.zeros(len(x))
rect02 = np.zeros(len(x))

d = 0.0; #desplazamiento sobre el eje x
AnchoPulso = 1.0
a1 = -AnchoPulso/2.0 + d #limites del ancho de pulso
a2 = AnchoPulso/2.0 + d
rect01[(x>a1)*(x<a2)] = 1.0
fig01 = plt.figure()
ax = 
plt.plot(x, rect01)
plt.show(fig01)

d = 0.0; #desplazamiento sobre el eje x
AnchoPulso = 1.0
a1 = -AnchoPulso/2.0 + d #limites del ancho de pulso
a2 = AnchoPulso/2.0 + d
rect02[(x>a1)*(x<a2)] = 1.0
fig02 = plt.figure()
plt.plot(x, rect02)
plt.show(fig02)

#%Recuerdese que en la convolocion una de las funciones debe ser invertida.
rect02 = rect02[len(rect02): -(len(rect02)+1):-1]

d=-l
f3 = np.zeros(len(x))
for i in range(len(x)):
    d = d + delta #desplazamiento sobre el eje x
    AnchoPulso = 1.0
    a1 = -AnchoPulso/2.0 + d #limites del ancho de pulso
    a2 = AnchoPulso/2.0 + d
    rect02 = np.zeros(len(x))
    rect02[(x>a1)*(x<a2)] = 1.0
    f3[i] = (rect02*rect01).sum()

f3 = f3/f3.max()
fig03 = plt.figure()
plt.plot(x, f3)
plt.show(fig03)

d=-l
f4 = np.zeros(len(x))
for i in range(len(x)):
    d = d + delta #desplazamiento sobre el eje x
    AnchoPulso = 1.0
    a1 = -AnchoPulso/2.0 + d #limites del ancho de pulso
    a2 = AnchoPulso/2.0 + d
    rect02 = np.zeros(len(x))
    rect02[(x>a1)*(x<a2)] = 1.0
    f4[i] = (rect02*f3).sum()

f4 = f4/f4.max()
fig04 = plt.figure()
plt.plot(x, f4)
plt.show(fig03)



