import numpy as np
import matplotlib.pyplot as plt
import pyabf
abf = pyabf.ABF("./patch/2023_10_18_000.abf")
abf.setSweep(0,0)
print(abf.sweepY) # displays sweep data (ADC)
print(abf.sweepX) # displays sweep times (seconds)
print(abf.sweepC) # displays command waveform (DAC)
print(type(abf.sweepY)) # displays sweep times (seconds)
print(np.size(abf.sweepY)) # displays sweep times (seconds)

print(abf.sweepUnitsC)
print(abf)

# plot the first channel
abf.setSweep(sweepNumber=0, channel=0)
plt.plot(abf.sweepX, abf.sweepY, label="Channel 1")

# plot the second channel
abf.setSweep(sweepNumber=0, channel=1)
plt.plot(abf.sweepX, abf.sweepY, label="Channel 2")
plt.show()

"""
fig = plt.figure(figsize=(8, 5))
plt.plot(abf.sweepX,abf.sweepC)
plt.show()
"""

"""
# plot the first channel
abf.setSweep(sweepNumber=0, channel=0)
plt.plot(abf.sweepX, abf.sweepY, label="Channel 1")

# plot the second channel
abf.setSweep(sweepNumber=0, channel=1)
plt.plot(abf.sweepX, abf.sweepC, label="Channel 2")

# decorate the plot
plt.ylabel(abf.sweepLabelY)
plt.xlabel(abf.sweepLabelX)
plt.axis([25, 45, -70, 50])
plt.legend()
plt.show()
"""