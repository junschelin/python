import sys

input = sys.stdin.readline

n, m = map(int, input().split())

lst = []

for i in range(1, n+1):
    lst.append(i)
    
# 배열을 담을 틀 만들기
total_set = set()

# m 크기만큼의 배열 생성
combi = [0]*m

# 각 자리에 각 숫자 하나씩 넣기
for i in range(m):
    combi[i] = lst[i]
    for j in range(m):
        combi[j] =     
    

# 전체 배열에 각 배열 집어 넣기 
combi[j] = num
total_set.add(tuple(combi))


print(total_set)