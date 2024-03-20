import sys
m, n = map(int, sys.stdin.readline().split())

listen = {}
for _ in range(m):
    listen[sys.stdin.readline().rstrip()] = _

see = {}
for _ in range(n):
    see[sys.stdin.readline().rstrip()] = _

lst = []
for k in listen:
    if k in see:
        lst.append(k)

print(len(lst))
for i in sorted(lst):
    print(i)