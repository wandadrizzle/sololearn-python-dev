#12 April 2024
colors = ["Yellow", "Red", "Blue"]
print("colors list original: ", colors)
colors[1] = "Orange"
colors.append("Black")
print("colors list after edits: ", colors)

################################################Tuples
b_date = (6, "August", 1996)
birth_month = b_date[1]
day, month, year = b_date
print("\nYou were born in:", birth_month)
print("Using Tuple unpacking -  you were born in:", month)
#b_date[1] = "July" #TypeError: 'tuple' object does not support item assignment

print()
scores = (7, 9, 9, 8, 9)
print("Number of scores:", len(scores))
print(scores.count(7))
print(scores.count(9))
print(scores.count(2))

print()
points = (12, 14, 9, 10, 9)
for point in points:
  if point > 10:
    print(point, ": passed")

languages = ("Korean", "Hindi", "Afrikaans", "Portuguese", "German")
favourite_language, *rest = languages
print("\nAfter I learn Korean I'll learn:", rest)

################################################Sets - used for unique data, unordered
planets = {"Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Mecury", "Venus", "Earth", "Mars"} #The duplicate 'Mars' will be discarded
#print(planets[2]) #TypeError: 'set' object is not subscriptable
print()
print(planets)
planets.add('Pluto') #append doesn't work with sets because they are unordered
planets.remove('Earth')
print("Edited planets set:", planets)
planets.clear()
planets.add("Wolf 1069")
print("\nAdded a planet to empty planet set:", planets)
exoplanets = ["Gliese 176", "EQ Pegasi", "TZ Arietis", "Wolf 1069","Luyten's Star", "Ross 128"]
planets.update(exoplanets)
print("Added a planets list to planet set:", planets)

print()
set1 = {'apple', 'banana'}
set2 = {'banana', 'cherry'}
combined_set = set1.union(set2) #The union() function called returns a new set with all elements from both sets, omitting duplicates.
print(combined_set)

print()
set1 = {'apple', 'banana', 'cherry'}
set2 = {'banana', 'orange'}
unique = set1.difference(set2) #The difference() function returns a set containing elements that are only in the first set and not in the second.
print(unique)
################################################Dictionaries
emergency_contact = {
  "name" : "The Popo",
  "number": 911
}

print("\nNote that any immutable datatype can be used as a key:\nint, float, complex, bool, str, tuple, frozenset\n")

dancer = {
  "name": "Maria",
  "points_from_judges": [8, 6, 10]
}

car = {
  "brand": "Audi",
  "model": "Q5",
  "model": "A5" #Note - since duplicate keys aren't allowed, value will be overwritten
}

print(car)
print(car["model"])

brand = car.get("brand")
print(brand)

car_keys = car.keys()
car_values = car.values()
print(f"\nMay car dictionary has:\nKeys: {car_keys}\nValues: {car_values}")
print("Items:",car.items())

print()
car["brand"] = "Renault"
car["model"] = "Kwid"
print("I've edited my car:",car)
car.update({"model":"Kiger", "year": 2024, "color": "White"})
print("I've edited my car again:",car)
car.pop("year")
print(car)
print("color" in car)

print()
for i in car:
  print(i)

print()
for i in car.values():
  print(i)
################################################List Comprehensions
print()
nums = []

'''
for x in range(1,51):
  nums.append(x)
'''
nums = [x for x in range(1,51)] #shorthand

for num in nums:
  print(num, end=", ")

print("\n")
for i, num in enumerate(nums):
    if i == len(nums) - 1:
        print(num, end="")
    else:
        print(num, end=", ")
        
print("\n")
result = ", ".join(str(num) for num in nums)
print(result)

'''
<variable> = [<expression> for <item> in <iterable]

<variable>: the variable that will store the newly created list
<expression>: an expression performed on each item. If no specific action is needed, the item itself is used
<item>: the current item being processed
<iterable>: any iterable object, such as ranges, lists, strings, tuples, and sets
'''
print()
nums = [x*2 for x in range(10)]
print(nums)

print()
tags = ["python", "webdev", "100daysofcode"]
hashtags = ["#" + x for x in tags]
hashtags = ["#" + x for x in tags if x == "python"]
print("I'm a tech girly!\n")

for hashtag in hashtags:
   print(hashtag, end=" ")
