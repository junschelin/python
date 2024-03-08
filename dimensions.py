dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

my_dimension = (200,)
print(my_dimension)


# 4-13 연습문제

menus = ("떡볶이", "참치회", "문어숙회", "킹크랩", "랍스터")

for menu in menus:
    print(menu)

# menus[1] = "참치찌개" # 이 코드는 오류남 (왜냐면 튜플은 immutable)
# print(menus)
    
menus = ("떡볶이", "김치찌개", "오뎅탕", "킹크랩", "랍스터")

for menu in menus:
    print(menu)
