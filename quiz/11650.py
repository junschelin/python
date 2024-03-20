from sys import stdin

n = int(stdin.readline().rstrip())

lst = []

for _ in range(n):
    lst.append(list(map(int, stdin.readline().split())))

# lst_sort = sorted(lst, key=lambda x : (x[0], x[1])) #아래코드와 같은 기능 (0번 인덱스 오름차순, 0번 인덱스 동일 시 1번 인덱스 오름차순)
# lst_sort = sorted(lst, key=lambda x : (x[0], -x[1])) #(0번 인덱스 오름차순, 0번 인덱스 동일 시 1번 인덱스 내림차순)
lst_sorted = sorted(lst)


for i in range(n):
    print(lst_sorted[i][0], lst_sorted[i][1])