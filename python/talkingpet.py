from tkinter import *
root=Tk()
root.geometry("1600x1500")
def mouse_click(event):
    global smile,flag
    flag=False
    round.delete(sad)
    smile=round.create_arc(620,550,720,600,start=0,extent=-190,style="arc",width=2)
def tongue_face(event):
    global sad,flag
    flag=False
    round.delete(sad)
    round.delete(smile)
    sad=round.create_arc(620,500,720,620,start=0,extent=-180,width=2,fill="red")
def sad_face():
    global sad
    round.delete(sad)
    sad=round.create_arc(620,550,720,600,start=0,extent=190,style="arc",width=2)
round=Canvas(root,bg="turquoise")
flag=True
round.place(x=0,y=0,height=1500,width=1600)
round.create_oval(350,100,1000,800,fill="yellow",outline="yellow")
round.create_polygon([410, 270, 430, 50, 530, 150,],fill="yellow")
round.create_polygon([800, 150, 900, 50, 930, 270,],fill="yellow")
round.create_oval(400,750,580,850,fill="yellow",outline="yellow")
round.create_oval(770,750,960,850,fill="yellow",outline="yellow")
round.create_oval(560,300,610,400,fill="white",outline="yellow")
round.create_oval(750,300,800,400,fill="white",outline="yellow")
round.create_oval(578,366,593,381,fill="black")
round.create_oval(768,366,783,381,fill="black")
sad=round.create_arc(620,550,720,550,start=0,extent=-190,style="arc",width=2)
round.bind('<Button-1>', mouse_click)
round.bind('<Double-1>',tongue_face)
if flag==True:
    root.after(5000,sad_face)
root.mainloop()