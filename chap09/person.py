from typing import Any


class Person:
    count = 0 #클래스 변수
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        self.weight = [65, 67, 70, 71] #공개속성
        self.__vision = 1.0 #private 속성
        self.height = 170
        Person.count += 1
        print("{}객체가 생성됨".format(self.name))
    
    @classmethod #decorator
    def printing(cls):
        print("객체 수는 {}".format(cls.count))


    def show_person_vision(self):
        print("시력은 {}".format(self.__vision))

    def __str__(self): # Person은 객체 : 출력 시 필요한 것은 String
        return "{}\t{}\t{}".format(self.name, self.age, self.address)
    
    def __len__(self):
        return len(self.weight)
    
    def __eq__(self,other):
        return self.age == other.age
    
    def __call__(self):
        return self.weight / self.height **2
    
    def __getitem__(self,indx):
        return self.weight[indx]

    def __del__(self):
        print("객체 {}이 소멸됨".format(self.name))


Person('guest',11,'jeju')
new_person = Person('hong', 20, 'busan')
other_person = Person('kim', 20, 'masan')
# print("이 사람은 {}".format(new_person.name))
# print(f"몸무게는 {new_person.weight}")
# print("시력은 {}".format(new_person.__vision)) 
# new_person.show_person_vision()
# str = new_person.__str__()

# print(new_person.__str__())
# print(str(new_person))
# print(new_person)

# print(new_person==other_person)

# print(f"리스트 길이 {len(new_person)}")

# print(f"BMI 지수 : {new_person()}")

# print(f"현재 체중은 {new_person[2]}kg")

# print("객체의 타입은 같은가? {}".format(isinstance(new_person, Person)))

# print(f"person 객체의 나이는**{new_person.age:5}***")

# a = '='
# print(f"**{a:5}**")

print(f"{Person.count} 객체가 생성됨")
print(f"{new_person.count} 객체가 생성됨")
print(f"{other_person.count} 객체가 생성됨")

Person.printing() ### 클래스 메서드 호출 (객체 생성 없이 바로 사용 가능)
