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
ax = plt.axes(xlim=(-l, l), ylim=(0, 1.5)) 
plt.xlabel("x")
plt.ylabel("y")
plt.title('Rect(x) - 01')
plt.plot(x, rect01)
plt.show(fig01)

d = 0.0; #desplazamiento sobre el eje x
AnchoPulso = 1.0
a1 = -AnchoPulso/2.0 + d #limites del ancho de pulso
a2 = AnchoPulso/2.0 + d
rect02[(x>a1)*(x<a2)] = 1.0
fig01 = plt.figure()
ax = plt.axes(xlim=(-l, l), ylim=(0, 1.5)) 
plt.xlabel("x")
plt.ylabel("y")
plt.title('Rect(x) - 02')
plt.plot(x, rect02)
plt.show(fig01)

#%Recuerdese que en la convolocion una de las funciones debe ser invertida.
rect02 = rect02[len(rect02): -(len(rect02)+1):-1]

d=-l
convol = np.zeros(len(x))
for i in range(len(x)):
    d = d + delta #desplazamiento sobre el eje x
    AnchoPulso = 1.0
    a1 = -AnchoPulso/2.0 + d #limites del ancho de pulso
    a2 = AnchoPulso/2.0 + d
    rect02 = np.zeros(len(x))
    rect02[(x>a1)*(x<a2)] = 1.0
    convol[i] = (rect02*rect01).sum()

convol = convol/convol.max()
fig01 = plt.figure()
ax = plt.axes(xlim=(-l, l), ylim=(0, 1.5)) 
plt.xlabel("x")
plt.ylabel("y")
plt.title("Conv(Rect01(x),Rect02(x))")
plt.plot(x, convol)
plt.show(fig01)



