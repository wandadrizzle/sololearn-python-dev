import keyword

print("Python keywords: ")
print(keyword.kwlist)

#There's no C# equivalent - https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/

print("\nWhat type is 'True'? ",type(True))

my_menu = ["Pizza", "Burger", "Salad"]

def show_menu(menu):
  print(menu)

print("\nA hardcoded menu:")
show_menu(my_menu)
print()

new_menu = []

def add_menu(menu, dish):
  menu.append(dish)


cart = []

def add_to_cart(cart):
  while True:
    product = input("What would you like to add to your cart? ")
    if product.lower() != "done":
        cart.append(product)
    else:
      print("\nThese are the things in your cart: ", cart)
      break

add_to_cart(cart)
#Simpson Chalkboard - BART
print()
print("I will not celebrate meaningless milestones.\n" * 100)

def passed(score):
  if score >= 70:
    return True

score = 65
print(passed(score)) 

def book_in_library(books, book):
  return book in books

books = [
  "Pride and Prejudice",
  "To Kill a Mockingbird",
  "The Lord of the Rings",
  "The Hitchhiker's Guide to the Galaxy",
  "Frankenstein",
  "One Hundred Years of Solitude",
  "The Great Gatsby",
  "Moby Dick",
  "Hamlet",
  "The Adventures of Huckleberry Finn"
]
print()

print("They have a copy of Yonder by Jabari Asim at the library: ", book_in_library(books, "Yonder"))
print("They have a copy of The Hitchhiker's Guide to the Galaxy by Douglas Adams at the library: ", book_in_library(books, "The Hitchhiker's Guide to the Galaxy"))

#Built-in Functions:
def calculate_the_most(price_list):
  total = sum(price_list)
  quantity = len(price_list)
  average_price = total/quantity
  maximum = max(price_list)
  minimum = min(price_list)
  return total, maximum, average_price, minimum

prices = [33, 49, 55, 14]
total = sum(prices)
print("\nThese are the sorted prices:", sorted(prices))
print("These are the sorted prices - descendig:", sorted(prices, reverse=True))
print("The total:", total)

total, max_price, avg, min_price = calculate_the_most(prices)
print(f"\nThe total is {total} and the average is {avg}. \nThe maximum and minimum prices are {max_price} and {min_price} respectively.")