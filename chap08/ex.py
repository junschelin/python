count = int(input())
lst = list(input().split())
v = int(input())
lst_int = []
for i in lst:
    lst_int.append(int(i))
    
ans = 0
for i in lst_int:
    if(v == i):
        ans += 1
print(ans)