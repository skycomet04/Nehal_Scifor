# prime no
number=int(input("Enter a number "))
mid=number//2
bool=True
for i in range(2,mid+1):
  if number%i==0:
    print("It is not a prime number")
    bool=False
    break
if bool==True:
  print("it is a prime number")

# even no
for i in range(0,101):
  if i%2==0:
    print(i)

# quiz program
print("hello  this is a quiz .In the quiz we are going to ask 5 ques" )
count=0
print("what is the cube of 12?")
ans=int(input())
if ans==1728:
  count+=1
print("What is the capital of Austraila?")
ans=input()
if ans.lower()=="canberra":
  count+=1
print("What is 1048+1022?")
ans=int(input())
if ans==2100:
  count+=1
print("What is the name of current Prime Minister of India ?")
ans=input()
if ans.lower()=="narendra modi":
  count+=1
print("Which river is the longest river?")
ans=input()
if ans.capitalize()=="Nile":
  count+=1
target=count*10
print(f"your total score is {target}")
print(f"Correct answers are {count} and wrong answers are{5-count}")
