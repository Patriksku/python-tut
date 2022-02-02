class Car:

    make = None
    model = None
    year = None
    color = None
    wheels = 4  # class variable

    def __init__(self, make, model, year, color):  # Constructor
        self.make = make    # instance variable
        self.model = model  # instance variable
        self.year = year    # instance variable
        self.color = color  # instance variable

    def drive(self):  # Refers to the object that is using this method
        print("This " + self.make + " is driving")

    def stop(self):
        print("This " + self.make + " is stopped")

