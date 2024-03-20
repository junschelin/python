class Restaurant:

    def __init__(self, restaurant_name, cusine_type):
        """레스토랑 정보"""
        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type
    
    def describe_restaurant(self):
        print(f"레스토랑 이름 : {self.restaurant_name} / 요리 타입 : {self.cusine_type}")

    def open_restaurant(self):
        print("opened")

class IceCreamStand(Restaurant):
    
    def __init__(self, r_name, c_type, flavors):
        super().__init__(r_name, c_type)
        self.flavors = flavors

new_ice = IceCreamStand("베스킨라빈스", "디저트", "체리쥬빌레")
new_ice.describe_restaurant()

# new_rest = Restaurant('자마미', '등갈비')
# new_rest.describe_restaurant()
# new_rest.open_restaurant()

# my_rest1 = Restaurant('곁집', ' 비빔밥')
# my_rest2 = Restaurant('겸', '돈까스')
# my_rest3 = Restaurant('철인7호', '치킨')

# my_rest1.describe_restaurant()
# my_rest2.describe_restaurant()
# my_rest3.describe_restaurant()
