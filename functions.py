print("Functions:\n")

is_Tired = True
print(type(is_Tired))

print(range(36))
print(len(range(36)))

print(list(range(36)))
for num in range(36):
    if num != 35:
        print(num, end=", ")
    else:
        print(num)

print()
num = '45' # string
print(int(num) + 3)

print("\nString Functions:")
my_string = 'Wanda NEEDS a NeW LaPTOp, and maybe a raise!'
full_name = "WaNDa DRizZle"
print(full_name.capitalize())
print(my_string.lower())
print(my_string.upper())

index_of_z = my_string.find("z")
print(index_of_z)

colors = ["Red", "Blue", "Yellow", "Purple", "Orange"]
colors.insert(2, "Green")
colors.append("Black")
print(colors[3])
print(colors)
colors.pop(3)
print(colors[3])
print(colors)

#12 April 2024
def rect(length, width):
  area = length * width
  perimeter = 2 * length + 2 * width
  return area, perimeter

x, y = rect(10, 5)
x, y = rect("five")

word = 'motorbike'
print(word.find('r'))
print(len(word))