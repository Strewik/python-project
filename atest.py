class Student:
    
#method 
 def __init__(self, fname, lname, age, grade):

    self.fname = fname
    self.lname = lname
    self.age = age
    self.grade = grade

#method 
 def say_hi(self):
    print('Hello, my name is', self.fname, self.lname)

student1 = Student("Emeka", "Wigwe", 6, 2)

print(student1)

print(student1.fname, student1.lname, student1.age, student1.grade)

print(student1.say_hi())




#child class

class Department(Student):

#method
 def __init__(self, fname, lname, age, grade, sex, dept):
    super().__init__(fname, lname, age, grade)
    self.sex = sex
    self.dept = dept

#override method
 def say_hi(self):
    print('My grade is', self.grade)

student3 = Department("Janeth", "Wejinya", 6, "second grade", "Female", "Primary section")

print(student3.fname, student3.lname, student3.age, student3.grade, student3.sex, student3.dept)

print(student3.say_hi())




print("=======================================================================================================")

class Dog:

#method 
    def __init__(self, name, color, age):
      self.name = name 
      self.color = color
      self.age = age

#method
    def say_hi(self):
        print('Hello, my dogs name is', self.name)

dog1 = Dog("Bingo", "Brown", 7)

print(dog1)

print(dog1.say_hi())



#child class

class Owner(Dog):

#method
    def __init__(self, name, color, age, gender, breed):
       super().__init__(name, color, age)
       self.gender = gender
       self.breed = breed

#override method
    def say_hi(self):
     print('My dog is an', self.breed)

dog2= Owner("Jack", "Grey", 6, "Male", "Alsatian")

print(dog2)

print(dog2.say_hi())