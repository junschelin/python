class Car:
    """자동차를 표현하는 클래스"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """거리계를 주어진 값으로 설정합니다.
            현재 값보다 적게 수정은 불가"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("주행기록계를 줄일 수 없습니다.")

    def increment_odometer(self, miles):
        """거리계 값을 주어진 값만큼 늘립니다"""
        self.odometer_reading += miles


class Battery:
    """전기차의 배터리를 표현하는 클래스"""

    def __init__(self, battery_size=40):
        """배터리 속성을 초기화합니다"""
        self.battery_size = battery_size
    
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery")

        

class ElectricCar(Car): # 상속할 때는 (괄호안에 부모 클래스 입력)
    """전기차에만 해당하는 특징을 정의합니다"""

    # def __init__(self, make, model, year, battery):
    #     """부모 클래스의 속성을 초기화합니다"""
    #     super().__init__(make, model, year)
    #     self.battery_size = battery

    def __init__(self, make, model, year, large_battery=Battery()):
        super().__init__(make, model, year)
        self.battery = large_battery

    def describe_battery(self):
        """배터리 크기를 설명하는 문장을 출력합니다"""
        print(f"This car has a {self.battery}-kWh battery")

    def get_descriptive_name(self):
        long_name = f"{super().get_descriptive_name()} {self.battery}"
        return long_name.title()

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23 #속성이 public이다.
my_new_car.update_odometer(13)
my_new_car.read_odometer()
my_new_car.update_odometer(33)
my_new_car.read_odometer()
my_new_car.increment_odometer(17)
my_new_car.read_odometer()
