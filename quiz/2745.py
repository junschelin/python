alphabet = [chr(c) for c in range(ord('A'), ord('Z')+1)]

dic = {}
for i in range(36):
    if i < 10:
        dic[str(i)] = i
    else:
        dic[alphabet[i-10]] = i


n, b = input().split()
b = int(b)


i = 0
sum = 0
for letter in n[::-1]:
    sum += dic[letter] * pow(b,i)
    i+=1
    

print(sum)