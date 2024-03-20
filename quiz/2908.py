from sys import stdin

a, b = stdin.readline().split()

# 방법 1 : reversed 사용
# print(''.join(reversed(a)), ''.join(reversed(b)))

# 방법 2 : slicing 사용
a_num = int(a[::-1])
b_num = int(b[::-1])

if a_num>b_num:
    print(a_num)
else:
    print(b_num)