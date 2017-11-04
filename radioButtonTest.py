from tkinter import *

root = Tk()
v =IntVar()
Radiobutton(root,text = '1',variable = v ,value = 1).pack(anchor = W)
Radiobutton(root,text = '2',variable = v ,value = 1).pack(anchor = W)
Radiobutton(root,text = '3',variable = v ,value = 1).pack(anchor = W)
Radiobutton(root,text = '4',variable = v ,value = 1).pack(anchor = W)

mainloop()

