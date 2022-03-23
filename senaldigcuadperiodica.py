from scipy import signal 
import matplotlib.pyplot as plot 
import numpy as np 
  
t = np.linspace(0, 1, 1000, endpoint=True)  
print(t)
      
plot.plot(t, signal.square(2 * np.pi * 10 * t)) 
  
plot.xlabel('Time') 
plot.ylabel('Amplitude') 
plot.title('Señal Cuadrada') 
  
plot.axhline(y = 0, color = 'k') 
plot.show()