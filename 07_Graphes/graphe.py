# Tracer d'un graphe

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,2*pi,100)
y = np.cos(x)

plt.figure(figsize=(6,6))
plt.plot(x,y,c='red')

plt.xlabel("x")
plt.ylabel("y")