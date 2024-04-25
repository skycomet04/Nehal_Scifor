class patient:
    def add_patient(self,name,disease,doctor_incharge,id):
        self.name=name
        self.disease=disease
        self.doc_incharge=doctor_incharge
        self.id=id
        self.discharge=None
    def  display_record(self):
        print(f"Patient Name : {self.name}\nDisease : {self.disease}\nDoctor Incharge : {self.doc_incharge}")
    def get_record(self,basis,ans):
        if basis.lower()=="id":
            for i in range( len(patient_list)):
                if patient_list[i].id==int(ans):
                    return i
        elif basis.lower()=="name":
            for i in range( len(patient_list)):
                if patient_list[i].name.lower()==ans.lower():
                    return i
        elif basis.lower()=="disease":
            l=[]
            for i in range( len(patient_list)):
                if patient_list[i].disease==ans.capitalize():
                    l.append(i)
                    return l
        elif basis.lower()=="doctor incharge":
            l=[]
            for i in range( len(patient_list)):
                if patient_list[i].doc_incharge==ans.title():
                    l.append(i)
                    return l
    def delete(self,item,type):
            if type.lower()=="id":
                ind=obj.get_record(type,item)
                del(patient_list[ind])
            elif type.lower()=="name":
                ind=obj.get_record(type,item)
                del(patient_list[ind])
    
patient_list=[]
unique=000
obj=patient()
while True:
    print("choose the operation to be performed\n1:Add patient\n2:Display All Patient Details\n3:Search patient \n4:delete patient\n5:Exit")
    user=int(input("Enter your choice "))
    if user==1:
        a=input("Enter patient name ")
        b=input("Enter disease ")
        c=input("Enter Doctor Incharge name ")
        unique+=1
        obj1=patient()
        patient_list.append(obj1)
        obj1.add_patient(a,b,c,unique)
    elif user==2:
        print("All Patients Details are :\n")
        for i in range(len(patient_list)):
            patient_list[i].display_record()
    elif user==3:
        basis=input("Enter how you want to get data searched\nBy name\nBy Id\nBy disease\nBy Doctor Incharge ")
        inp=input("Enter the value of the above choice ")
        index=obj.get_record(basis,inp)
        if len(index)>1:
            for i in range(len(index)):
                patient_list[i].display_record() 
        else:
            patient_list[index[0]].display_record() 
    elif user==4:
        type=input("Enter how you want to get data deleted\nname\nid")
        item=input("Enter patient value who is to be deleted ")
        obj.delete(item,type)
    elif user==5:
        break