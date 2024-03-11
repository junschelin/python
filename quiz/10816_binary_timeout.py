from sys import stdin

n = int(stdin.readline().rstrip())
card =  sorted(list(map(int, stdin.readline().split())))

m = int(stdin.readline().rstrip())
checks = list(map(int, stdin.readline().split()))

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start +  end) //2
    if array[mid] == target:
        return array[start : end+1].count(target)
    elif array[mid] < target:
        return binary_search(array, target, mid+1, end)
    else:
        return binary_search(array, target, start, mid-1)

for i in range(m):
    result = binary_search(card, checks[i], 0, n-1)
    if result is not None:
        print(result, end = ' ')
    else :
        print(0, end=' ')    