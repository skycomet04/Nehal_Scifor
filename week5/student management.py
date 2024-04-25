class student:
    def __init__(self,name,age,percentage,dob,id):
        self.name=name
        self.age=age
        self.per=percentage
        self.dob=dob
        self.roll=id
    def accept(self,name,age,percentage,dob,roll):
        st=student(name,age,percentage,dob,roll)
        stu.append(st)
    def display(self,st):
        print(f"Student details are\nName {st.name}\nAge {st.age}\nPercentage {st.per}\nDate of Birth {st.dob}\nRoll No. {st.roll}")
    def search(self,item):
        for i in range(0,len(stu)):
            if stu[i].roll==item:
                return i      
    def delete_details(self,item):
        ind=obj.search(item)
        del(stu[ind])
    def update(self,item,edit):
        if edit=="name":
            ind=obj.search(item)
            s=stu[ind]
            s.name=input("Enter student edited name ")
        elif edit=="age":
            ind=obj.search(item)
            s=stu[ind]
            s.age=int(input("Enter student  age "))
        elif edit=="dob":
            ind=obj.search(item)
            s=stu[ind]
            s.dob=input("Enter student dob ")
        elif edit=="percentage":
            ind=obj.search(item)
            stu[ind].percentage=float(input("Enter student percentage "))
unique=100
stu=[]
obj=student("",0,0,"",1)
while True:
    print("choose the operation to be performed\n1:Add student\n2:Display Student Details\n3:Search details of a student\n4:delete student\n5:update student detail\n6:Exit")
    user=int(input("Enter your choice "))
    if user==1:
        a=input("Enter student name ")
        b=int(input("Enter student age "))
        c=float(input("Enter student percentage "))
        d=input("Enter student Date of Birth ")
        obj.accept(a,b,c,d,unique)
        unique+=1
    elif user==2:
        for i in range(len(stu)):
            obj.display(stu[i])
    elif user==3:
        inp=int(input("Enter student Roll No "))
        index=obj.search(inp)
        obj.display(stu[index]) 
    elif user==4:
        item=int(input("Enter student roll no whose details to be deleted "))
        obj.delete_details(item)
    elif user==5:
        item=int(input("Enter student roll no whose details to be updated "))
        what=input("Enter what you want to update\nName\nAge\ndob\nPercentage\n")
        obj.update(item,what)
    elif user==6:
        break

