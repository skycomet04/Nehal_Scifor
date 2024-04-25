# pan card information
def uppercase(name, pan_no):
  flag=True
  if name.isupper()!=True:
    name=name.upper()
  if pan_no.isupper!=True and  len(pan_no)==10:
    pan_no=pan_no.upper()
  else:
    print("Enter valid input")
    flag=False
  return name, pan_no,flag
pan_no=input("enter your pan number ")
name=input("Enter your Fullname ")
dob=input("Enter your date of birth ")
name1,pan_no,flag=uppercase(name,pan_no)
if flag:
  print(f"Pan Details are as follows\nName = {name1}\nPan Number = {pan_no}\nDOB = {dob}")

# percentage calculation
score=list(map(int, input("Enter five subjects marks out of 100 ").split()))
total=sum(score)
perc=(total/500)*100
print(f"your Percentage is {perc}% ")

#signup
def useraccount(userid,password):
  username=userid
  password=password
  return username,password
while True:
  print("1 : Signup\n2 : login\n0 : Exit")
  user=int(input("Enter which option no to be perform "))
  if user==1:
    userid=input("Enter username ")
    password=input("Password ")
    confirm=input("Confirm Password ")
    if password!=confirm:
      print("password not matching")
      break
    print("Your account is created : D")
    username,password= useraccount(userid,password)
  elif user==2:
    user=input("Enter your username ")
    pas=input("Enter your password ")
    if pas!=password:
      print("Incorrect password. Login failed")
      break
    elif user!=username:
      print("Username not found")
      break
    print("Login successful")
  elif user==0:
    break
  else:
    print("Enter valid option no")

#fibonacci series
print("1: Calculate nth term in fibonacci\n 0:exit")
while True:
  user=int(input("Enter your choice "))
  if user==1:
    n=int(input("Enter the number  "))
    a=0
    b=1
    for i in range(2,n+1):
      c=a+b
      a=b
      b=c
  elif user==0:
    break
  else:
    print("Enter valid no ")
    break
  print(a)

#student file 
import os 
def new_stud():
    stud_name=input("Enter student name ")
    Fname=input("Enter student's father name ")
    Mname=input("Enter student's mother name ")
    contact=int(input("Enter contact no "))
    email=input("Enter student email address ")
    residence=input("Enter student residence address ")
    grade=int(input("Enter student grade "))
    percentage=float(input("Enter percentage obtained "))
    return stud_name,Fname,Mname,contact,email,residence,grade,percentage
print("Choose from the given options\n1 : Creating new file\n2 : New Transaction\n3 : Display student details \n4 : Rename the file\n5 : Delete the student file  ")
user=int(input("Enter your choice "))
if user==1:
    stud=new_stud()
    print(stud)
    f=open(f"C:/Users/ishan/OneDrive/Desktop/python/{stud[0]}.txt","w")
    f.write(f"Student Name - {stud[0]}\nFather's Name - {stud[1]}\nMother's Name - {stud[2]}\nContact - {stud[3]}\nEmail Id - {stud[4]}\nAddress - {stud[5]}\nGrade - {stud[6]}\nPercentage - {stud[7]}")
    f.close()
elif user==2:
    student=input("Enter which student file to be opened ")
    f=open(f"C:/Users/ishan/OneDrive/Desktop/python/{student}.txt","a+")
    f.seek(0)
    data=f.readlines()
    d1=0
    for i in range(len(data)):
        if "Percentage" in data[i]:
            d1=data[i].split("-")
            d1=d1[1]
        if "Grade" in data[i]:
            data[i]=data[i].split("-")
            print(data[i][-1])
            if float(d1)>40.0:  
                g=str(int(data[i][1])+1)
                print(g)
            print(data[i])
    #f.write("Hii")
    f.close()

# story
import random
when =['A few years ago', 'Yesterday', 'Last night', 'A long time ago','On 20th Jan']
who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle','a cat','']
name = ['Ali', 'Miriam','daniel', 'Hoouk', 'Starwalker']
part1=random.choice(when)
part2=random.choice(who)
part3=random.choice(name)
print(f"{part1} {part2} named {part3} used to live in a jungle.\n{} ")

#bricks count
count=0
for i in range(0,6):
  for j in range(0,6):
    for k in range(0,6):
      count+=1
print(f"The nunmber of bricks present in the cubical are {count}")

#count words in file assignment
filename=input("Enter file name which you want to open ")
f=open(f"{filename}.txt","r")
data=f.read()
data=(data.replace(",",""))
data=data.split(" ")
print(f"File contains {len(data)} words in it.")
