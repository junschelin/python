import math

lst = []
for i in range(5):
    lst.append(int(input()))

# 첫 번째는 평균
print(int(sum(lst)/len(lst)))
# 두 번째는 중앙값
print(sorted(lst)[math.floor(len(lst)/2)])