from tkinter import *


#Tkinter总共提供了三种布局组件的方法:pack(),gird()和place()
#gird()允许你用表格的形式来管理组件的位置

root = Tk()
Label(root ,text='作品: ').grid(row=0)
Label(root,text='作者: ').grid(row = 1)
Label(root,text='密码: ').grid(row = 2)
e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root,show ='*')
e1.grid(row = 0,column=1,padx=10,pady=5)
e2.grid(row = 1,column=1,padx=10,pady=5)
e3.grid(row = 2,column=1,padx=10,pady=5)

def show():
    print('作品:《%s》' % e1.get())
    print('作者:%s' % e2.get())
    e1.delete(0,END)
    e2.delete(0,END)

Button(root,text = "获取信息",width=10,command=show)\
                 .grid(row=4,column=0,sticky=W,padx=10,pady=5)


Button(root,text = '退出',width=10,command=root.quit)\
                 .grid(row=4,column=1,sticky=E,padx=10,pady=5)
mainloop()
