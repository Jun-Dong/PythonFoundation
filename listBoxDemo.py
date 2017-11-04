from tkinter import *

root = Tk()
#添加滚动条
sb = Scrollbar(root)
sb.pack(side = RIGHT,fill = Y)

#创建一个空列表
theLB = Listbox(root,yscrollcommand = sb.set)

#往列表里添加数据
for item in range(110):
    theLB.insert(END,item)
theLB.pack(side = LEFT,fill = BOTH)
sb.config(command = theLB.yview)

theButton = Button(root,text = '删除',command = lambda x=theLB: x.delete(ACTIVE))
theButton.pack()

mainloop()
