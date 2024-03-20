from matplotlib import pyplot as plt
import csv
from datetime import datetime as dt

x1 = []
y1 = []
y2 = []

with open('./chap16/sitka_weather_07-2021_simple.csv', 'r') as f:
    reader = csv.reader(f)

    header = next(reader)
  
    for row in reader:
        x1.append(dt.strptime(row[2],"%Y-%m-%d"))
        y1.append(int(row[4]))
        y2.append(int(row[5]))


# plt.plot(x1, y1, label="TMAX", color = 'red')
# plt.plot(x1, y2, label="TMIN", color = 'blue')
# plt.fill_between(x1, y1, y2, alpha=1)
# plt.legend()
# plt.show()

ax = plt.subplot(2,2,1)
ax.plot(x1, y1, label="TMAX", color = 'red')
ax.plot(x1, y2, label="TMIN", color = 'blue')
ax.fill_between(x1, y1, y2, alpha=1)
ax.legend()
plt.show()