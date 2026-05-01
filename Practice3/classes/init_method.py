class Data:
  def __init__(self, name, age, phone, country):
    self.name = name
    self.age = age
    self.phone = phone
    self.country = country

n = input("Enter your name: ") 
a = int(input("Enter your age: ")) 
p = input("Enter your phone: ")
c = input("Enter your country: ")
p1 = Data(n, a, p, c)

print(p1.name)
print(p1.age)
print(p1.phone)
print(p1.country)