import sys
input = sys.stdin.readline

n = int(input().rstrip())
dance_set = set()
isChong = False

for _ in range(n):
    input_set = set(input().split())
    
    if 'ChongChong' in input_set:
        isChong = True
        dance_set |= input_set
    
    if isChong:
        for item in input_set:
            if {item}.issubset(dance_set):
                dance_set |= input_set

    print("input : ", input_set)
    print("dance_set : ", dance_set)


print(len(dance_set))

# 12
# bnb2011 chansol
# chansol chogahui05
# chogahui05 jthis
# jthis ChongChong
# jthis jyheo98
# jyheo98 lms0806
# lms0806 pichulia
# pichulia pjshwa
# pjshwa r4pidstart
# r4pidstart swoon
# swoon tony9402
# tony9402 bnb2011