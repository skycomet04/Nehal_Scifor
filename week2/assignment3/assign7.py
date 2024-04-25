# ques 1
def add(a,b):
  return a+b
def subtract(a,b):
  return a-b
def multiply(a,b):
  return a*b
def divide(a,b):
  return a/b if b>0 else 0
a,b=map(int, input("enter two numbers ").split(" "))
ans=add(a,b)
ans1=subtract(a,b)
ans2=multiply(a,b)
ans3=divide(a,b)
print(f"{ans}\n{ans1}\n{ans2}\n{ans3}")

# ques 2
def simple_interest(p,r,t):
  return round((p*r*t)/100,3)
def compound_interest(p,r,t):
   ci=(p*(1+r/100)**t)-p
   return round(ci,3)
print("Enter 1 for simple interest\nEnter 2 for commpound interest\nEnter 3 for both interest ")
choice=int(input("Enter your choice "))
principal=int(input("Enter principal amount "))
rate=int(input("Enter rate of interest "))
time=int(input("Enter time "))
if choice==1:
  print(f"Simple Interest is: {simple_interest(principal,rate,time)}")
elif choice==2:
  print(f"Compound Interest is: {compound_interest(principal,rate,time)}")
elif choice==3:
  print(f"Simple Interest is: {simple_interest(principal,rate,time)}")
  print(f"Compound Interest is: {compound_interest(principal,rate,time)}")
else:
  print("Enter correct choice ")

# ques 3
import math
def check_square(a):
  root=int(math.sqrt(a))
  if root*root==a:
    print("It is a perfect square")
  else:
    print("Not a perfect square")
  return
check_square(int(input()))

#   ques 4
def digit_to_word(string):
  word_dict={"1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine","0":"zero"}
  s=[]
  for i in string:
    if i in word_dict.keys():
      s.append(word_dict.get(i))
    else:
      print("Enter correct number")
      break
  return "-".join(s)
word=input("Enter the number ")
word=list(word)
print(digit_to_word(word))

# ques 5
def branch_one(ts,ss):
  if ss>ts:
    print("Sold stock can't be greater than total stock")
  else:
    available_stock=ts-ss
    print(f"Avaliable stock in branch one is {round(available_stock/ts*100,3)}%")
def branch_two(ts,ss):
  if ss>ts:
    print("Sold stock can't be greater than total stock")
  else:
    available_stock=ts-ss
    print(f"Avaliable stock in branch two is {round(available_stock/ts*100,3)}%")

def branch_three(ts,ss):
  if ss>ts:
    print("Sold stock can't be greater than total stock")
  else:
    available_stock=ts-ss
    print(f"Avaliable stock in branch three is {round(available_stock/ts*100,3)}%")
def branch_four(ts,ss):
  if ss>ts:
    print("Sold stock can't be greater than total stock")
  else:
    available_stock=ts-ss
    print(f"Avaliable stock in branch four is {round(available_stock/ts*100,3)}%")
branch_one(int(input("Enter total stock ")),int(input("Enter sold stock ")))
branch_two(int(input("Enter total stock ")),int(input("Enter sold stock ")))
branch_three(int(input("Enter total stock ")),int(input("Enter sold stock ")))
branch_four(int(input("Enter total stock ")),int(input("Enter sold stock ")))
