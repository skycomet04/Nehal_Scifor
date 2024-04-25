from tkinter import *
win=Tk()
win.geometry("1700x1500")
bengal="The Bengal Tiger is the national animal of both India and Bangladesh. The tiger’s coat is yellow to light orange, with stripes ranging from dark brown to black. The number of tigers has reduced dramatically in the past few years, due to poaching and human-tiger conflict."
Lion="Asiatic Lion aka the Indian Lion or Persian Lion is a lion subspecies that is endangered. It differs from the African lion by less inflated auditory bullae, a larger tail tuft and a less developed mane."
leopard="The snow leopard is a large cat native to the mountain ranges in Central and South Asia. Snow leopards have long, thick fur, and their"
buck="The Blackbuck is an ungulate species of antelope and it is near threatened. The main threat to this species is poaching, predation, habitat destruction, overgrazing, inbreeding and sanctuary visitors"
canvas = Canvas(win,width=1500,height=980)
canvas.pack()
Label(canvas,text="Endangered Animals",bg="#FFEF00",font=("impact",28)).place(x=590,y=10,height=60)
tiger = PhotoImage(file="C:/Users/ishan/OneDrive/Desktop/python/bt.png")
backgroundPic = PhotoImage(file='C:/Users/ishan/OneDrive/Desktop/python/jungle.png')
canvas.create_image(0,0, anchor=NW,image=backgroundPic)
Label(canvas,text="Bengal Tiger",font=("callibre",20),bg="#FFEF00").place(x=220,y=80,height=40)
t1=Text(canvas,font=("serif",16),bg="#FFEF00")
t1.place(x=310,y=140,width=350,height=270)
t1.insert(END,bengal)
canvas1 = Canvas(win, width = 250, height = 200)      
canvas1.place(x=50, y= 140)      
canvas1.create_image(0,0,anchor=NW, image=tiger)
# Asiatic Lion
Label(canvas,text="Asiatic Lion",font=("callibre",20),bg="green yellow").place(x=980,y=80,height=40)
t2=Text(canvas,font=("serif",16),bg="green yellow")
t2.place(x=1050,y=140,width=350,height=270)
t2.insert(END,Lion)
lion = PhotoImage(file="C:/Users/ishan/OneDrive/Desktop/python/lion.png")
canvas2 = Canvas(win, width = 250, height = 200)      
canvas2.place(x=770, y= 140)      
canvas2.create_image(0,0,anchor=NW, image=lion)
# Snow Leopard
Label(canvas,text="Snow Leopard",font=("callibre",20),bg="green yellow").place(x=220,y=480,height=40)
t2=Text(canvas,font=("serif",16),bg="green yellow")
t2.place(x=310,y=540,width=350,height=270)
t2.insert(END,leopard)
sl = PhotoImage(file="C:/Users/ishan/OneDrive/Desktop/python/leopard.png")
canvas3 = Canvas(win, width = 250, height = 200)      
canvas3.place(x=50, y= 540)      
canvas3.create_image(0,0,anchor=NW, image=sl)
# Black Buck
Label(canvas,text="Black Buck",font=("callibre",20),bg="#FFEF00").place(x=980,y=480,height=40)
t2=Text(canvas,font=("serif",16),bg="#FFEF00")
t2.place(x=1050,y=540,width=350,height=270)
t2.insert(END,buck)
bb = PhotoImage(file="C:/Users/ishan/OneDrive/Desktop/python/buck.png")
canvas3 = Canvas(win, width = 250, height = 200)      
canvas3.place(x=770, y= 540)      
canvas3.create_image(0,0,anchor=NW, image=bb)

# Create Frame
win.mainloop()
