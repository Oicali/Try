from tkinter import *

root = Tk()
root.geometry('300x200')
root.title('Frame')

frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

redbutton = Button(frame, text='Red', fg='red')
redbutton.pack(side=LEFT)