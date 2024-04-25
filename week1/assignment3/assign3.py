# ques 1 Palindrome
pet_name=input("Enter name to be checked ")
if pet_name[::1]==pet_name[::-1]:
  print("True")
else:
  print("False")

# ques 2 Secret language
word=input("enter the text here ").split()
temp=[]
for s in range(0,len(word)):
  secret=word[s][1::2]+word[s][::2]
  temp.append(secret)
secret_code=" ".join(temp)
print(secret_code)

# assign3 verify mobile number
number=input("Enter your mobile number ")
if len(number)==10 and number.isnumeric()==True:
  if number[0]=='9' or number[0]=='8' or number[0]=='7':
    print("Verfication successful ")
  else:
    print("Verification failed")
