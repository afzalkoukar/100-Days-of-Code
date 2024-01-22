print("Welcome to the tip calculator")
Total = int(input("Enter Your Total Bill\n"))
Nos = int(input("Enter the total number of people\n"))
tip = int(input("Enter the percentage of tip to be paid, Ex - 10, 20, etc \n"))

person = round((Total+(Total/1/tip))/(tip),2)

print("Amount to be paid per person " + str(person))