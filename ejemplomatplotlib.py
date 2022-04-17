import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,100,0.01)
y1 = np.cos(2*np.pi*10*x)
y2 = np.sin(x)


plt.plot(x,y1,linewidth=3,color=(0.2,0.1,0.4))

plt.plot(x,y2,'o',linewidth=2,color='g')
plt.grid()
plt.axis('equal')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Lab DLS')
plt.show()