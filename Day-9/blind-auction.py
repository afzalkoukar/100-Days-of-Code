import os

def cls():
    os.system('cls')

from art import logo

print(logo)

contin = True
TotalBids = {}

while (contin):
    
    name = input("Enter your name: \n")
    bid = int(input("Enter your bid: \n"))

    TotalBids[name] = bid

    Any_more_user = input("Are there more users, Say yes or no\n")

    if (Any_more_user == "yes" or Any_more_user == "YES"):
            contin = True
            cls()
    elif (Any_more_user == "NO" or Any_more_user == "no"):
            contin = False

highest_bid = 0

for key in TotalBids:
      if(TotalBids[key] > highest_bid):
        highest_bid = TotalBids[key]

key_list = list(TotalBids.keys())
val_list = list(TotalBids.values())

position = val_list.index(highest_bid)

print(f"Highest Bid is {key_list[position]}: {highest_bid}")