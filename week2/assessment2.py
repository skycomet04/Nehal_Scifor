# jumbled word
import random
def jumble():
  global point
  words=["banana","cherry","apple","grapes","custardapple","books","cupboard","orange","pencil"]
  choices=random.choice(words)
  list_choice=" ".join(choices).split(" ")
  random.shuffle(list_choice)
  print(f"{list_choice}")
  ans=input("Enter your answer here ")
  word="".join(list_choice)
  if ans ==choices:
    point+=1
    print("You have given the correct word ")
  else:
    print("Incorrect word")
  print("Do you want to exit ")
  user=input("Enter exit if you want to exit game ")
  return user
print("Welcome to Jumble words\n In this game we will give you a jumbled word and you have to tell what word it could be ")
point=0
count=0
while True:
  user=jumble()
  count+=1
  if user=="exit":
    break
print(f"your total score is {point} out of {count}")

def guess_no(user,comp_no):
  flag=False
  if comp_no==user:
    flag=True
  elif comp_no>user:
    print(f"No is greater than {user}")
  else:
    print(f"No is smaller than {user}")
  return flag
import random
comp_no=random.randint(10,100)
chance=10
i=chance
while i>0:
  user=int(input("Enter a no between range 0-100 "))
  ans=guess_no(user,comp_no)
  if ans==True:
    print(f"you win ")
    break
  i-=1
if ans!=True:
  print("You loose")

# adventure game
def adventure():
  print("If someone is drowning and you know how to swim will you help the person yes/no?")
  ans=input("Enter your answer here ")
  if ans.lower() =="yes":
    print("After saving him, The person offers you some money for saving him. will you take the money yes/no?")
    ans=input("Enter your answer ")
    if ans=="yes":
      print("You are money minded person")
    else:
      print("You are selfless ,good person")
  else:
    print(" if that person offers you money for helping him will you help yes/no")
    ans=input("Enter your answer ")
    if ans.lower()=="yes":
      print("You exploit someone weakness")
    else:
      print("You let the person drown in water")
print("Welcome to adventure game\nIn this game you will be given a situation and you have to yes or no ")
adventure()

# complement and intersection
def intersection_set(a,b):
  intersection=set()
  for i in a:
    if i in b:
      intersection.add(i)
  print(f"Intersection of a and b set is {intersection}")
def complement(a,b):
  comp_set=set()
  a_len=len(a)
  b_len=len(b)
  if a>b:
    for i in a:
      if i not in b:
        comp_set.add(i)
  elif a<b:
     for i in b:
      if i not in a:
        comp_set.add(i)
  else:
     for i in a:
      if i not in b:
        comp_set.add(i)
  print(f"Complement set is {comp_set}")

a={1,2,4,7,88,54}
b= {2,5,7,33,54,13,15}
intersection_set(a,b)
complement(a,b)

# union of set
a={19,34,56,7}
b={1,2,5,19,34,7}
c=set()
for i in a:
  c.add(i)
for i in b:
  c.add(i)
print(c)

# ques 4
n=int(input("Enter total no of questions "))
quesno=[]
for i in range(0,n):
  quesno.append(int(input("Enter question number here ")))
print(f"Selected questions are: {quesno}")
for i in range(0,len(quesno)):
  for j in range(0,len(quesno)-1):
    if quesno[j]>quesno[j+1]:
        quesno[j],quesno[j+1]=quesno[j+1],quesno[j]
print(f"Selected questions in order: {quesno}")
ques=int(input("Enter the question number whose page no you want "))
if ques in quesno:
  page=quesno.index(ques)
  print(f"Solve it on page number {page+1}")
else:
  print( "you don’t have to solve this question.")
# another method of searching without using in built function
for i in range(0,len(quesno)):
  if quesno[i]==ques:
    print(print(f"Solve it on page number {i+1}"))
    break
else:
    print( "you don’t have to solve this question.")

stud_dict={}
sub=["Eng","Maths","Hindi","SST","Science"]
for i in range(0,5):
  name=input("Enter student name ")
  sub_dict={}
  for j in range(0,len(sub)):
    sub_dict[sub[j]]=int(input(f"Enter {sub[j]} marks "))
  stud_dict[name]=sub_dict
print(stud_dict)


