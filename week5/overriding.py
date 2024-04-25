class vehicle:
    def __init__(self,type,price,color,company):
        self.type=type
        self.price=price
        self.color=color
        self.company=company
    def display_info(self):
        print(f"{self.type} Details :\nCompany name : {self.company}\nPrice : {self.price}\nVehicle Color : {self.color}")
class car(vehicle):
    def __init__(self):
        self.type="car"
        self.price=int(input("Enter price "))
        self.color=input("Enter your vehicle color ")
        self.company=input("Enter vehicle company ")
        self.model=input("Enter car model ")
        self.car_type=input("Enter whether its electric or diesel or petrol or CNG ")
        super().__init__(self.type,self.price,self.color,self.company)
    def display(self):
        super().display_info()
class bike(vehicle):
    def __init__(self,price,color,company):
        self.type="bike"
        self.price=price
        self.color=color
        self.company=company
        super().__init__(self.type,self.price,self.color,self.company)
    def display(self):
        super().display_info()

c1=car()
price=int(input("Enter price "))
color=input("Enter your vehicle color ")
company=input("Enter vehicle company ")
b1=bike(price,color,company)
c1.display_info()
b1.display_info()




