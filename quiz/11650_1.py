import sys
n = int(sys.stdin.readline())

x_y = {}
for i in range(n):
    x_y[(tuple(map(int,sys.stdin.readline().split())))] = i

print(x_y)

for k in x_y:
    for value in k:
        print(value)