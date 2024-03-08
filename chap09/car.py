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

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23 #속성이 public이다.
my_new_car.update_odometer(13)
my_new_car.read_odometer()
my_new_car.update_odometer(33)
my_new_car.read_odometer()
my_new_car.increment_odometer(17)
my_new_car.read_odometer()
