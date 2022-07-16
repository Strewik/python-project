# def FunctionName(args):
#     '''docstring'''
#     function-body
    
# function declaration 
def greet(name):
    """A funtion to greet a user"""
    print('Hello, ' + name + '. How are you?')
    
# function calling/ invoking a function
greet('Jane Doe')
greet('John Doe')
greet('Elijah')



def absolute_value(num):
    if num >= 0:
        return num
    else:
        return -num
    
print(absolute_value(5))
print(absolute_value(-5))


envName/bin/activate