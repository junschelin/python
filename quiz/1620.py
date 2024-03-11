import sys

input = sys.stdin.readline

m, n = map(int, input().split())

pokemon = {}
for i in range(1,m+1):
    name = input()
    pokemon[name] = i
    pokemon[str(i)] = name

for _ in range(n):
    user_input = input()
    print(pokemon[user_input])