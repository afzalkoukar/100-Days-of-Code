import random

names_string = input("Give me everybody's names, seperated by a comma.\n")
names = names_string.split(', ')
end = len(names)-1

randomnumber = random.randint(0,end)

print(f"The bill should be paid by {names[randomnumber]}. ")