import sys

input = sys.stdin.readline

n=int(input().rstrip())


def danceCount(n):
	dance_set=set()
	isChong = False
	for _ in range(n):
		# input_set = set(input().split())
		input_set = set(sys.stdin.readline().split())
        
		if 'ChongChong' in input_set:
			isChong = True
			dance_set |= input_set
   
		if isChong:
			for item in input_set:
				if {item}.issubset(dance_set):
					dance_set |= input_set


	return len(dance_set)
	
print(danceCount(n))