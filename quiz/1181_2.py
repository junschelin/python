import operator
from sys import stdin

n = int(stdin.readline().rstrip())

dic = {}
lst = []

for i in range(n):
    lst.append(stdin.readline().rstrip())

lst = list(set(lst))

for word in lst:
    dic[word] = len(word)

# s_dic=dict(sorted(dic.items(), key=operator.itemgetter(0))) # key 기준으로 정렬
s_dic=dict(sorted(dic.items(), key=operator.itemgetter(1))) # value 기준으로 정렬

for k in s_dic.keys():
    print(k)