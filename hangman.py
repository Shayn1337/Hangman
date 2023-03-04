import tkinter as tk
from string import ascii_uppercase
import random
import json
import sys, os

game = 0

if getattr(sys, 'frozen', False):
    bundle_dir = sys._MEIPASS
else:
    bundle_dir = os.path.dirname(os.path.abspath(__file__))
configfile = bundle_dir + "\config"
word_list_d = bundle_dir + "\word_list_d"
word_list_e = bundle_dir + "\word_list_e"

with open(configfile, 'r') as f:
    config = json.load(f)

configvar = ["language","win","loss"]

for f in configvar:
    if f not in config:
        config[f] = 0
with open(configfile, 'w') as f:
    json.dump(config, f)

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
        tk.Button(self, text="Spiel Starten", command=lambda: master.switch_frame(StartGame) ,width='10').pack()
        tk.Button(self, text="Optionen", command=lambda: master.switch_frame(Options) ,width='10').pack()
        tk.Button(self, text="Highscore", command=lambda: master.switch_frame(Highscore), width='10').pack()
        tk.Button(self, text="Schliessen", command=self.quit, width='10').pack()

#Spiel Frame
class StartGame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Spiel gestartet").grid(columnspan=9)
        #hier muss das Spiel rein:

        def generateword():
            global word_with_space
            global length
            global rndword
            global line_word
            global life
            global game
            length = 0
            life = 12
            game = 1

            if config['language'] == 1:
                wordlist=word_list_d
            elif config['language'] == 2:
                wordlist=word_list_e
            else:
                wordlist=word_list_d

            word=[]
            wordlist = open(wordlist,'r')
            for line in wordlist:
                word.append(line.strip().split(","))
            wordlist.close()
            rndword = (random.choice(word))
            rndword = rndword[0]
            line_word = rndword.upper()
            for c in ascii_uppercase:
                line_word = line_word.replace(c, "_")
            line_word = " ".join(line_word)
            rndword = " ".join(rndword)
            LabelLife['text'] = ("verbleibende Leben: {}".format(life))
            Label['text'] = line_word

        def guess(select_letter):
            select_letter = select_letter.lower()
            global rndword
            global line_word
            global life
            global game
            if game == 1:
                if(rndword.lower().count(select_letter) > 0):
                    for x in range(rndword.lower().count(select_letter)):
                        line_word = line_word[:rndword.lower().find(select_letter)] + rndword[rndword.lower().find(select_letter)] + line_word[(rndword.lower().find(select_letter)+1):]
                        rndword = rndword[:rndword.lower().find(select_letter)] + "-" + rndword[(rndword.lower().find(select_letter)+1):]
                    if line_word.count("_") < 1:
                        line_word = ("Glückwunsch das Wort ist richtig: \n {}".format(line_word))
                        config['win'] += 1
                        game = 0
                        with open(configfile, 'w') as f:
                            json.dump(config, f)
                else:
                    life-=1
                    if life < 1 :
                        line_word = "Bitte probier es erneut"
                        config['loss'] += 1
                        game = 0
                        with open(configfile, 'w') as f:
                            json.dump(config, f)
            
        
                LabelLife['text'] = ("verbleibende Leben: {}".format(life))
                Label['text'] = line_word

        Label = tk.Label(self, text="Generiere ein Word!", font=10, width=90)
        LabelLife = tk.Label(self, text="Drücke Neues Spiel um ein Spiel zu starten", font=10, width=90)
        Label.grid(columnspan=9)
        LabelLife.grid(columnspan=9)

        #Erstellung Tastatur
        n=0
        for c in ascii_uppercase:
            tk.Button(self, text=c, width=10, command=lambda c=c: guess(c)).grid(row=3+n//9, column=n%9)
            n+=1
        tk.Button(self, text="Neues Spiel", width=10, command=generateword).grid(row=5, column=8)
        tk.Button(self, text="Zurück zum Menu", width=90, command=lambda: master.switch_frame(StartPage)).grid(columnspan=9)

#Option Frame
class Options(tk.Frame):
    def __init__(self, master):

        def language(number):
            config['language'] = number
            with open(configfile, 'w') as f:
                json.dump(config, f)

        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tk.Label(self, text="Optionen").grid(columnspan=3)
        tk.Label(self, text="Sprache:").grid(row=1, column=1)
        tk.Button(self, text="Deutsch", command=lambda c=1: language(c)).grid(row=1, column=2)
        tk.Button(self, text="Englisch", command=lambda c=2: language(c)).grid(row=1, column=3)
        tk.Button(self, text="Zurück zum Menu", command=lambda: master.switch_frame(StartPage)).grid(row=2, column=1, columnspan=2)
        tk.Button(self, text="Spiel Starten", command=lambda: master.switch_frame(StartGame)).grid(row=2, column=3)

#Highscore Frame
class Highscore(tk.Frame):
    def __init__(self, master):

        if (config['win'] ==0)and(config['loss'] == 0):
            win_loss_rate = 0
        else:      
            win_loss_rate = round((config['win']/(config['win']+config['loss'])),2)
        
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tk.Label(self, text="Highscore", width='20').grid(column=1, columnspan=2, pady=15)
        tk.Label(self, text="Siege", width='10', anchor="w").grid(row=2, column=1)
        tk.Label(self, text=config['win'], width='10').grid(row=2, column=2)
        tk.Label(self, text="Niederlagen", width='10', anchor="w").grid(row=3, column=1)
        tk.Label(self, text=config['loss'], width='10').grid(row=3, column=2)
        tk.Label(self, text="W/L Rate", width='10', anchor="w").grid(row=4, column=1)
        tk.Label(self, text=win_loss_rate, width='10').grid(row=4, column=2)
        tk.Button(self, text="Zurück zum Menu",  width='20', command=lambda: master.switch_frame(StartPage)).grid(row=5, column=1, columnspan=2)

if __name__ == "__main__":
    app = App()
    app.geometry("1000x300")
    app.title("Hangman")
    app.mainloop()