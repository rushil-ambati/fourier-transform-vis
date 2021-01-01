import matplotlib.pyplot as plt
import numpy as np

# - DEFINITIONS - 
# 3 Hz
t = np.linspace(0, 4.5, 45000)
I = np.cos(3*(2*np.pi)*t) + 1

'''
# 2.3 Hz + 4.5 Hz
t = np.linspace(0, 5, 5000)
I = np.cos(4.5*(2*np.pi)*t) + np.cos(2.3*(2*np.pi)*t) + 2
'''
# - DEFINITIONS - 

plt.figure()

plt.plot(t, I)

plt.xlim(t.min(), t.max())

plt.xlabel("Time")
plt.ylabel("Intensity")

plt.show()