from sys import stdin

def input():
    return stdin.readline().rstrip()

n = int(input())
num_lst = sorted(list(map(int, input().split())))

m = int(input())
checks = list(map(int, input().split()))

for check in checks:
    low, high = 0, n-1
    exist = False
    while low <= high:
        mid = (low + high) // 2
        if num_lst[mid] > check:
            high = mid - 1 
        elif num_lst[mid] < check:
            low = mid+ 1 
        else:
            exist = True
            break
    print (1 if exist else 0, end = ' ')