from tkinter import *

def callback():
    print(variable.get())
OPTIONS = [
    'number',
    '1',
    '2',
    '3',
    '4'
    ,'5'
    ]
root = Tk()
variable = StringVar()
variable.set(OPTIONS[0])
w = OptionMenu(root,variable,* OPTIONS)
w.pack()
Button(root,text = 'click',command=callback).pack()

mainloop()
