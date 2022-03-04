import http


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