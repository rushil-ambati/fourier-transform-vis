import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

plt.figure()

# - DEFINITIONS - 
mu, sigma = 0, 1
t = np.linspace(mu - 3*sigma, mu + 3*sigma, 5000)
I = stats.norm.pdf(t, mu, sigma)
# - DEFINITIONS - 

fs = []
transform_x = []
# transform_y = []
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
plt.xlim((mu - 3*sigma, mu + 3*sigma))
plt.ylim((min(transform_x), max(transform_x)))
plt.xlabel("Frequency")
plt.ylabel("CoM")
plt.grid()

plt.show()