# method chaining = calling multiple methods sequentially
#                   each call performs an action on the same object and returns self

class Car:

    def turn_on(self):
        print("Starting engine")
        return self

    def drive(self):
        print("You drive the car")
        return self

    def brake(self):
        print("Braking")
        return self

    def turn_off(self):
        print("Stopping engine")
        return self


car = Car()

# Line continuation symbol '\'
car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()



