import random
user = int(input("Type 0 for rock, 1 for paper and 2 for scissors\n"))

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

comp =random.randint(0,2)

if(user == 0):
    print(f"you choice is \n{rock}")

elif(user==1):
    print(f"you choice is \n{paper}")

elif(user==2):
    print(f"you choice is \n{scissors}")


if(comp == 0):
    print(f"comp choice is \n{rock}")

elif(comp==1):
    print(f"comp choice is \n{paper}")

elif(comp==2):
    print(f"comp choice is \n{scissors}")

if user >= 3 or user < 0: 
  print("You typed an invalid number, you lose!") 
elif user == 0 and comp == 2:
  print("You win!")
elif comp == 0 and user == 2:
  print("You lose")
elif comp > user:
  print("You lose")
elif user > comp:
  print("You win!")
elif comp == user:
  print("It's a draw")