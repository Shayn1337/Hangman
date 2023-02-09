import random
import os

from words import word_list
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from string import ascii_lowercase
from string import ascii_uppercase
root=Tk()
root.title("Hangman")
lis=[]
for x in word_list:
    x=x.upper()
    lis.append(x)


photos=[PhotoImage(file="hang01.png"),PhotoImage(file="hang02.png"),PhotoImage(file="hang03.png"),PhotoImage(file="hang04.png"),PhotoImage(file="hang05.png"),PhotoImage(file="hang06.png"),PhotoImage(file="hang07.png"),PhotoImage(file="hang08.png"),PhotoImage(file="hang09.png"),PhotoImage(file="hang10.png"),PhotoImage(file="hangman0.png"),]
topframe=Frame(root,bd=5,width=770,height=990,relief=RIDGE)
topframe.grid(row=1,column=0)

topframe1=Frame(root,bd=5,width=770,height=990,relief=RIDGE)
topframe1.grid(row=2)
def newGame():
    global space_word
    global no_of_guess
    no_of_guess=0
    img.config(image=photos[0])
    actual_word=random.choice(lis)
    space_word=" ".join(actual_word)
    label_word.set(" ".join("_"*len(actual_word)))

def guess(letter):
    global no_of_guess
    txt=list(space_word)
    guessed=list(label_word.get())
    if space_word.count(letter)>0:
        for c in range(len(txt)):
            if txt[c]==letter:
                guessed[c]=letter
            label_word.set("".join(guessed))
            if label_word.get()==space_word:
                messagebox.showinfo("Game status", "Gratulation es ist Richtig!")
                break

    else:
        no_of_guess+=1
        img.config(image=photos[no_of_guess])
        if no_of_guess==10:
            messagebox.showinfo("Game status"," Schade es ist Falsch!")


def Endgame():
    root.destroy()
    os.system('python mainmenu.py')

img=Label(topframe)
img.grid(row=0,column=0,columnspan=3,padx=10,pady=40)
img.config(image=photos[0])

label_word=StringVar()
l1=Label(topframe,textvariable=label_word,font=("Arial"))
l1.grid(row=0,column=5,columnspan=6,padx=10)


end=Button(topframe,text="Spiel Beenden",font=("Arial",8),bg="white",width=12,height=1,command=Endgame)
end.place(x=200,y=7)

Next=Button(topframe,text="Nächstes Wort",font=("Arial",8),bg="white",width=12,height=1,command= lambda :newGame())
Next.place(x=200,y=50)

i=0
for a in ascii_uppercase:
     b1=Button(topframe1,text=a,command=lambda a=a: guess(a),font=("Arial"),width=4)
     b1.grid(row=1+i//9,column=i%9)
     i=i+1

newGame()
root.geometry("525x450+450+150")
root.mainloop()