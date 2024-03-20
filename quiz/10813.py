import sys

input = sys.stdin.readline

n, m = input().rstrip().split()

n = int(n)
m = int(m)

bucket = []

for i in range(1, n+1):
    bucket.append(i)

for _ in range(m):
    idx = list(map(int, input().rstrip().split()))
    bucket[idx[0]-1], bucket[idx[1]-1] = bucket[idx[1]-1], bucket[idx[0]-1]

for item in bucket:
    print(item, end=' ')