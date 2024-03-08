import string 
alphabet_upper = string.ascii_uppercase
lst_number = []

for alphabet in alphabet_upper:
    lst_number.append(0)

word = input().upper()

for w in word:
    i = alphabet_upper.find(w)
    lst_number[i] += 1

if lst_number.count(max(lst_number)) > 1:
    print("?")
else:
    max_index = lst_number.index(max(lst_number))
    max_char = alphabet_upper[max_index]
    print(max_char)