import matplotlib.pyplot as plt


x = [2, 4, 6, 8, 10, 12]

y = [4, 16, 64, 256, 1024, 4096]

plt.plot(x, y, 'b')
plt.xlabel('Inputs')
plt.ylabel('Steps')
plt.title('Exponential Complexity')
plt.show()

