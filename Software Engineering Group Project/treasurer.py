from tkinter import *




class TreasurerWindow(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)               
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Treasurer Page")
        self.pack(fill=BOTH, expand=1)
        quitButton = Button(self, text="Quit")
        quitButton.place(x=0, y=0)
