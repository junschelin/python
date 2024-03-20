import sys

lst = []

for i in range(9):
    lst.append(int(sys.stdin.readline().rstrip()))

print(max(lst))
print(lst.index(max(lst))+1)