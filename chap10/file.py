# with open('백준문제리스트.txt', encoding='utf-8') as file:
#     print(file.readlines())
#     for line in file:
#         print(line, end='')

# def add(a=1,b=2):
#     return a+b

# print(add(3,4))
# print(add())

import csv

with open('chap10/grade.csv') as file:
    reader = csv.reader(file)
    for line in reader:
        print(line)


from pathlib import Path
file_path = Path ('./name.txt')
dir_path = Path ('./')
print(file_path)

import os
print(os.path.isdir(file_path))
print(os.path.isdir(dir_path))

for d in os.listdir():
    print(d, os.path.isdir(d))
    if '.txt' in d:
        print('.txt found')

no_file = Path('./aaa/b.txt')
is_file = Path('./chap10/aaa/aaa.txt')
print(os.path.exists(no_file))
print(os.path.exists(is_file))