import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np

fig = plt.figure(figsize=(6,6))

func_ax = plt.axes([0.1, 0.2, 0.75, 0.75])
func_ax.set_aspect(1)
slider_ax = plt.axes([0.1, 0.05, 0.8, 0.05])

plt.axes(func_ax)

# - DEFINITIONS - 
f_min = 0
f_max = 12
f_init = 3

# 3 Hz
t = np.linspace(0, 4.5, 4500)
I = np.cos(3*(2*np.pi)*t) + 1

'''
# 2.3 Hz + 4.5 Hz
t = np.linspace(0, 5, 5000)
I = np.cos(4.5*(2*np.pi)*t) + np.cos(2.3*(2*np.pi)*t) + 2
'''
# - DEFINITIONS - 

a = I * np.exp(2*np.pi * 1j * f_init * t)
real = []
imag = []
for x in range(len(a)):
    real.append(a[x].real)
    imag.append(a[x].imag)

func_plot, = plt.plot(real, imag, 'ro', markersize=0.25)
com, = plt.plot(np.mean(real), np.mean(imag), 'bo', markersize=4)

plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.grid()
a_slider = Slider(slider_ax,
                  'f',
                  f_min,
                  f_max,
                  valinit=f_init
                 )

def update(f):
    a = I * np.exp(2*np.pi * 1j * f * t)
    real = []
    imag = []
    for x in range(len(a)):
        real.append(a[x].real)
        imag.append(a[x].imag)
    func_plot.set_data(real, imag)
    com.set_data(np.mean(real), np.mean(imag))
    fig.canvas.draw_idle()
a_slider.on_changed(update)

plt.show()