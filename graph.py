#for plotting graphes of functions, for big O notation and such kind of functions comparison

import inline
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

n = np.linspace(1, 20)
# plt.plot(n, (7 * n * n + 6 * n + 5), label = "7n^2 + 6n + 5")
# plt.plot(n, (7 * n**2), label="7n^2")
# plt.legend(loc='upper left')
# plt.show()

plt.plot(n, (3 **n), label = "3^n")
plt.plot(n, 2 **(2 * n), label = "2^2n ")
plt.legend(loc = 'upper left')
plt.show()