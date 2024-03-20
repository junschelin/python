import sys

lst = []

for i in range(9):
    lst.append(list(map(int, sys.stdin.readline().split())))

maxi = 0
idx = (0, 0)

for row in lst:
    for element in row:
        if element >= maxi:
            idx = (lst.index(row), row.index(element))
            maxi = element

print(maxi)
print(idx[0]+1, idx[1]+1)
