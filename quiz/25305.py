from sys import stdin

n, k = map(int, stdin.readline().split())
lst = list(map(int, stdin.readline().split()))

print(sorted(lst, reverse=True)[k-1])