from sys import stdin

m, n = map(int, stdin.readline().split())

# 집합 방식
# A = set(list(map(int, stdin.readline().split())))
# B = set(list(map(int, stdin.readline().split())))

# print(len(B-A) + len(A-B))

A = set(list(map(int, stdin.readline().split())))
B = set(list(map(int, stdin.readline().split())))

cnt = 0

for a in A:
    if a in B:
        cnt += 1
        
print(m+n-2*cnt)