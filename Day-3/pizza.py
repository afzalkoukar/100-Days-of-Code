print("Welcome to Pizza Place\n")

size=input("What size do you wanr, S, M or L\n")
pep = input("Do you want pepporoni, Y or N\n")
cheese = input("Do you want Extra cheese, Y or N\n")

if(size == "S" or size == "s"):
    amount = 15
    if(pep=="y" or pep =="Y"):
        amount=amount+2


elif(size == "M" or size == "m"):
    amount = 20
    if(pep=="y" or pep =="Y"):
        amount=amount+3


else:
    amount = 25
    if(pep=="y" or pep =="Y"):
        amount=amount+3



if(cheese=="Y" or cheese == "y"):
    amount=amount+1


print(f"Total amount is {amount}")