a, b, v = map(int, input().split())

i=0
sum = 0
while True:
    sum += a
    i += 1

    if sum >= v:
        break

    sum -= b
    if sum >= v:
        break
print(i)