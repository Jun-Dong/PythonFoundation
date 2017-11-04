from tkinter import *
import hashlib

root = Tk()
text = Text(root,width = 30,height =5)
text.pack()
text.insert(INSERT,'I love FishC.com!')

#将任何格式的索引号统一为元组(行,列)形式输出
def getIndex(text,index):
    return tuple(map(int,str.split(text.index(index),'.')))

start = 1.0

while True:
    pos = text.search('I',start,stopindex = END)
    if not pos:
        break
    print('找到的位置是:',getIndex(text,pos))
    print(type(pos))
    print(type(text.index(pos)))
    start = pos +'+1c'#将start指向下一个字符


mainloop()
