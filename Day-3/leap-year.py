year = int(input("Enter your year\n"))

if(year%4==0):
    if(year%100!=0):
        print("Year is a leap year.")
    elif(year%100==0 and year%400==0):
        print("Year is a leap year.")
    else:
        print("Year is not leap year.")
else:
    print("Year is not a leap year.")

        