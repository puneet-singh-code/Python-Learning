# class car:
#     def drive(self):
#         return "car is moving"
    
# car1 = car()
# print(car1.drive())



# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def person_info(self):
#         print(f"The name of the person is {self.name} and the age is {self.age} years")

    
# p1 = Person("John Doe", 45)
# p1.person_info()



# class Animal:
#     def __init__(self,name):
#         self.name = name
#     def sound(self):
#         print("Some sound")
    
# class Dog(Animal):
#     def sound(self):
#         print("Bark!")

# d1 = Dog("shiro")
# d1.sound()



class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        print("Bark!")

a = Animal()
a.sound()

b = Dog()
b.sound()
