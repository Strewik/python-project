
# class Employee:
#     fname = "John"
#     lname = "Doe"
#     age = 30
    
#     def __init__(
#         print("post")
#     )
# class Employee:
#     fname = "Jane"
#     lname = "Doe"
#     age = 30
    
#     def __init__(
#         print("post")
#     )
# class Employee:
#     fname = "Kapere"
#     lname = "Doe"
#     age = 30
    
#     def __init__(
#         print("post")
#     )

# A Sample class with init method
# Parent
class Person(object):
 
    # init method or constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    # Sample Method
    def say_hi(self):
        print('Hello, my name is', self.name)
 
 
# p = Person('Nikhil')
# p.say_hi()

person1 = Person("Kapere", 30)
person2v= Person("john", 60)
person3= Person("jane", 20)

print(person1)
print(person1.name)
print(person1.age)

print(person1.say_hi())

print("==================================================")


class Employee(Person):
    # Constructor
    def say_hi(self):
        print('My new age this year is ', self.age)





person5 = Employee("Gabby", 12)
print(person5.name)

print(person5.say_hi())

# Inheritance
# Child class
# class Employee(Person):
#     # Constructor
#     def __init__(self, name, age, gender, phone, dept):
#         self.gender = gender
#         self.phone = phone
#         self.dept = dept




# # person5 = Employee("Gabby", 12)
# # print(person5.name)
# person6 = Employee("Gabby", 12, "Female", 998963974, "Developer" )
# print(person6.name)




class Base(object):
     
    # Constructor
    def __init__(self, name):
        self.name = name
 
    # To get name
    def getName(self):
        return self.name
 

