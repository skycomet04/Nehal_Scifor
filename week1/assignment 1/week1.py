#ques 7
print("1 : addition\n2 : Subtraction\n3 : Multiplication\n4 : Divison")
a,b=map(int, input("Enter any two integer no").split())
choice=input("Enter a no from 1,2,3,4 for arithmetical operation you want to perform ")
if choice=="1":
  c=a+b
  print(f"The sum of {a} and {b} is {c}")
elif choice=="2":
  c=a-b
  print(f"Subtraction of {a} and {b} is {c}")
elif choice=="3":
  c=a*b
  print(f"multiplication of {a} and {b} is {c}")
elif choice=="4":
  c=a/b
  print(f"Division of {a} and {b} is {c}")
else:
  print("Enter correct choice")

#ques 8
byear=int(input("enter your birth year to calculate your age "))
age=2024-byear
print(f"your age is {age}")

#ques 6
books=input("Enter the no of books to buy ")
amount=books*2
print("Amount to be paid is $",amount)

#ques 5
print("Hello, I am a chatbot. What's your name?")
name=input()
print(f"okay {name} in which grade you are right now?")
grade=input()
print(f"So {name} you are in {grade}th grade. Do you have any hobby? Yes or no")
ans=input()
print(f"{name}, What is it")
hobby=input()
print(f"That's nice {name} .Can I ask you one question ? yes or no?")
choice=input()
if choice=="yes":
  print("Tell me 1098-98 =?")
  answer=int(input())
  if answer==1000:
    print("Good your answer is correct ")
  else:
    print("Oops, your answer is incorrect. 1000 is the right answer")
  print("Can I ask you one General Knowledge question ? yes or no?")
  a=input()
  if a=="yes":
    print("Tell me what is your national animal name?")
    animal=input()
    if animal=="tiger":
      print(f"Well done! {animal} is correct answer.It was nice talking you.\n Have a good day!!.Byee")
    else:
      print("Oh no, that's not the correct answer.")
  else:
    print("That's ok.Byee")
  print("It was nice talking you.\n Have a good day!!.Byee")
else:
  print(f"No problem {name}.It was nice talking to you.Byee")

  #ques 4
name=input("Enter Your name ")
age=int(input("Enter your Age "))
standard=input("which class you study in ")
color=input("Enter your favourite color ")
ad=input("Enter your address ")
interest=input("Enter your one interest ")
print(f"I am {name}.I am {age} years old. I study in {standard} class. {color} is my favourite color. My residence address is {ad}. My interest \nis {interest}. ")

# ques 3
print("Mamta\nAnanya\nHardik\nGarvesh\nHarsh")

# ques 2
for i in range(0,10):
  print("- "*10)

# ques 1
print("Arvind")
print("Name: Nehal and Age: 24")