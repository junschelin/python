class User:
    
    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last
    
    def describe_user(self):
        print(f"이름 : {self.last_name}{self.first_name}")

    def greet_user(self):
        print(f"{self.last_name}{self.first_name}님 환영합니다!")

# user = User("존", "박")
# user.describe_user()
# user.greet_user()