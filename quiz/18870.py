import sys

input=sys.stdin.readline

n = int(input().rstrip())

lst = list(map(int, input().rstrip().split()))

nums = sorted(list(set(lst)))

print(nums)

#키에 숫자 넣고, 값에 인덱스 넣어라