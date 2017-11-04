from tkinter import *

root = Tk()
Langs =  [
    ('Python',1),
    ('Java',2),
    ('Ruby',3),
    ]
v = IntVar()
v.set(1)
for lang,num in Langs:
    b = Radiobutton(root,text = lang,variable = v,value = num)
    b.pack(anchor = W)

mainloop()
