from tkinter import *
import os
from tkinter import ttk
def START():
    root.destroy()
    os.system('python hang.py')

def SCORE():
    print('hello')

def OPTIONS():
    print('hello')

def EXIT():
    root.destroy()
root=Tk()

bg=PhotoImage(file='hangmank.png')
pic=Label(root,image=bg)
pic.place(x=0,y=0,relwidth=1,relheight=1)


start=Button(root,text="START GAME",font=("italic",8),width=18,height=2,command=START)
start.place(x=205,y=60)

score=Button(root,text="VIEW SCORE",font=("italic",8),width=18,height=2,command=SCORE)
score.place(x=205,y=110)

options=Button(root,text="OPTIONEN",font=("italic",8),width=18,height=2,command=OPTIONS)
options.place(x=205,y=160)

exit=Button(root,text="EXIT",font=("italic",8),width=18,height=2,command=EXIT)
exit.place(x=205,y=210)

root.geometry('500x400+450+150')
root.title("Menu")
root.mainloop()


