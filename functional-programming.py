def welcome(name):
  return "Welcome, " + name
greet = welcome #I am assigning a function to a variable

print(greet("Wanda"))

def process_user(name, func): #A higher order function, return functions and take in functions as arguments
    return func(name)

print(process_user("Alice", welcome))

'''
Pure Functions:
Deterministic: A pure function always returns the same output for the same input values.
No Side Effects: It doesn't modify any external state (variables, files, databases) outside of its function scope.

The function is impure if it depends on any external state that it modifies or that affects its output. 
eg.: Functions that depend on input()
'''

#Lambda Expressions for single + concise expressions
def total(price, count):
  return price*count

print()
print(total(2,3))

print()
# lambda <argument> : <expression> | They are anonymous but you can assign the lambda expression to a variable and then call it as a regular function.
greet = lambda name: "Welcome, " + name

print(greet("Bob"))
res = (lambda x, y: x + y) (2, 3)
print(res)

print()
def mult(n):
  return lambda a : a * n #These are useful in data manipulation

doubler = mult(2)
tripler = mult(3)
print(doubler)
print(tripler)
print()
print(doubler(5))
print(tripler(5))


print()
names = ["alice", "bob", "CHARLIE", "Tom"]


#The map functions is a higher order function angithi?
def capitalize(name):
  return name.capitalize()

#map(<function>, <iterable>)
capitalized = map(capitalize, names)
capitalized = list(capitalized)

#Regular Expressions ?

import re

def is_valid_email(email):
  pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]+$"  # Email address pattern
  return re.match(pattern, email) is not None  # Check if email matches the pattern

email = "testing@fakemail"
#if is_valid_email("user@example.com"):
if is_valid_email(email):
    print("Valid email address")

numbers = [1, 2, 3]
doubled = list(map(lambda x: x*2, numbers))
print(doubled)

products = ["Table", "Sofa", "Cushion", "Bookshelf", "Vase"]
filtered_prod = list(filter(lambda name: len(name) == 4, products)) #Items that meet a condition
print(filtered_prod)

products = {'Table': 110, 'Sofa': 120, 'Chair': 45, 'Lamp': 70}
filtered = dict(filter(lambda item: item[1] < 90, products.items()))
#Here, products.items() returns key-value pairs as tuples. In each tuple, item[1] is the value (price), and item[0] is the key (product name).
print(filtered)

#UNKNOWN NUMBER OF ARGUMENTS

def total(numbers): #USE A LIST
  result = 0
  for i in numbers:
    result+=i
  return result

#def <func> (<argument>, <*args>, <**kwargs>)
def total(*args): #args is a Tuple, iterable?
  result = 0
  for arg in args:
    result += arg
  return result

def show_items(category, *items): #function signature
  print("Category: " + category)
  for item in items:
    print(item)

#Python also allows you to pass keyword arguments using **kwargs. - dictionary
'''
The ** operator in Python is used to unpack dictionaries into arguments. 
It enables a function to accept an arbitrary number of keyword arguments, 
converting these arguments into a dictionary of key:value pairs.
'''
def display_info(**kwargs):
  for key, value in kwargs.items():
    print(key, ":", value)

#Decorators
#In Python functions can be nested
print()
def outer_function():
    print("Hello from the outer function")

    def inner_function():
        return "Hello from the inner function"

    inner_message = inner_function()
    return inner_message

print(outer_function())

#?????
