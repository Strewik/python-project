# # compile time errors - 
# print("My name is not defined")

# for i in range(5):
#     print("hello world")
    
# # runtime errors

# c = 30
# d = 0

# print(c / d)
    
    
# # logical errors

# a = "1"
# b = "2"

# print(a + b)


a= 5
b = 0




try:
    print(a / b)
    print("open connection to database")
    
except Exception as e:
    print("You should not divide by zero", e)
    print("Can't connect to database")

finally:
    print("program got to this point")
    print("close database connection")

try:
    print(a / b)
    
except ZeroDivisionError as e:
    print("Can't divide by zero")
    
except TypeError as e:
    print("Can't devide different types of values")


