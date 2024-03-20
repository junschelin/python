#복습
import random
from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator

# x = range(4)
# print(x, type(x))
# y = [i**2 for i in x]

# plt.plot(x,y)
# plt.scatter(x,y)

# x = [random.randint(0,100) for _ in range(10000)]

# plt.hist(x)

x1 = list(range(5))
y1 = [i**2 for i in x1]

x2 = list(range(5))
y2 = [i**3 for i in x2]


fig, ax = plt.subplots()
ax.plot(x1, y1, label = "squared two", color = 'red')
ax.plot(x2, y2, label = "squared three", color = 'blue')
ax.scatter(x1, y1, color = 'red')
ax.scatter(x2, y2, color = 'blue')
ax.set_xticks([0,1,2,3,4])
ax.xaxis.set_major_locater(MultipleLocator(1))
ax.set_title('AAA vs BBB')
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.legend()
plt.show()



