lst_credit = list()
lst_grade = list()
lst_total = list()
cnt = 0
while cnt<=20:
    input_string = input().split()
    cnt +=1

    name = input_string[0]
    credit = float(input_string[1])
    grade = input_string[2]
    
    if grade == 'A+':
        lst_grade.append(4.5)
        lst_credit.append(credit)
    elif grade == 'A0':
        lst_grade.append(4.0)
        lst_credit.append(credit)
    elif grade == 'B+':
        lst_grade.append(3.5)
        lst_credit.append(credit)
    elif grade == 'B0':
        lst_grade.append(3.0)
        lst_credit.append(credit)
    elif grade == 'C+':
        lst_grade.append(2.5)
        lst_credit.append(credit)
    elif grade == 'C0':
        lst_grade.append(2.0)
        lst_credit.append(credit)
    elif grade == 'D+':
        lst_grade.append(1.5)
        lst_credit.append(credit)
    elif grade == 'D0':
        lst_grade.append(1.0)
        lst_credit.append(credit)
    elif grade == 'P':
        lst_grade.append(0.0)
        lst_credit.append(0.0)      
    else:
        lst_grade.append(0.0)
        lst_credit.append(credit)

    if cnt == 20:
        break

for i in range(len(lst_grade)):
    plus = lst_grade[i] * lst_credit[i]
    lst_total.append(plus)

total_score = sum(lst_total)
total_credit = sum(lst_credit)

print(float(total_score / total_credit))