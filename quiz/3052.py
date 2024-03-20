n = 0
lst = []
cnt = 0

while n<10:
    user_input = input()
    lst.append(int(user_input))
    n+=1

left_num_set = set()

for i in lst:
    left_num_set.add(i%42)

print(len(left_num_set))