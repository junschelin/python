import matplotlib.pyplot as plt

x = range(1,101)
square = [i**2 for i in x]

fig, ax = plt.subplots()
ax.scatter(x, square, c = square, s=3, cmap=plt.cm.Blues)
ax.set_xlim(0,100) 
ax.set_ylim(0,10000) 
# ax.axis([0, 100, 0, 10_000])
ax.set_title('Square', fontsize = 20)
ax.set_xlabel('X', fontsize = 15)
ax.set_ylabel('Y', fontsize = 15)
ax.tick_params(labelsize=12)
fig.colorbar()
plt.style.use('seaborn-v0_8-pastel')
ax.legend
# for s in plt.style.available:
#     print(s)

plt.show()