#print("New Message) #SyntaxError: unterminated string literal

salary = 50000
#role = Analyst #NameError: name 'Analyst' is not defined
#age -> 29 #SyntaxError: invalid syntax (1)
print(salary)

print()
name = "Mery"
surname = "Osborn"
print(name + surname)
print(name, surname)

print()
data = ["anna", "bob", "mery"]
#names = [x.upper() for x in data]
names = [x.capitalize() for x in data]
print(names)

print()
name = "Bob"
#name[0] = "R" #TypeError: 'str' object does not support item assignment
print(name)

print()
cars = ["BMW", "Tesla", "Ford"]
print(cars[1])
#print(cars[4]) #IndexError: list index out of range

print()
message = 5 #TypeError: object of type 'int' has no len()
message = "Hello"
length = len(message)

data = "message" #ValueError: invalid literal for int() with base 10: 'message' | Inappropriate value
data = "12345"
num_data = int(data)
'''
Note - Compilers typically catch errors in a specific order.

1. Lexical Analysis - tokens: keywords, identifiers, operators
2. Syntax Analysis - "is your code grammatically correct"
3. Semantic Analysis -

Bugs are flaws or mistakes in a program's code, leading to incorrect or unintended behavior. LOGICAL ERRORS?
Exceptions are another category of mistakes in programming - WILL BREAK CODE
'''


#EXCEPTION HANDLING
prices = [250, 300, "240", 400]
try:
  total = sum(prices)
  print(total)
except TypeError:
  print("Invalid data type")

print("Happy Shopping")

print()
colors = ['Red', 'Yellow', 'Green']
try:
  print(colors[10])
except NameError: #with this alone your program will still fail because you're expecting the wrong type of error
  print("Error: variable not defined")
except IndexError as ex:
  print("Your list isn't that large, index out of range")
  print(ex)

print("Taste the rainbow")

print()

products = ["Scarves", "Hats", "Braletes"]
#products = "3 mugs"
#products = True

try:
  for product in products:
    print(product)
except Exception as ex:
    error_message = str(ex)  # or error_message = ex.__str__()
    print(error_message)
else:
    print("Great products neh")
    '''  
    except:
    print("An unexpected error occurred.")
    '''  
finally:
  print("Okay, that's it those are all the products we have.")

print()
try:
  print(3 + "3")
except ValueError:
  print("Cannot add different types")
except TypeError:
  print("Type mismatch error")

#There are some things you want to avoid that can't be caught by the computer so - RAISE AN EXCEPTION NANA

print("\nRate from 0 to 10")
try:
   
    rate = 15
    if rate > 10 or rate < 0:
        raise ValueError
except ValueError:
   print("Ratings can only be from ZERO to TEN | 0 - 10")

#print(len(93)) #TypeError: object of type 'int' has no len()


year_born = 93
if not isinstance(year_born, int) or len(str(year_born)) != 4:
    raise ValueError("Year born must be a four-digit integer.")
