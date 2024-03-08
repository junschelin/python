class Dog:
    """개 클래스"""

    def __init__(self, name, age, price=100):
        self.name = name
        self.age = age
        self.__price = price

    def sit(self):
        print(f"{self.name} is 앉기")

    def get_price(self):
        return self.__price    

my_dog = Dog('Willie', 6, 100)#생성자 호출 > 인스턴스 생성 < __init__() 함수가 자동 호출
my_dog.sit()
print(f"개 이름은 {my_dog.name} + {my_dog.get_price()}$")

