from tkinter import *

root = Tk()


photo = PhotoImage(file = 'b.jpg')
theLabel = Label(root,
                 text='早上好',
                  justify = LEFT,
                  image = photo,
                  compound =CENTER,
                  font = ('微软雅黑',20),
                 )
theLabel.pack(side=RIGHT)

mainloop()
    
