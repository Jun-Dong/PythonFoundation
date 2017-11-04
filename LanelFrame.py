from tkinter import *

root = Tk()
group = LabelFrame(root,text = '最好的脚本语言是?',padx = 5 ,pady = 5)
group.pack(padx = 10,pady = 10)
LANGS = [
       ('Python',1),
       ('Ruby',2),
       ('Lua',3)
    ]
v = IntVar()
v.set(2)
for lang ,num in LANGS:
    b = Radiobutton(group,text = lang,variable = v,value = num)
    b.pack(anchor = W)

mainloop()
