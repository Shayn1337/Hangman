from tkinter import *
import tkinter as tk

def peter():
    print(var.get())
    var.set(var.get() + "Peter")

def heinz():
    var.set("Heinz")

root = tk.Tk()
root.title("Hangman")

var = StringVar()
label = Label( root, textvariable=var, relief=RAISED )

var.set("Hey!? How are you doing?")
label.pack()

button2 = tk.Button(root, text='Peter', width=100, command= peter)
button2.pack()

button3 = tk.Button(root, text='Heinz', width=100, command= heinz)
button3.pack()

button = tk.Button(root, text='Stop', width=100, command=root.destroy)
button.pack()
root.mainloop()


#gpüssel:
"""
   def __init__ (menu, master):

        menu.frame =Frame(master)
        menu.frame.pack()

        #inhalt menu

        menu.start_game = Button(menu.frame, text="Spiel Starten", command=lambda:menu.game_frame(master))
        menu.start_game.pack(side=LEFT)
        menu.option = Button(menu.frame, text="Optionen", command=lambda:menu.option_frame(master))
        menu.option.pack(side=LEFT)
        menu.button= Button(menu.frame, text="Schliessen", command=menu.frame.quit)
        menu.button.pack()

    def game_frame (menu, master):

        menu.frame.pack_forget()
        game=Frame(master)
        game.pack()
        menu.dummy = Button(game, text="Hi")
        menu.dummy.pack()
        menu.button= Button(game, text="Schliessen", command=menu.frame.quit)
        menu.button.pack()

    def option_frame (menu, master):
        menu.frame.pack_forget()
        option=Frame(master)
        option.pack()
        menu.button= Button(option, text="Zurück", command=lambda:option.game_frame(master))
        menu.button.pack()

"""