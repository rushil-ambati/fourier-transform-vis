import matplotlib.pyplot as plt
import numpy as np

# - DEFINITIONS - 
f = 9
# 3 Hz
t = np.linspace(0, 4.5, 4500)
I = np.cos(3*(2*np.pi)*t) + 1

'''
# 2.3 Hz + 4.5 Hz
t = np.linspace(0, 5, 5000)
I = np.cos(4.5*(2*np.pi)*t) + np.cos(2.3*(2*np.pi)*t) + 2
'''
# - DEFINITIONS - 

plt.figure()

a = I * np.exp(2*np.pi * 1j * f * t)

real = []
imag = []
for x in range(len(a)):
    real.append(a[x].real)
    imag.append(a[x].imag)

plt.plot(real, imag, 'ro', markersize=0.25)
plt.plot(np.mean(real), np.mean(imag), 'bo', markersize=4)
limit = np.max(np.ceil(np.absolute(a)))

plt.xlim((-limit, limit))
plt.ylim((-limit, limit))

plt.xlabel("Real")
plt.ylabel("Imaginary")

plt.grid()

ax = plt.gca()
ax.set_aspect(1)

plt.show()