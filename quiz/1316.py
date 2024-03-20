import sys

n = int(sys.stdin.readline().rstrip())

lst = []
for _ in range(n):
    lst.append(sys.stdin.readline().rstrip())

cnt = 0

for i in range(n):
    isContinuous = True
    word = lst[i]

    for j in range(len(word)):
        same_idx = 0
        diff_idx = 0
        for k in range(j+1, len(word)):
            if word[j] != word[k]:
                if word[j] in word[k:len(word)]:
                    isContinuous = False
                    break
        if not isContinuous:
            break            

    if isContinuous:
        cnt += 1
print(cnt)