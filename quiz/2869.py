a, b, v = map(int, input().split())

i = (v-a)//(b-a)
i = i * (b-a) + 1
print(i)
