class Shape:
    def __init__(self, base, height):
        self.__base = base  # private 변수
        self.__height = height  # private 변수

    @property  # getter decorator
    def base(self):
        return self.__base

    @property  # getter decorator
    def height(self):
        return self.__height

    @height.setter  # setter decorator
    def height(self, value):
        self.__height = value

new_shape = Shape(5, 10)

i = new_shape.base
j = new_shape.height
print(i, j)
new_shape.height = 15
i = new_shape.base
j = new_shape.height
print(i, j)



# def get_data():
#     return 1, 2, 3
# _,a,b = get_data() # _ : 관심없는 데이터를 받는 변수를 지정할 때 사용

# a = [1, 2, 3] 
# b = [11, 22, 33]
# mylist_1 = [*a, *b]
# mylist_2 = [a, b] #병합
# print(mylist_1)
# print(mylist_2)

# c = ['a', 'b']
# z = zip(a,c)
# print(list(z))