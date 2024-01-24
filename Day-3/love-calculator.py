print("Welcome to love calculator\n")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lowername1 = name1.lower()
lowername2 = name2.lower()

t = name1.count('t') + name2.count('t') 
r = name1.count('r') + name2.count('r')
u = name1.count('u') + name2.count('u')
e = name1.count('e') + name2.count('e')

truetotal = t+r+u+e

l = name1.count('l') + name2.count('l') 
o = name1.count('o') + name2.count('o')
v = name1.count('v') + name2.count('v')
e2 = name1.count('e') + name2.count('e')

lovetotal = l+o+v+e

total = (truetotal*10)+lovetotal

if(total<10 or total > 90):
    print(f"your love score is {total}, You go like coke and mentos")
elif(total >= 40 and total<=50):
    print(f"Your love score is {total}, You will be alright")
else:
    print(f"your love score is {total}")

