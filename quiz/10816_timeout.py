from sys import stdin

n = int(stdin.readline().rstrip())

lst_1 = list(map(int, stdin.readline().split()))
# dic_1 = dict()

# for i in range(n):
#     dic_1[i] = lst_1[i]

m = int(stdin.readline().rstrip())

lst_2 = list(map(int, stdin.readline().split()))
dic_2={}
for i in lst_2:
    dic_2[i] = i
    print(lst_1.count(dic_2[i]), end=' ')
