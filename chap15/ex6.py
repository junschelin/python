from matplotlib import pyplot as plt

names = ['Hong', 'Lee', 'Kang']
y1 = [50, 70, 20]
y2 = [30, 50, 70]
y_gap = [abs(v1 - v2) for v1,v2 in zip(y1,y2)]


# 왼쪽 축 (국어)
fig, ax1 = plt.subplots()
ax1.plot(names, y1, color='red', label='Lang')
ax1.scatter(names, y1, color='red')
ax1.plot(names, y2, color='blue', label="Eng.")
ax1.scatter(names, y2, color='blue')
ax1.set_xlabel("Name")
ax1.set_ylabel("Score")

# 오른 쪽 축(영어)
ax2 = ax1.twinx()
ax2.bar(names,y_gap, color='green', label='gap', alpha = 0.2) 
ax2.set_ylabel("Gap")

ax1.legend()
ax2.legend(loc='upper right')
plt.show()

# names = ['group_a', 'group_b', 'group_c']
# values = [1, 10, 100]

# plt.figure(figsize=(9, 3))

# plt.subplot(131)
# plt.bar(names, values)

# plt.subplot(132)
# plt.scatter(names, values)

# plt.subplot(133)
# plt.plot(names, values)

# plt.suptitle('Categorical Plotting')
# plt.show()