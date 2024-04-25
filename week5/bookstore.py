from datetime import date
class book:
    def __init__(self,id,title,price):
        self.id=id
        self.title=title
        self.price=price
        self.date=date.today()
        self.y=date.today().year
        self.purchase=False
    def add(self,id,title,price):
        b=book(id,title,price)
        book_list.append(b)
    def search(self,item,choice):
        for i in range(0,len(book_list)):
            if choice==1:
                if book_list[i].id==int(item):
                    return i
            elif choice==2:
                if book_list[i].title==item:
                    return i
            elif choice==3:
                if book_list[i].price==int(item):
                    return i
    def display(self):
        print(f"Book Id - {self.id}\nBook Title - {self.title}\nBook Price - {self.price}\nBook Date - {self.date}")
    def delete(self,index):
        del(book_list[index])
     
book_list=[]  
b1=book(1,"The Ramayan",120)  
while 1:
    print("1 : Add a book\n2 : Search a Book\n3 : Display all the Books\n4 : Delete Book\n5 : Exit")
    user=int(input("Enter your choice "))
    if user==1:
        a=int(input("Enter book id "))
        b=input("Enter book title ")
        c=int(input("Enter book price "))
        b1.add(a,b,c)
    elif user==2:
        print("how you want to get book\n1:ID\n2:Title\n3:Price")
        choice=int(input("Enter your choice "))
        item=input("Enter item to be searched here ")
        ind=b1.search(item,choice)
        b1.display(book_list[ind])
    elif user==3:
        print("All The BOOKS Details are\n")
        for i in range(0,len(book_list)):
            book_list[i].display()
    elif user==4:
        for i in range(len(book_list)):
            d=book_list[i].y
            if d<=1999:
                b1.delete(i)
    elif user==5:
        break
