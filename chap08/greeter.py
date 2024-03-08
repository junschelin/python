# input_name = 'jessi'
# greet_user(input_name)
# print(input_name)

# # greet_user()
# # help(greet_user) #함수명, docstring 출력
# # print(greet_user.__doc__) #docstring 출력

# a = 'abc'
# print(hex(id(a)))
# a = 'bbc'
# print(hex(id(a)))



def greet_user(username): #String은 immutable
    """인사말""" #docstring : 주석과 비슷
    print(f"hello, {username.title()}")
    username='kim'

def get_formatted_name(first_name, last_name):
    """실제 이름을 깔끔한 형식으로 반환합니다"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# 무한 루프입니다!
while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}")

