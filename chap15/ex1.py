import matplotlib.pyplot as plt

fig, ax = plt.subplots()

def plot(x, y, label):
    ax.plot(x, y, label=label)

x1 = [1, 2, 3, 4]
y1 = [2, 3, 4, 6]
plot(x1, y1, label='blue')

x2 = [1, 2, 3, 4]
y2 = [1, 2, 3, 4]
plot(x2, y2, label='yellow')

ax.set_title('Plot A and B')
ax.set_xlabel('BMI')
ax.set_ylabel('AGE')
ax.set_aspect('equal')
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.legend()
plt.savefig('plot.png') #그래프 저장
plt.show()




