squares = [value ** 2 for value in range(1,11)]
print(squares)

print(squares[0:3])
print(squares[-3:])
print(squares[:-2])

my_list = [1, 2, 3, 4, 5, 6, 7, 8]

print(my_list[::-1])
print(my_list[::-2])
print(my_list[::-3])

print(squares[::-1])
print(squares[::-2])
print(squares[::-3])


a = [1, 2, 3, 4]
b = [3, 4]
# c = a - b : 에러

c1 = [x for x in a if x not in b]
c2=list(set(a) - set(b))
print(c1)
print(c2)

# Shallow Copy : 주소 값만 복사
a = [10, 20, 30, 40, 50]
b = a
a[0] = 100
print(b)

# Deep Copy : 실제 값을 복사
a = [10, 20, 30, 40, 50]
b = a[:]
a[0] = 100
print(b)

# Shallow Copy : 주소 값만 복사
a = [[1, 2, 3], [4, 5, 6]]
b = a[:]
print(b)
a[0][0] = 100
print(b)

