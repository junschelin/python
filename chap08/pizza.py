def make_pizza(size, *toppings):
    """주문 내용 요약"""
    print(f"Masking {size}-inch pizza 다음 토핑으로")
    for topping in toppings:
        print(f" - {topping}")

        

# def make_pizza(size, *toppings):
#     """요청받은 토핑 리스트를 출력합니다"""
#     print(f"\nMaking a {size}-inch pizza with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")

# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peepeers', 'extra cheese')