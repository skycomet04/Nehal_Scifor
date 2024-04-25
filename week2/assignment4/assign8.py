#ques1
file=open("aboutPython.txt","r")
print(file.read())

#ques2
filename=input("Enter filename to be opened ")
f=open(f"C:/Users/ishan/OneDrive/Desktop/python/{filename}.txt","r")
data=f.readlines()
line=[]
for i in range(0,len(data)):
    for j in range(0,len(data[i])):
        if data[i][j].isdigit():
            line.append(i)
            break
if len(line):
    print(f"Yes the file contain numerical value and they are at line no {line}")
else:
    print("No numerical value found")
f.close()

#ques3
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

#ques4
file=input("Enter file name to be opened ")
f=open(f"C:/Users/ishan/OneDrive/Desktop/python/{file}.txt","r")
data=f.readlines()
sno=1
new_data=[]
for i in data:
    if i!="\n":
        n=list(i)
        temp=n[0]
        n[0]=str(sno)+" "+temp
        n="".join(n)
        print(n)
        new_data.append(n)
        sno+=1
new_data="".join(new_data)
f.close()
f=open(f"C:/Users/ishan/OneDrive/Desktop/python/{file}.txt","w")
f.write(new_data)
f.close()

#ques5
correct=input("Enter the correct word ")
incorrect=input("Enter the incorrect word ")
filename=input("Enter the file name in which changes to be made ")
f=open(f"C:/Users/ishan/OneDrive/Desktop/python/{filename}.txt",'r')
data=f.read()
f.close()
file=open(f"C:/Users/ishan/OneDrive/Desktop/python/{filename}.txt","w")
change_data=data.replace(incorrect,correct)
file.write(change_data)
file.close()

#ques6
filename=input("Enter file name to be opened ")
file=open(f"C:/Users/ishan/OneDrive/Desktop/python/{filename}.txt",'r+')
data=file.read()
size=len(data)
data=list(data)
for i in range(0,size):
    if i!=len(data)-2:
        if data[i].isdigit()==True and data[i+1]==".":
            data.insert(i+2,"\n")
data1="".join(data)
file.seek(0)
file.write(data1)
file.close()

#ques7
filename=input("Enter filename to be opened ")
f= open(f"C:/Users/ishan/OneDrive/Desktop/python/{filename}.txt","r+")
data=f.readlines()
change_data=[]
flag=False
for i in range(0,len(data)):
    check=data[i].split(" ")
    data1=[]
    for j in range(0,len(check)-2):
        if check[j]!=check[j+1] :
           data1.append(check[j]) 
           flag=True
    change_data.append(" ".join(data1))
f.seek(0)
f.write("\n".join(change_data))
if flag:
    print("Duplicate data removed ")
f.close()
