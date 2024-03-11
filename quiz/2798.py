n, m = map(int, input().split())
lst = list(map(int, input().split()))

min = m
sum = 0

for i in range(0,n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            sub = m - (lst[i] + lst[j] + lst[k])
            # print("i,j,k는 {},{},{} sub는 {}이고, min은 {}이고, sum은 {}입니다.".format(lst[i], lst[j], lst[k], sub, min, lst[i] + lst[j] + lst[k]))

            if (sub >= 0 and sub <= min):
                min = sub
                sum = lst[i] + lst[j] + lst[k]

print(sum)