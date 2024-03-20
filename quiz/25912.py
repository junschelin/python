from sys import stdin
input = stdin.readline

def counting():
    n = int(input().rstrip())
    cnt = 0
    user_set = set()
    for i in range(n):
        user = input().rstrip()
        if user != "ENTER":
            if user not in user_set:
                user_set.add(user)
                cnt+=1
        else:
            user_set.clear() 
    return cnt


print(counting())