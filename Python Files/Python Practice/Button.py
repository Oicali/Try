from tkinter import *  #Tkinter library

root = Tk()
root.geometry('300x200')
root.title('Button')

b = Button(root, text='Click Me!')
b.pack()

root.mainloop()