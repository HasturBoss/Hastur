import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
fig, ax = plt.subplots()
for i in range(10):    
    ax.plot(np.random.rand(10), '-o', ms=20, lw=2, mfc='blue')
    ax.grid()
    plt.title("Linear graph")
    plt.pause(1)
    plt.cla()
    if i==9:
        plt.pause(1)
        exit(0)

plt.show()