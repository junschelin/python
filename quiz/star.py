n = int(input())

for i in range(1,2*n):
    if i > n:
        print(' '*(i - n) + '*'*(2*(i - 2*(i-n))-1))
    else:
        print(' '*(n - i) + '*'*(2*i - 1))