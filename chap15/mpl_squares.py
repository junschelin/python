import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [i**2 for i in range(1,6)]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(input_values,squares, linewidth=3)

# 그래프 타이틀을 지정하고 축에 이름표를 붙입니다.
ax.set_title("Squares Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#틱 이름표 크기를 지정합니다 (x값, y값)
ax.tick_params(labelsize=10)
plt.show()
