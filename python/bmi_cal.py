from datetime import date as d
height=float(input("Enter your height in meter "))
weight=float(input("Enter your weight in kilograms "))
bmi=weight/height**2
date=d.today()
flag=True
f=open("C:/Users/ishan/OneDrive/Desktop/python/bmi.txt","a+")
if bmi >=18.5 and bmi<25:
  f.write(f"\nDate is: {date}\n BMI is: {round(bmi,2)}\n Height is: {height}\n Weight is: {weight}\n category- normal\n ")
elif bmi >=25 and bmi<39.9:
  f.write(f"D\nate is: {date}\n BMI is: {round(bmi,2)}\n Height is: {height}\n Weight is: {weight}\n category - overweight\n ")
elif bmi >=40:
  f.write(f"\nDate is: {date}\n BMI is: {round(bmi,2)}\n Height is: {height}\n Weight is: {weight}\n Category - obese\n ")
elif bmi <= 18.4:
  f.write(f"\nDate is: {date}\n BMI is: {round(bmi,2)}\n Height is: {height}\n Weight is: {weight}\n category - underweight\n ")
else:
  print("Invalid input")
  flag=False
if flag:
  print("Data added successfully in the file")
f.close()