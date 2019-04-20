import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(10, 10.5)

ax = plt.axes(xlim=(0, 10), ylim=(0, 10))
patch = plt.Circle((5, -5), 0.15, fc='g')

#Background
img = plt.imread("space.png")
ax.imshow(img,zorder=0, extent=[0, 10, 0, 10])

ax.set_title("Simulation of earth orbtiting the sun")

#Sun
x_sun = [5]
y_sun = [5]

ax.scatter(x_sun,y_sun,c="y",s=400,zorder=1)

def init():
    patch.center = (5, 5)
    ax.add_patch(patch)
    return patch,

def animate(i):
    x, y = patch.center
    x = 5 + 3 * np.sin(np.radians(i))
    y = 5 + 3 * np.cos(np.radians(i))
    patch.center = (x, y)
    return patch,

anim = animation.FuncAnimation(fig, animate, 
                               init_func=init, 
                               frames=360, 
                               interval=20,
                               blit=True)
plt.axis("off")
plt.show()