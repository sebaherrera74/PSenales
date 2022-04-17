#ejemplo de subplot

from nis import maps
import numpy as np
import matplotlib.pyplot as plt

# create some data
x = np.arange(-2, 20, 0.5)                 # values of x
y1 =(-4.0/3.0)*x + 16     # values of y1(x)
y2 =0.2*x**2 -5*x + 32    # values of y2(x)
print(x)
print(y1)
print(y2)

fig = plt.figure(figsize=(8, 6))
#plt.clf()


plt.plot(x,y1,linewidth=3,color=(0.2,0.1,0.4))
plt.plot(x,y2,'o',linewidth=2,color='g')
plt.axhline(0, color='gray')
plt.axvline(0, color='gray')

plt.grid()
plt.axis('equal')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Lab DLS')
plt.axis([0, 20, -10, 40])
#plt.xlim(-10,20)
#plt.ylim(-10,40)

plt.show()
'''
fig = plt.figure()
ax1 = fig.add_subplot(111)

# create line plot of y1(x)
line1= ax1.plot(x, y1, 'g', label="Function y1")
ax1.set_xlabel('x')
ax1.set_ylabel('y1', color='g')

# create shared axis for y2(x)
ax2 = ax1.twinx()

# create line plot of y2(x)
line2 = ax2.plot(x, y2, 'r', label="Function y2")
ax2.set_ylabel('y2', color='r')

# set title, plot limits, etc
plt.title('Two functions on common x axis')
plt.xlim(-2, 18)
plt.ylim(0, 25)

# add a legend, and position it on the upper right
plt.legend((line1, line2), ('Function y1', 'Function y2'))
'''
# plt.show()
