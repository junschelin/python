from sys import stdin

n = int(stdin.readline().rstrip())

dic = {}
lst = []

for i in range(n):
    lst.append(stdin.readline().rstrip())

lst = list(set(lst))

for word in lst:
    dic[word] = len(word)

s_dic=dict(sorted(dic.items(), key=lambda x : (x[1], x[0])))

for k in s_dic.keys():
    print(k)