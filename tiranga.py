import numpy as np
import matplotlib.pyplot as py
import matplotlib.patches as patch

a = patch.Rectangle((0,1), width=10, height=2, facecolor='green', edgecolor='grey')
b = patch.Rectangle((0,3), width=10, height=2, facecolor='white', edgecolor='grey')
c = patch.Rectangle((0,5), width=10, height=2, facecolor='#FF6103', edgecolor='grey')
m,n = py.subplots()
n.add_patch(a)
n.add_patch(b)
n.add_patch(c)

radius = 1.0
py.plot(5,4, marker ='o', markerfacecolor='#000088ff', markersize=6.5)
chakra = py.Circle((5,4), radius, color='#000088ff', fill=False, linewidth=7)
n.add_artist(chakra)

for i in range(0,24):
    p = 5 + radius/2 * np.cos(np.pi*i/12 + np.pi/48)
    q = 5 + radius/2 * np.cos(np.pi*i/12 - np.pi/48)
    r = 4 + radius/2 * np.sin(np.pi*i/12 + np.pi/48)
    s = 4 + radius/2 * np.sin(np.pi*i/12 - np.pi/48)
    t = 5 + radius * np.cos(np.pi*i/12)
    u = 4 + radius * np.sin(np.pi*i/12)
    n.add_patch(patch.Polygon([[5,4], [p,r], [t,u], [q,s]], fill=True, closed=True, color='#000088ff'))
py.axis('equal')
py.show()