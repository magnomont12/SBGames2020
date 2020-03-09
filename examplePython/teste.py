import matplotlib.pyplot as plt

vetorx = []
vetory = []
x = -50
for a in range(0,100):
    vetorx.append(x+a)
    vetory.append(1/(x+a))

plt.plot(vetorx, vetory)
plt.ylabel('some numbers')
plt.show()