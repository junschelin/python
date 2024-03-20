import sys

n = sys.stdin.readline().rstrip()

lst = sorted(n, reverse=True) # sorted : 리스트 타입으로 변환

for i in lst:
    print(i, end='')