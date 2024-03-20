from sys import stdin
def input():
    return stdin.readline().rstrip()

n = int(input())

lst = [0] * 10001

# append를 사용하면 메모리 재할당이 이루어져서 메모리를 효율적으로 사용 못함

# 입력 받는 숫자의 개수만큼 값을 증가
for _ in range(n):
    lst[int(input())] += 1

# 리스트를 오름차순으로 순회하면서 입력 받은 횟수 만큼 출력
for idx in range(len(lst)):
    if lst[idx] != 0:
        for j in range(lst[idx]):
            print(idx)

