class Animal:
    def speak(self):
        print("The animal makes a sound")


class Dog(Animal):
    def speak(self):   # overriding parent method
        print("The dog barks")


class Cat(Animal):
    def speak(self):   # overriding parent method
        print("The cat meows")


a = Animal()
d = Dog()
c = Cat()

a.speak()   # The animal makes a sound
d.speak()   # The dog barks
c.speak()   # The cat meows