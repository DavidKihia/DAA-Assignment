import matplotlib.pyplot as plt
import numpy as np

x = [2, 4, 6, 8, 10, 12]

y = [8, 64, 216, 512, 1000, 1728]

plt.plot(x, y, 'b')
plt.xlabel('Inputs')
plt.ylabel('Steps')
plt.title('Cubic Complexity')
plt.show()
