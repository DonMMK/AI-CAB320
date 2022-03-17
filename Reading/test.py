import http
from nis import match

num = 2+2
print(num)

# .append
# setting into a null array to remove it

a, b = 0 , 1 # multiple assingment 
print(a, b)

while a < 10:
    print(a)
    a, b = b, a+b
    
# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
        
for i in range(5):
    print(i)
    
while True:
    pass # the pass statement does nothing. 
         # It can be used as a placeholder for code that will be written in the future.
    break # exit the loop

# match statements

def http_error(status):
   match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

http_error(404)

# Patterns

class Point:
    x: int
    y: int

# point is an (x, y) tuple
def where_is(point):
    match point:
        case (0, 0):
            print("Origin")
        case (0, y):
            print(f"Y={y}")
        case (x, 0):
            print(f"X={x}")
        case (x, y):
            print(f"X={x}, Y={y}")
        case _:
            raise ValueError("Not a point")
        
where_is()
    
# Documentation strings

def my_function():
    """ Do nothing, but document it
    
    
    """
    pass
    
print(my_function.__doc__)

# Naming conventions
# Name your classes and functions consistently; 
# the convention is to use UpperCamelCase for classes and lowercase_with_underscores for functions and methods. 
# Always use self as the name for the first method argument (see A First Look at Classes for more on classes and methods).


# Data Structures
# Lists: append , extend, insert, remove, pop, clear etc etc
# Use Lists as Stacks, Using Lists as Queues


# Modules
# 