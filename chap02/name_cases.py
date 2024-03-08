# 2-3~4 문제

msg = '안녕하세요.'
name = "eric"
print(f"{msg} {name}, 오늘 파이썬 배워 보는게 어떨까요?")

print(name.upper())
print(name.lower())
print(name.title())

# 2-5 명언
print("알베르트 아인슈타인, \"한 번도 실수한 적이 없는 사람은 한 번도 새로운 것에 도전해 본 적이 없는 사람이다.")
print('알베르트 아인슈타인, "한 번도 실수한 적이 없는 사람은 한 번도 새로운 것에 도전해 본 적이 없는 사람이다.')

# 2-6 명언2
famous_person = "알베르트 아인슈타인"
message = f"{famous_person}, \"한 번도 실수한 적이 없는 사람은 한 번도 새로운 것에 도전해 본 적이 없는 사람이다."
print(message)

# 2-7 이름에서 공백 제거
name_ = "  알베르트_아인슈타인  "
print(name_)
print(name_.lstrip())
print(name_.rstrip())
print(name_.strip())

# 2-8 파일 확장자
filename = 'python_notes.txt'
print(filename.removesuffix('.txt'))