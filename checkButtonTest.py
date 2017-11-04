from tkinter import *

root = Tk()
GIRLS = ['王昭君','貂蝉','杨雨薇','西施']
v = []
for girl in GIRLS:
    v.append(IntVar())
    c = Checkbutton(root,text=girl,variable = v[-1])
    c.pack(anchor = W)#anchor 用于指定显示位置

mainloop()
