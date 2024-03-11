from sys import stdin
from bisect import bisect_left, bisect_right

n = int(stdin.readline().rstrip())
card = sorted(list(map(int, stdin.readline().split())))

m = int(stdin.readline().rstrip())
checks = list(map(int, stdin.readline().split()))

def count_by_range(lst, left_value, right_value):
    right_index = bisect_right(lst, right_value)
    left_index = bisect_left(lst, left_value)
    return right_index - left_index

for i in range(m):
    result = count_by_range(card, checks[i], checks[i])
    print (result, end = ' ')