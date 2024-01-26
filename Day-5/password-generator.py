#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#easymode

password = ""

for n in range(0,nr_letters):
    randomvar = random.randint(0,51)
    password = password + letters[randomvar]

for n in range(0,nr_symbols):
    randomvar = random.randint(0,8)
    password = password + symbols[randomvar]

for n in range(0,nr_numbers):
    randomvar = random.randint(0,7)
    password = password + numbers[randomvar]


print(f"Your easy password is {password}")



#hard mode

hard_password = ''.join(random.sample(password,len(password)))

print(f"Your hard Password is {hard_password}")