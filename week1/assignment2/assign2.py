#ques 1
no_of_choco=327
no_of_kids=78
remaining_choco=no_of_choco % no_of_kids
print("Chocolates remaining with teacher after equal distribution are ",remaining_choco)

#ques 2
print("Please enter your name")
name=input()
print("Enter your contact no")
contact=input()
print("Enter your age")
age=int(input())
print("Enter your email id")
email=input()
print(f"Hi, {name}!! Thanks for visiting our restaurant and registering for our lucky draw competition on our 25th Anniversary.\nOnce the lucky draw results are announced you will receive a message on your mobile number : {contact} and detailed description of your gift on your email Id : {email}. \nThank you for being a valued customer {name} !!Dominos"
)

#ques 3
total_student=60
person_per_team=4
total_teams=total_student//person_per_team
print(f"{total_teams} teams can be created among students ")

# ques 4
temp_farhen=float(input("Enter temperature in Fahrenheit "))
temp_celsius=((temp_farhen-32)*5)/9
print(f"Temperature in celsius is {temp_celsius:.2f}" )
