import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)  #(x, y, s = 점의 크기)


# 그래프 타이틀을 지정하고 축에 이름표를 붙입니다.
ax.set_title("Squares Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#틱 이름표 크기를 지정합니다 (x값, y값)
ax.tick_params(labelsize=14)

# 각 축의 범위를 지정합니다
ax.axis([0, 1100, 0, 1_100_000])
ax.ticklabel_format(style='plain') # 눈금 이름표의 기본 스타일을 덮어쓸 수 있음
plt.savefig('squares_plot.png', bbox_inches = 'tight')
