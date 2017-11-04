import tkinter as tk


app = tk.Tk()
app.title('FishC Demo')

theLabel = tk.Label(app,text = '我的第一个窗口程序!')
theLabel.pack()#用于自动调节组件的尺寸和位置

app.mainloop()
