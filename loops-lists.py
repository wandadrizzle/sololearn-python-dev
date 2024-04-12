ranks = ["Ace", "King", "Queen"]
suits = ["Hearts", "Clubs", "Diamonds"]

print_count = 0
outer = 0
for rank in ranks:
  outer += 1
  inner = 0
  for suit in suits:
    inner += 1
    card = rank + ' ' + suit
    if(card == "King Diamonds"):
        print("Outer loop iteration #: " + str(outer) + "\nInner loop iteration #: " + str(inner))
        break
    print(rank, suit)
    print_count += 1
    
print()    
print(print_count) #Original count without break was 9
days = ['Monday', 'Wednesday', 'Wednesday']
tasks = ['Gym', 'Homework', 'Pool']
for day in days:
  print('\n' + day + ': ', end="")
  tasks_str = ", ".join(tasks)
  print(tasks_str)
'''
 for task in tasks:
    print(task, end=", ")
'''
print()
scores = [45, 67, 89, 34, 56, 77, 49, 91, 52]

for score in scores:
  if score >= 70:
    print(score)

prices = [35, 80, 16, 100, 95, 76]
print()
for price in prices:
  if price < 90:
    break
  else:
    print(price)

print("\nAge appropriate guest list - NO UNDER 18s allowed")
ages = [13,19, 22, 8, 75, 34, 26, 41]
guest_ages = []
for age in ages:
  if age < 18:
    continue
  else:
    guest_ages.append(age)
print("The ages of the guests at my party are:")
print(guest_ages)
print()
products = ['ball', 'gloves']
colors = ['red', 'blue']
for i in products :
  for j in colors:
    print(j, i)
exit()