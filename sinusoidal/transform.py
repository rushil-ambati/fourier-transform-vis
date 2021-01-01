import matplotlib.pyplot as plt
import numpy as np

plt.figure()

# - DEFINITIONS - 
# 3 Hz
t = np.linspace(0, 4.5, 4500)
I = np.cos(3*(2*np.pi)*t) + 1

'''
# 2.3 Hz + 4.5 Hz
t = np.linspace(0, 5, 5000)
I = np.cos(4.5*(2*np.pi)*t) + np.cos(2.3*(2*np.pi)*t) + 2
'''
# - DEFINITIONS - 

fs = []
transform_x = []
transform_y = []
for f in t:
    a = I * np.exp(2*np.pi * 1j * f * t)
    real = []
    imag = []
    for x in range(len(a)):
        real.append(a[x].real)
        imag.append(a[x].imag)
    fs.append(f)
    transform_x.append(np.mean(real))
    # transform_y.append(np.mean(imag))
    
plt.plot(fs, transform_x, 'mo', markersize=0.25)
# plt.plot(fs, transform_y, 'bo', markersize=0.25)
plt.xlim((0, max(t)))
plt.ylim((min(transform_x), max(transform_x)))
plt.xlabel("Frequency")
plt.ylabel("CoM")
plt.grid()

plt.show()