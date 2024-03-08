# # 함수의 매개변수로 함수 전달

# def ten_times(func):
#     for i in range(5):
#         func()


# def print_hello():
#     print("hello")


# ten_times(print_hello)

# def print_work():
#     print('coding')

# ten_times(print_work)

# def add(x,y):
#     return x + y

# def minus(x,y):
#     return x - y

# def apply_operation(operation, x, y):
#     return operation(x,y)

# result = apply_operation(add, 3, 4)
# result2 = apply_operation(minus, 3, 4)

# print(f"add 결과 = {result}, minus 결과 = {result2}")

# #map(), filter()함수 사용
# def power(item):
#     return item * item

# def under_three(item):
#     return item < 3

power = lambda x: x*x
under_three = lambda x : x<3

lst = [1, 2, 3, 4, 5]
map_list = map(power, lst)
print(f"map() 함수 적용결과 : {list(map_list)}")

filter_list = filter(under_three, lst)
print(f"filter() 함수 적용결과 : {list(filter_list)}")

# 함수 선언 없이 바로 람다식 사용
lambda_list = map(lambda x:x+3, lst)
print(f"lambda식 적용 결과 : {list(lambda_list)}")
