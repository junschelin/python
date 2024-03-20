n = int(input())

lst = []

for idx in range(n):
	age, name = input().split()
	lst.append((int(age),name,idx))
	
s_lst = sorted(lst, key=lambda x : (x[0],x[2]))

for item in s_lst:
	print(item[0], item[1])