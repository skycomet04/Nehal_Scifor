# 1 convert odd number into even in a list
number_list=list(map(int, input("Enter natural nos separated by space ").split()))
if len(number_list)!=0:
  for i in range(0,len(number_list)):
    if number_list[i]%2!=0:
      number_list[i]=number_list[i]+1
  print(number_list)

  # 2 swap first element with last element
number_list=list(map(int, input("Enter natural nos separated by space ").split()))
temp=number_list[0]
number_list[0]=number_list[-1]
number_list[-1]=temp
print(number_list)

# 3 take user input and add in the list
n=int(input("Enter length of the list "))
num_list=[]
for i in range(0,n):
  num_list.append(int(input(f"Enter the {i+1} number ")))
print(num_list)

# 4 Employee list
emp_list=["Jack","Jacob", "Crystal","Kylie","Chuck","Andre"]
print("enter 1 : Add new employee")
print("Enter 2 : Add employee at particular index")
print("Enter 3 : Delete particular employee if resigned")
print("Enter 4 : Delete new employees list ")
print("Enter 5 : Correct employee name")
print("Enter 0 : Exit")
while True:
  choice=int(input("Enter the number of the operation to be performed "))
  if choice ==1:
    emp_list.append(input("Enter name of the new employee to be added "))
  elif choice==2:
    length=len(emp_list)
    index=int(input(f"Enter the index at which you want to add no and no should be less than or equal to length {length} "))
    emp_list.insert(index-1,input("Enter the employee name "))
  elif choice==3:
    emp_list.remove(input("Enter the employee name to be removed "))
  elif choice==4:
    emp_list.clear()
  elif choice ==5:
    name=input("Enter the name to be corrected ")
    correct_name= input("Enter the correct name ")
    index=emp_list.index(name)
    emp_list[index]=correct_name
  elif choice==0:
    break
  else:
    print("Enter valid option no")
print(emp_list)

