# ques 1 probablity
fav_outcome=int(input("Enter number of favourable outcomes "))
tot_outcome=int(input("Enter total number of outcomes "))
probablity=round(fav_outcome/tot_outcome, 2)
print(probablity,"is the probablity")

# ques 2 Check age for license
age=int(input("Enter your age "))
if age >=18:
  print("Eligible for next step ")
else:
  if age<0:
    print("Enter valid age")
  else:
    print("Not eligible for next step")


# ques 3 Chatbot
print("Hey, What's your name ")
name=input()
print(f"A very good day to you {name}!!\nHow are you feeling Today {name}? Good/Not good?")
choice=input()
if choice =="Good" or choice=="good":
  print(f"It's really a productive day to do something innovative and you are close to it.Btw how old are you {name}?")
  age=int(input())
  if age>10 and age<=15:
    print(f"Can I ask you a question {name}?yes/no")
    choice=input()
    if choice =="yes":
      print("What's your favourite subject ?")
      subject=input()
      if subject.capitalize()=="Maths or Mathematics":
        print(f"So {name}.Tell me the cube of 11? ")
        ans=int(input("Enter your answer here "))
        if ans== 1331:
          print(f"Hurray!! You have answer correctly.")
          print(f"{name} it was nice chatting to you. Next time will ask you some more interesting questions. byee!!")
        else :
          print(f"Oops, Your answer is incorrect. Correct answer is 1331 ")
          print(f"{name} it was nice chatting to you. Next time will ask you some other interesting questions. byee!!")
      elif subject.capitalize()=="English":
        print(f"So {name}.What is the antonym of Cautious?")
        ans=input("Enter your answer here ")
        if ans== "Careless "or ans=="careless":
          print(f"Hurray!! You have answer correctly.")
          print(f"{name} it was nice chatting to you. Next time will ask you some more interesting questions. byee!!")
        else :
          print(f"Oops, Your answer is incorrect. Correct answer is Careless ")
          print(f"{name} it was nice chatting to you. Next time will ask you some other interesting questions. byee!!")
      elif subject.title()=="Social Science or Social Studies":
        print(f"So {name}.In which continent France is located?")
        ans=input("Enter your answer here ")
        if ans.capitalize()== "Europe":
          print(f"Hurray!! You have answer correctly.")
          print(f"{name} it was nice chatting to you. Next time will ask you some more interesting questions. byee!!")
        else :
          print(f"Oops, Your answer is incorrect. Correct answer is Europe")
          print(f"{name} it was nice chatting to you. Next time will ask you some other interesting questions. byee!!")
      elif subject.capitalize()=="Science":
        print(f"So {name}.What is known as powerhouse of the cell ?")
        ans=input("Enter your answer here ")
        if ans== "Mitochondria or mitochondria":
          print(f"Hurray!! You have answer correctly.")
          print(f"{name} it was nice chatting to you. Next time will ask you some more interesting questions. byee!!")
        else :
          print(f"Oops, Your answer is incorrect. Correct answer is Mitochondria")
          print(f"{name} it was nice chatting to you. Next time will ask you some other interesting questions. byee!!")
      else:
        print("Enter Valid subject")
    else:
          print(f"{name} it was nice chatting to you. Next time will share some interesting facts with you. byee!!Have a good day {name}.")
  else :
      if age>15:
        print(f"Can I ask you a question {name}?yes/no")
        choice=input()
        if choice=='yes':
          print(f"So {name} .What is the capital of Australia ?")
          ans=input("Enter your answer here ")
          if ans.capitalize() =="Canberra":
            print(f"Hurray!! You have answer correctly.")
            print(f"{name} it was nice chatting to you. Next time will ask you some more interesting questions. byee!!")
          else :
            print(f"Oops, Your answer is incorrect. Correct answer is Canberra")
            print(f"{name} it was nice chatting to you. Next time will ask you some other interesting questions. byee!!")
        else:
          print(f"{name} it was nice chatting to you. Next time will share some interesting facts with you. byee!!")
      else:
        print(f"So {name} in which grade are you?")
        grade=input()
        print(f"Do you like cartoons. if Yes write the name of the cartoon else write no")
        cartoon=input()
        if cartoon=="no":
          print(f"{name} it was nice chatting to you. Next time will ask you some more interesting questions. byee!!")
        else :
          print(f"I too like {cartoon}")
          print(f"{name} it was nice chatting to you. Next time will ask you some other interesting questions. byee!!")
else:
  print(f"Let me tell you a joke.How does the ocean say hi? It waves!\nHow was the joke .funny/not funny")
  choice=input()
  if choice=='funny':
    print(f"{name} Can I tell you some more jokes? yes/no")
    choice=input()
    if choice.lower()=="yes":
      print("Why is a football stadium always cold? It has lots of fans!\n What did one math book say to the other? “I’ve got so many problems.\nWhat do you call two bananas on the floor? Slippers\nWhy can’t you ever tell a joke around glass? It could crack up")
      print(f"So {name} how are you feeling now.I hope your are feeling good.It was nice chatting you. Come to me if you ever feel bad. i will tell you more good jokes. Byee!!!")
    else:
      print(f"{name} it was nice chatting to you. Next time will ask you some other interesting questions. byee!!")
  elif choice=="not funny":
    print(f"No issue, next time will come up with more good jokes. Byee{name}!!")

# ques 4 AtM
print("Enter 1 : Withdraw amount")
print("Enter 2 : Deposit cash")
print("Enter 3 : Balance enquiry")
print("Enter 4 : Fast cash")
balance=50000
choice=int(input("Enter your choice "))
if choice==1:
  amount=int(input("Enter amount to be withdrawn "))
  if amount%100!=0:
    print("Enter amount that are multiples of 100 like 100, 200, 1000 as 1 rupees, 2 rupees, 10 rupees, 50 rupees are impossible in ATM")
elif choice==2:
  amount=int(input("Enter amount to be deposited "))
elif choice ==3:
  print(f"Account Balance is {balance}")
elif choice==4:
  print('''select amount to be withdran from the given options \noption1 : 5000\noption2 : 10000\noption3 : 15000\noption4 : 20000\noption5 : 25000\n
  option6 : 30000\noption7 : 35000\noption8 : 40000\noption9 : 45000\noption10 : 50000''')
  choice=int(input("Enter the option no you have selected "))
  if choice==1 :
    print("Amount withdrawn",5000)
  elif choice==2 :
    print("Amount withdrawn",10000)
  elif choice==3 :
    print("Amount withdrawn",15000)
  elif choice==4:
    print("Amount withdrawn",20000)
  elif choice==5:
    print("Amount withdrawn",25000)
  elif choice==6 :
    print("Amount withdrawn",30000)
  elif choice==7 :
    print("Amount withdrawn",35000)
  elif choice==8 :
    print("Amount withdrawn",40000)
  elif choice==9 :
    print("Amount withdrawn",45000)
  elif choice==10 :
    print("Amount withdrawn",50000)
  else:
    print("Either the choice is invalid ")
else:
  print("Enter valid no")

  # ques 5 color input
colors= input("Enter color names and seperate them with comma ")
for color in colors.split(","):
  if color.lower()=="red":
    continue
  else:
    print(color)

# ques 6 simple and compound interest
principal=10000
rate=6
time=30
simple_amount=(principal+(principal*rate*time))/100
compound_amount=principal*((1+rate/100)*time)
difference=compound_amount-simple_amount
print("Difference in their return is",difference)

# ques 7 tax calculation
income=int(input("Enter your income on which tax is need to be calculated "))
tax=0
if income>0 and income<300000:
  tax=round((income*0)/100, 2)
  print("tax amount is ",tax)
elif income>=300000 and income<600000:
  tax=round((income*5)/100, 2)
  print("tax amount is ",tax)
elif income>=600000 and income<900000:
  tax=round((income*10)/100, 2)
  print("tax amount is ",tax)
elif income>=900000 and income<1200000:
  tax=round((income*15)/100, 2)
  print("tax amount is ",tax)
elif income>=1200000 and income<1500000:
  tax=round((income*20)/100, 2)
  print("tax amount is ",tax)
elif income>= 1500000:
  tax=round((income*30)/100, 2)
  print("tax amount is ",tax)
else:
  print("Enter correct input")

  # ques 8 bmi index
height=float(input("Enter your height in meter "))
weight=float(input("Enter your weight in kilograms "))
bmi=weight/height**2
if bmi >=18.5 and bmi<25:
  print("Normal")
elif bmi >=25 and bmi<39.9:
  print("Overweight")
elif bmi >=40:
  print("Obese")
elif bmi <= 18.4:
  print("Underweight")
else:
  print("Invalid input")

# Ques 9 leap year
year=int(input("Enter the year "))
if year%400==0:
  print(year," is a leap year")
elif year % 100!=0 and year%4==0:
  print(year,"is a leap year")
else:
  print(year,"is not a leap year")
