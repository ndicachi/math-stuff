import matplotlib.pyplot as plt 
import matplotlib.animation as animation 
import numpy as np 

fig = plt.figure() 
ax = plt.axes(xlim=(-2, 2), ylim=(-2, 2)) 
circulo, = ax.plot([], [], lw=2) 

def init(): 
	circulo.set_data([], []) 
	return circulo, 

theta = np.arange(0., 2.0*np.pi, np.pi/180.0)
r = np.arange(0.0, 1.5, 0.01) 

def animate(t): 
	x = r[t]*np.sin(theta) 
	y = r[t]*np.cos(theta) 
	circulo.set_data(x, y) 
	return circulo, 
	
plt.title('Circulo creciendo') 

animacion = animation.FuncAnimation(fig, animate, init_func=init, frames=len(r), interval=240, blit=True) 
plt.show()







