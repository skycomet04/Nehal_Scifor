# ques 1
row=int(input("Enter no of rows "))
col=int(input("Enter no of columns "))
print(f"no of desk present in a class is {row*col}")

# ques 2
code=[0,1]
no_of_guest=0
while True:
  auth_code=int(input("Enter your autherisation code "))
  if auth_code==1:
    print("Door Opened\nWelcome to the Party, We Hope you have fun.")
    no_of_guest+=1
  elif auth_code==0:
    print("Access Granted\nDoor Opened")
  else:
    break

# ques 3
min_no,max_no=map(int, input("Enter the starting no and ending no of the range and separate them by space ").split())
for i in range(min_no,max_no+1):
  if i%2!=0:
    print(i,"is an odd number")
  else:
    print(i,"is an even number")

# ques 4
essay=input("Write your essay ")
word_count=essay.count(" ")
if word_count>=250:
  print("Cleared")
else:
  print("Not cleared")

# ques 5
num=int(input("Enter number to be check for prime number "))
mid=num//2
boolean=False
for i in range(2,mid+1):
  if num%i==0:
    print(num,"is not a prime number")
    break
  else:
    boolean=True
if boolean==True:
  print(num,"is a prime number")

# ques 6
com_student={1:"Arun",2:"Bhavesh"}
#print("To add new student ")
new_student={3:"Ram",4:"Rohan"}
com_student.update(new_student)
print("updated list",com_student)
for i in com_student:
  print(f"Message sent to: {i}")

# ques 7
print("Welcome")
print("To add new student record enter 1")
print("To display all student records enter 2")
print("To delete student record enter 3")
print("To correct student details enter 4")
print("To search student name enter 5")
print("To exit enter 0")
student={}
unique_no=1
while True:
  choice=int(input("Enter the operation to be performed "))
  if choice==1:
    name=input("enter student name ")
    age=int(input("Enter student age"))
    grade=input("Enter student class ")
    student_record={"name":name,"age":age,"Class":grade}
    student[unique_no]=student_record
    unique_no+=1
  elif choice==2:
    for i in student:
      print(i,student[i])
  elif choice==3:
    roll=input("Enter student unique no to be deleted ")
    student.pop(roll)
    print("Student deleted ")
  elif choice==4:
    where,correct=input("choose either one name/age/class and enter correct value ").split(",")
    if where=="age":
      student.update({where:int(correct)})
    else:
      student.update({where:correct})
    print("Student detail updated ")
  elif choice==5:
    roll_no=int(input("Enter student unique no "))
    st_name=student.get(roll_no)
    print(f"Student details are {st_name} ")
  elif choice==0:
    break
  else:
    print("Enter valid choice")

# create quiz using function
def quiz(choice):
  correct=0
  if choice=="maths":
    print("What is cube of 10 ")
    ans=int(input("Enter your answer "))
    if ans==1000:
      print("correct answer")
      correct+=1

  elif choice=="science":
    print("What is known as the powerhouse of cell ")
    ans=input("Enter your answer ")
    if ans.lower()=="mitochondria":
      print("correct answer")
      correct+=1
  elif choice=="computer":
    print("Who is know as the father of computer ")
    ans=input("Enter your answer ")
    if ans.lower()=="charles babbage":
      print("correct answer")
      correct+=1
  else:
    print("Enter correct choice")
  return correct
i=1
print("This is a quiz . there will be 5 questions ")
print("For maths question enter maths")
print("For science question enter science")
print("For computer related question enter computer")
c=0
while i<=2:
  choice=input("Enter your choice ")
  ans=quiz(choice)
  c+=ans
  i+=1
print(f"Total correct answer are {c} and incorrect ans are{5-c}\n.score is {c*10}")

