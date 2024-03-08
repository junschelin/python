# input 예시 IntroductiontoComputerEngineering 3.0 A+

lst_credit = list()
lst_grade = list()


while True:
    input_string = input().split()
    if not input_string:
        break

    name = input_string[0]
    credit = float(input_string[1])
    grade = input_string[2]
    lst_credit.append(credit)
    
    if grade == 'A+':
        lst_grade.append(4.5)
    elif grade == 'A0':
        lst_grade.append(4.0)
    elif grade == 'B+':
        lst_grade.append(3.5)
    elif grade == 'B0':
        lst_grade.append(3.0)
    elif grade == 'C+':
        lst_grade.append(2.5)
    elif grade == 'C0':
        lst_grade.append(2.0)
    elif grade == 'D+':
        lst_grade.append(1.5)
    elif grade == 'D0':
        lst_grade.append(1.0)
    else:
        lst_grade.append(0.0)

print(lst_credit)
print(lst_grade)


print(sum(lst_credit), sum(lst_grade))

