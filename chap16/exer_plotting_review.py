from matplotlib import pyplot as plt
from random import randint

# x = [1, 2, 3, 4]
# y = [ i ** 2 for i in x]

x1 = list(range(1, 5))
y1 = [i*i for i in x1]

x2 = list(range(1,5))
y2 = [i**3 for i in x2]

fig, axs = plt.subplots(1,2)

axs[0].plot(x1,y1,label='Squared Two', color='red')
axs[0].plot(x2,y2,label ='Squared Three', color='blue')

axs[1].scatter(x1,y1)
axs[1].scatter(x2,y2)

axs.xlabel('X')
axs.ylabel('Y')
axs.legend()

# plt.plot(x1, y1, label='Squared Two', color='red')
# plt.plot(x2, y2, label ='Squared Three', color='blue')

# plt.title('X Square')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.legend()


plt.show()