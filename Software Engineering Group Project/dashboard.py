from tkinter import *
from secretary import SecretaryWindow
from treasurer import TreasurerWindow

class MainWindow(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)               
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("CSC395 Bowling Project")
        self.pack(fill=BOTH, expand=1)
        quitbtn_coordinates = MainWindow.format_coordinates("396, 449")
        self.setup_quitbutton("Quit", quitbtn_coordinates)
        secretarybtn_coordinates = MainWindow.format_coordinates("341, 238")
        self.setup_secretarybutton("Go To secretary page", secretarybtn_coordinates)
        treasurerbtn_coordinates = MainWindow.format_coordinates("344, 337")
        self.setup_treasurerbutton("Go To treasurer page", treasurerbtn_coordinates)
        infolabel_coordinates = MainWindow.format_coordinates("199, 148")
        self.setup_infolabel("Welcome to CSC395 Group 3 bowling interface. This is the dashboard.", infolabel_coordinates)

        
    def setup_quitbutton(self, txt, coordinates):
        quitButton = Button(self, text=txt, command=self.client_exit)
        quitButton.place(x=coordinates[0], y=coordinates[1])

    def setup_secretarybutton(self, txt, coordinates):
        secretaryButton = Button(self, text=txt, command=self.create_secretary_button)
        secretaryButton.place(x=coordinates[0], y=coordinates[1])

    def setup_treasurerbutton(self, txt, coordinates):
        treasurerButton = Button(self, text=txt, command=self.create_treasurer_button)
        treasurerButton.place(x=coordinates[0], y=coordinates[1])

    def setup_infolabel(self, txt, coordinates):
        infoLabel = Label(self, text=txt)
        infoLabel.place(x=coordinates[0], y=coordinates[1])

    def client_exit(self):
        exit()
        
    def create_secretary_button(self):
        secretary_root = Tk()
        secretary_root.geometry("800x600")
        secretary_root.maxsize(width=800, height=600)
        secretary_root.resizable(False, False)
        secretary_app = SecretaryWindow(secretary_root)
        secretary_app.bind("<Button-1>", MainWindow.show_dynamic_coordinates)
        secretary_root.mainloop()

        
    def create_treasurer_button(self):
        treasurer_root = Tk()
        treasurer_root.geometry("800x600")
        treasurer_root.maxsize(width=800, height=600)
        treasurer_root.resizable(False, False)
        treasurer_app = TreasurerWindow(treasurer_root)
        treasurer_app.bind("<Button-1>", MainWindow.show_dynamic_coordinates)
        treasurer_root.mainloop()

        
    def format_coordinates(s):
        newl = []
        l = s.strip().split(",")
        for i in l:
            i = i.strip()
            newl.append(int(i))
        return newl

    def show_dynamic_coordinates(event):
        print("%d, %d" % (event.x, event.y))




    
root = Tk()
#size of the window
root.geometry("800x600")
root.maxsize(width=800, height=600)
root.resizable(False, False)

app = MainWindow(root)
def print_coords(event):
    print("%d, %d" % (event.x, event.y))
app.bind("<Button-1>", print_coords)
root.mainloop()



