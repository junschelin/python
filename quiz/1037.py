import sys

input = sys.stdin.readline

quantity = int(input().rstrip())

lst = list(map(int, input().rstrip().split()))

lst.sort()

if quantity % 2 == 1:
    N = (lst[len(lst)//2])**2

else:
    N = (lst[0]) * (lst[-1])

print(N)