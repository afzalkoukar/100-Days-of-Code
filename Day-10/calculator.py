import os
import sys
from art import logo

def cls():
    os.system('cls')
print(logo)

def add (a, b):
    return (a+b)

def sub (a, b):
    return (a-b)

def divide(a,b):
    return (a/b)

def multiply(a, b):
    return (a * b)

def calculator():
    calculate = True

    operations = {
    "+": add,
    "-": sub,
    "*": multiply,
    "/": divide
    }

    Num1 = float(input("Enter the first number: \n"))

    for key in operations:
        print(key)

    while(calculate):
        symbol = input("Pick an operation: ")

        Num2 = float(input("Enter Second number: \n"))

        operator = operations[symbol]

        answer = operator(Num1, Num2)

        print(f"{Num1} {symbol}  {Num2} = {answer}")
        
        choice = input(f"Do you want to calculate more with {answer}. Y for Yes and N for No and exit to exit the program \n")

        if(choice == "Y" or choice == "Yes" or choice == "y"):
            Num1 = answer
        elif (choice == "N" or choice == "No" or choice == "n"):
            calculate = False
            cls()
            calculator()
        elif (choice == "exit"):
            sys.exit(0)

calculator()