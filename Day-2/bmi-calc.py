height = float(input("Enter Your height in meters\n"))
weight = float(input("Enter your weight in kgs\n"))

bmi = float(round((weight)/(height**2),2))

if(bmi<18.5):
    print("Your BMI is: " + str(bmi)+"," + " And your are underweight")
elif(bmi>18.5 and bmi < 25):
    print("Your BMI is: " + str(bmi)+"," + " And your are Normal weight")
elif(bmi>25 and bmi < 30):
    print("Your BMI is: " + str(bmi)+"," + " And your are Over weight")
elif(bmi>30 and bmi < 35):
    print("Your BMI is: " + str(bmi)+"," + " And your are Obese")
else:
    print("Your BMI is: " + str(bmi)+"," + " And your are Clinically Obese")