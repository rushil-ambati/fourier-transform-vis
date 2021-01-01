import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np

import scipy.stats as stats
# - DEFINITIONS - 
mu, sigma = 0, 1
limit = mu + 3*sigma
t = np.linspace(mu - 3*sigma, mu + 3*sigma, 5000)
I = stats.norm.pdf(t, mu, sigma)
# - DEFINITIONS - 

fig = plt.figure()

plt.xlabel("Real")
plt.ylabel("Imaginary")


ax = plt.axes(xlim=(-1, 1), ylim=(-1, 1))
ax.set_aspect(1)

argand, = ax.plot([], [], 'ro', markersize=0.25)
com, = ax.plot([], [], 'bo', markersize=4)

def init():
    argand.set_data([], [])
    com.set_data([], [])
    return argand, com,

time_text = ax.text(0.05, 0.95,'',horizontalalignment='left',verticalalignment='top', transform=ax.transAxes)

plt.grid()

c = 0.001
def animate(f):
    a = I * np.exp(2*np.pi * 1j * (c*f) * t)
    real = []
    imag = []
    for x in range(len(a)):
        real.append(a[x].real)
        imag.append(a[x].imag)
    argand.set_data(real, imag)
    com.set_data(np.mean(real), np.mean(imag))
    
    time_text.set_text(round(c*f, 3))
    return argand, com, time_text,

def on_press(event):
    if event.key.isspace():
        if anim.running:
            anim.event_source.stop()
        else:
            anim.event_source.start()
        anim.running ^= True
    elif event.key == 'left':
        anim.direction = -1
    elif event.key == 'right':
        anim.direction = +1

    if event.key in ['left','right']:
        anim.frame_seq.__next__()

fig.canvas.mpl_connect('key_press_event', on_press)

frames = int(3/c)
anim = animation.FuncAnimation(fig, animate,init_func=init, frames=frames, interval=1000/60, blit=True)
anim.running = True
anim.direction = +1

plt.show()
'''
Writer = animation.writers['ffmpeg']
writer = Writer(fps=60, metadata=dict(artist='Rushil A.'), bitrate=1800)
anim.save('animated.mp4', writer=writer)
'''