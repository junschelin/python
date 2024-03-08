# cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort()
# print(cars)
# print(sorted(cars, reverse=True))
# print(cars)


# print("===========================")
# print(len(cars))
# print(cars[-1])


# cars = ['bmw', 'audi', 'toyota', 'subaru']
# for car in cars: #자바에서 말하는 확장형 for 문 // JAVA : for (int n : arr)
#     print(car)
#     print(f"my car is a {car}")

cars = ['bmw', 'audi', 'toyota', 'subaru']
for car in cars:
    if car == 'bmw' :   
        print(car.upper())
    else:
        print(car.title())


def make_car(manufacturer, model_name, **car_information):
    car_information['manufacturer'] = manufacturer
    car_information['model_name'] = model_name
    return car_information

car_info = make_car('subaru', 'outback', color='blue', tow_package=True)

print(car_info)