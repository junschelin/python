# 중복X -> 키 값으로 비교

n = int(input())
sang_list = list(map(int, input().split()))

m = int(input())
num_list = list(map(int, input().split()))

dic={}

for i in num_list:
    dic[i] = 0

for i in sang_list:
    if i in dic:
        dic[i] = 1

for i in dic:
    print(dic[i], end=' ')