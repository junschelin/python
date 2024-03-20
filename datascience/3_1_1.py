# 집합
A1 = {1, 2, 3, 4}
A2 = {2, 4, 6}
A3 = {1, 2, 3}
A4 = {2, 3, 4, 5, 6}

# 합집합
# 1번 방법 : union method
print(A1.union(A2))

# 2번 방법 : |
print(A1 | A2)

# 교집합

# 1번 방법 : intersection
print(A3.intersection(A4))

# 2번 방법 : & 
print(A3 & A4)

# 부분집합여부 확인
# 1번 방법 : issubset
print(A3.issubset(A1))

# 2번 방법 : 부등호 (<= or <)
print(A3 <= A1)
print(A1 <= A4)

# 차집합
# 1번 방법 : difference
print(A1.difference(A2))

# 2번 방법 : -
print(A1 - A2)