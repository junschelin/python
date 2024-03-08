from car import Car

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23 #속성이 public이다.
my_new_car.update_odometer(13)
my_new_car.read_odometer()
my_new_car.update_odometer(33)
my_new_car.read_odometer()
my_new_car.increment_odometer(17)
my_new_car.read_odometer()
