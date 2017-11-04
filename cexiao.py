from tkinter import *

root = Tk()
text = Text(root,width=30,height = 5,autoseparators = False,undo = True,maxundo = 10)
text.pack()

def callback(event):
    text.edit_separator()

text.bind('<Key>',callback)
text.insert(INSERT,'I LOVE FishC')

def show():
    text.edit_undo()

Button(root,text = '撤销',command = show).pack()

mainloop()
