import sys


n = int(sys.stdin.readline())

lst=[]

for _ in range(n):
    lst.append(list(map(int, sys.stdin.readline().split())))

s_lst = sorted(lst, key=lambda x : (x[1], x[0]))

for i in range(n):
    print(s_lst[i][0], s_lst[i][1])