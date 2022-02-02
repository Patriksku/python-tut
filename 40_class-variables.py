from car import Car

car_1 = Car("Volvo", "X80", "2018", "Green")
car_2 = Car("Ford", "Mustang", "2022", "Red")

car_1.wheels = 2
print(car_1.wheels)
print(car_2.wheels)


print(Car.wheels)
Car.wheels = 2  # Now we change the class variable "wheels" for all instances of the Car-class.









