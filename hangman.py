import tkinter as tk
from string import ascii_uppercase
import random

class App(tk.Tk):
    def __init__ (self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

#Startseite
class StartPage(tk.Frame):
    def __init__ (self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Hauptmenu").pack()
        tk.Button(self, text="Spiel Starten", command=lambda: master.switch_frame(StartGame)).pack()
        tk.Button(self, text="Optionen", command=lambda: master.switch_frame(Options)).pack()
        tk.Button(self, text="Schliessen", command=self.quit).pack()

#Spiel Frame
class StartGame(tk.Frame):


    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Spiel gestartet").grid(columnspan=9)
        #hier muss das Spiel rein:

#        def newGame():
#            global word_with_space
#            global length
#            length = 0
        word=[]
        wordlist = open('word_list','r')
        for line in wordlist:
            word.append(line.strip().split(","))
        wordlist.close()


        rndword = random.choice(word)



        #Erstellung Tastatur
        n=0
        for c in ascii_uppercase:
            tk.Button(self, text=c, width=10).grid(row=1+n//9, column=n%9)
            n+=1
        tk.Button(self, text="Neues Spiel", width=10).grid(row=3, column=8)
        tk.Button(self, text="Zurück zum Menu", width=90, command=lambda: master.switch_frame(StartPage)).grid(columnspan=9)
        tk.Button(self, text=rndword, width=90, command=lambda: master.switch_frame(StartGame)).grid(columnspan=9)
#Option Frame
class Options(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='red')
        tk.Label(self, text="Optionen").pack()
        tk.Button(self, text="Zurück zum Menu", command=lambda: master.switch_frame(StartPage)).pack()


if __name__ == "__main__":
    app = App()
    app.attributes('-fullscreen',True)
    app.mainloop()