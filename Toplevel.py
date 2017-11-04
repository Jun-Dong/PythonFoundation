from tkinter import *

root = Tk()
def create():
    top = Toplevel()
    top.title('FishC Demo')
    top.attributes('-alpha',0.5)
    msg = Message(top,text = 'I love FishC,com')
    msg.pack()

Button(root,text = '创建顶级窗口',command=create).pack()

mainloop()
