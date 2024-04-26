import requests
import tkinter as t
import json
root=t.Tk()
root.geometry("800x600")
r=requests.get('https://zenquotes.io/api/random')
res=r.text
parse=json.loads(res)
print(parse[0].get('q'))
t.Label(root,text="Random quotes",font=('arial',34),fg="lightpink",bg="lightblue").place(x=0,y=10,height=68,width=800)
if r.status_code==200:
    label=t.Label(root,text=parse[0].get('q'),bg="lightblue")
    label.place(x=0,y=80,height=500,width=800)
else:
    label=t.Label(root,text="")
    label.place(x=50,y=80,height=300,width=600)
print(r.ok)
root.mainloop()