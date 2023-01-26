import tkinter as tk
from string import ascii_uppercase

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

class StartPage(tk.Frame):

    def __init__ (self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Hauptmenu").pack()
        tk.Button(self, text="Spiel Starten", command=lambda: master.switch_frame(StartGame)).pack()
        tk.Button(self, text="Optionen", command=lambda: master.switch_frame(Options)).pack()
        tk.Button(self, text="Schliessen", command=self.quit).pack()

class StartGame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Spiel gestartet").pack()
        tk.Button(self, text="Zurück zum Menu", command=lambda: master.switch_frame(StartPage)).pack()

class Options(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='red')
        tk.Label(self, text="Optionen").grid(columnspan=9)
        n=0
        for c in ascii_uppercase:
            tk.Button(self, text=c, font=('Helvetica 18'), width=4).grid(row=1+n//9, column=n%9)
            n+=1
        tk.Button(self, text="Zurück zum Menu", command=lambda: master.switch_frame(StartPage)).grid(columnspan=9)


if __name__ == "__main__":
    app = App()
    app.attributes('-fullscreen',True)
    app.mainloop()