"""
====================
Plot a sine function
====================

This is an example.

Here is a paragraph.

"""
print(__doc__)

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, num=2 ** 10)
y = np.sin(x * np.pi * 2)

plt.plot(x, y, label="Sine")
plt.legend()
plt.grid()
plt.show()
