class Car:
    car = "Toyota" # class property
    def __init__(self, brand):
       self.brand = brand # Instance property
    def show(self):
       print(self.brand)
c1 = Car("Ford")
c1.show()
c1.brand = "BMW"
c1.show()