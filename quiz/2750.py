# from sys import stdin
#
# n = int(stdin.readline())
#
# #data = [int(d.rstrip()) for d in stdin.readlines()] #EOF 필요
#
# data = [map(int, stdin.readlines())] #EOF 필요
#
#
# print(sorted(data))

# from sys import stdin
# for number in sorted([int(stdin.readline()) for _ in range(int(stdin.readline()))]): print(number)

import sys
b = input()
a = list(map(int, sys.stdin.read().rstrip()))
a.sort()
for i in a:
    print(i)
