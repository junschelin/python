from bisect import bisect_right, bisect_left

lst = [1,2,3,4,4,8]
checks = [4, 5, 6, 7, 8]

print(bisect_left(lst,8))
print(bisect_right(lst, 8))

for check in checks:
    low, high = 0, len(lst)-1
    exist = False
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] > check:
            high = mid - 1 
        elif lst[mid] < check:
            low = mid+ 1 
        else:
            exist = True
            break
    # print (1 if exist else 0, end = ' ')
    print (high - low if exist else 0, end = ' ')