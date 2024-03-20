m,n = map(int, input().split())

ans_lst = []
input_lst = []

for i in range(m):
    ans_lst.append(input())

for i in range(n):
    input_lst.append(input())

cnt = 0
for item in input_lst:
    if(item in ans_lst):
        cnt += 1

print(cnt)