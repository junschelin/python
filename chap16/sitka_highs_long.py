# with open('death_valley_2021_full.csv') as f:
#     for line in f:
#         print(line.strip().split(sep=','))


import csv
from pathlib import Path #리눅스나 윈도우에 상관없이 사용 가능
from matplotlib import pyplot as plt


path = Path('chap16','sitka_weather_2021_simple.csv') #해당 경로를 알아서 찾아줌
# path = Path('chap16/sitka_weather_07-2021_simple.csv') #동일 경로

x1, y1=[],[]
x2, y2=[], []

COL_DATE = 2
COL_TMAX = 4
COL_TMIN = 5

with open(path) as f:
    reader = csv.reader(f)
    header = next(reader)
    for line in reader:
        # print(line)
        x1.append(line[COL_DATE])
        y1.append(line[COL_TMAX])
        
        x2.append(line[COL_DATE])
        y2.append(line[COL_TMIN])
        

plt.plot(x1,y1, label='TMAX')
plt.plot(x2,y2, label='TMIN')
plt.legend()
plt.show()