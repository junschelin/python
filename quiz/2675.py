n =int(input())
input_lst = []
for i in range(n):
    user_input = input().split()
    input_lst += user_input

repeat_num_lst = []
repeat_str_lst = []

for repeat in input_lst[::2]:
    repeat_num_lst.append(int(repeat))

for repeat in input_lst[1::2]:
    repeat_str_lst.append(repeat)

for i in range(len(repeat_num_lst)):
    for letter in repeat_str_lst[i]:
        print(letter*repeat_num_lst[i], end='')
    if i != len(repeat_num_lst) -1 :
        print()