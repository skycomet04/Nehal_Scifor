import requests,json
from tkinter import *
import datetime
    
win=Tk()
win.title("Currency Converter")
win.geometry("1700x1500")
f1=Frame(win)
f1.place(x=0,y=0,height=290,width=1700)
currency=['ALL','AFN','ARS','AWG','AUD','AZN','BSD','BBD','BYN','BZD ','BMD','BOB','BAM','BWP','BGN','BND','KHR','CAD','KYD','CLP','CNY','COP','CRC','HRK','CUP','CZK','DKK','DOP','XCD','EGP', 'SVC','EUR','FKP','FJD','GHS','GIP','GTQ','GBP', 'GYD','HNL','HKD','HUF','ISK','INR','USD']
def convert_amt():
    r=requests.get("https://api.freecurrencyapi.com/v1/latest?apikey=Yu1xQYaDpHMAhD4oaOuhiS5eWXYj8uPRinVVrlni")
    if r.status_code==200:
        data=r.text
        parse=json.loads(data)
        cur=parse.get('data')
        rate2=cur.get(convert.get())
        rate1=cur[option.get()]
        print(rate1,rate2)
        a=round((amount.get()/rate1)*rate2,5)
        conamount.set(a)
        s=f"{str(amount.get())} {option.get()} Equals {str(a)} {convert.get()} \n"
        t1.insert(END,s)
# ct stores current time
        ct = datetime.datetime.now()
        time=f"Last time update--- {ct}\n "
        t1.insert(END,time)
    else:
        print("Some issue is there")

def clear():
    global f1,t1
    amount.set("0")
    conamount.set("0.0")
    t1.delete('1.0',"end")
    
amount=IntVar()
conamount=DoubleVar()
option=StringVar()
option.set("USD")
convert=StringVar()
convert.set("INR")

Label(f1,text="Currency converter using Python",fg="#a695f8",font=("impact",28)).place(x=500,y=10,height=50)
Label(f1,text="Amount",font=("serif",22)).place(x=100,y=80,height=40)
e1=Entry(f1,textvariable=amount,font=("serif",16))
e1.place(x=100,y=130,height=40,width=400)
e2=Entry(f1,textvariable=conamount,font=("serif",16))
e2.place(x=100,y=200,height=40,width=400)
d1=OptionMenu(f1,option,*currency)
d1.place(x=750,y=130,height=50,width=400)
d2=OptionMenu(f1,convert,*currency)
d2.place(x=750,y=190,height=50,width=400)
b1=Button(win,text="Convert",bg="#6a9ed2",command=convert_amt)
b1.place(x=100,y=300,height=50,width=150)
b2=Button(win,text="Clear",bg="#6a9ed2",command=clear)
b2.place(x=100,y=380,width=120,height=50)
t1=Text(win)
t1.place(x=300,y=300,width=1100)
win.mainloop()
