from tkinter import *

root = Tk()
text = Text(root,width=30,height = 10)
text.pack()

#INSERT索引表示插入光标当前的位置
text.insert(INSERT,'I LOVE FishC')
photo = PhotoImage(file = 'b.jpg')

def show():
    text.image_create(END,image = photo)

b1 = Button(text,text='点我',command = show)
text.window_create(INSERT,window = b1)

mainloop()
