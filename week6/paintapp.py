from tkinter import *
from tkinter import ttk,colorchooser
class paintapp():
    def __init__(self):
        self.win=Tk()
        self.win.geometry("1500x1000")
        self.win.title("Paint")
        self.tools=Frame(self.win,bg="lightgrey")
        self.tools.place(x=2,y=2,width=1500,height=100)
        self.brush_color='yellow'
        self.canva=Canvas(self.win,bg="white")
        self.canva.place(x=300,y=102,width=800,height=700)
        self.canva.bind("<B1-Motion>",self.draw)
        self.b1=Button(self.tools,text="Pen",bg="lightgrey",fg="black",relief='flat',
    borderwidth=0,font=(15),command=self.pen)
        self.b1.place(x=20,y=20,height=50,width=100)
        self.b2=Button(self.tools,text="Brush",bg="lightgrey",fg="black",relief='flat',
    borderwidth=0,font=(15),command=self.pen)
        self.b2.place(x=200,y=20,height=50,width=100)
        self.b3=Button(self.tools,text="Color",bg="lightgrey",fg="black",relief='flat',
    borderwidth=0,font=(15),command=self.changecolor_brush)
        self.b3.place(x=400,y=20,height=50,width=100)
        self.b4=Button(self.tools,text="Eraser",bg="lightgrey",fg="black",relief='flat',
    borderwidth=0,font=(15),command=self.eraser)
        self.b4.place(x=600,y=20,height=50,width=100)
        self.b5=Button(self.tools,text="Brush/Pen size",bg="lightgrey",fg="black",relief='flat',
    borderwidth=0,font=(15),command=self.pen_brush_resize)
        self.b5.place(x=800,y=20,height=50,width=200)
        self.b6=Button(self.tools,text="Clear",bg="lightgrey",fg="black",relief='flat',
    borderwidth=0,font=(15),command=self.clear)
        self.b6.place(x=1002,y=20,height=50,width=200)
        self.win.mainloop()
    def pen(self):
        self.f=False
        self.brush_width=4
        self.brush_color='black'
        self.canva["cursor"] = "pencil"
    def pen_brush_resize(self):
        self.pen_sizeframe=LabelFrame(self.win,bg="snow",text=" Size",font=(15))
        self.pen_sizeframe.place(x=10,y=102,width=60,height=200)
        self.pen_size=Scale(self.pen_sizeframe,orient="vertical",from_=40,to=1,length=160)
        self.pen_size.grid(row=0,column=1,padx=15)
        self.f=True
    def draw(self,event):
        x1,y1=(event.x-1),(event.y-1)
        x2,y2=(event.x+1),(event.y+1)
        if self.f==True: 
            self.brush_width=self.pen_size.get()
        brush_color = self.brush_color 
        self.canva.create_oval(x1,y1,x2,y2,width=self.brush_width,fill=brush_color,outline=brush_color)
    def eraser(self):
        self.canva["cursor"] = DOTBOX
        self.brush_color="white"
    def clear(self):
        self.canva.delete(ALL)
    def changecolor_brush(self):
        new_color = colorchooser.askcolor(title="Select a Color")
        if new_color[1]:
            self.brush_color = new_color[1]
        else:
            pass
    
paintapp()