from tkinter import *
import datetime
import time
import winsound
from threading import *
def Threading():
    t1=Thread(target=alarm)
    t1.start()

def alarm():
    while True:
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
        time.sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if set_alarm_time==current_time:
            winsound.Beep(700,2000)
root=Tk()
root.geometry("500x500")
root.resizable(0,0)
f=Frame(root,bg="teal")
f.place(x=0,y=0,width=500,height=500)
hour=StringVar()
minute=StringVar()
second=StringVar()
hours = ('00', '01', '02', '03', '04', '05', '06', '07','08', '09', '10', '11', '12', '13', '14', '15','16', '17', '18', '19', '20', '21', '22', '23', '24')
minutes = ('00', '01', '02', '03', '04', '05', '06', '07','08', '09', '10', '11', '12', '13', '14', '15',
'16', '17', '18', '19', '20', '21', '22', '23','24', '25', '26', '27', '28', '29', '30', '31','32', '33', '34', '35', '36', '37', '38', '39',
'40', '41', '42', '43', '44', '45', '46', '47','48', '49', '50', '51', '52', '53', '54', '55','56','57','58','59')
seconds=('00', '01', '02', '03', '04', '05', '06', '07','08', '09', '10', '11', '12', '13', '14', '15',
'16', '17', '18', '19', '20', '21', '22', '23','24', '25', '26', '27', '28', '29', '30', '31','32', '33', '34', '35', '36', '37', '38', '39',
'40', '41', '42', '43', '44', '45', '46', '47','48', '49', '50', '51', '52', '53', '54', '55','56','57','58','59')
l1=Label(f,text="Alarm Clock ",bg="teal",fg="turquoise",font=("Helvetica 35 bold")).place(x=130,y=10,height=100,width=300)
l2=Label(f,text="Set Time",bg="teal",font=("Helvetica 24"),fg="turquoise").place(x=160,y=120,height=40,width=150)
hr=OptionMenu(f,hour,*hours)
hr.place(x=180,y=200)
min=OptionMenu(f,minute,*minutes)
min.place(x=230,y=200)
sec=OptionMenu(f,second,*seconds)
sec.place(x=280,y=200)
hour.set(hours[0])
minute.set(minutes[0])
second.set(seconds[0])
b1=Button(f,text="Set Alarm",bg="blue",fg="turquoise",font=("Helvetica 28"),command=Threading)
b1.place(x=150,y=250,height=70)
root.mainloop()
