class Flyer:
    def fly(self):
        print("Flying in the sky")

class Swimmer:
    def swim(self):
        print("Swimming in the water")

class Duck(Flyer, Swimmer):
    def quack(self):
        print("Quack!")

d = Duck()
d.fly()
d.swim()
d.quack()