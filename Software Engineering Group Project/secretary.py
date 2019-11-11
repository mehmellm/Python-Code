from tkinter import *
from addbowler import AddBowlerWindow
import pymysql
from tkinter.messagebox import showinfo



class SecretaryWindow(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)               
        self.master = master
        self.bowlerNameEntry = None
        self.teamNameEntry = None
        self.birthdayEntry = None
        self.addressEntry = None
        self.phoneNumberEntry = None
        self.handEntry = None
        self.usbcEntry = None
        self.init_window()

    def init_window(self):
        self.master.title("Secretary Page")
        self.pack(fill=BOTH, expand=1) 
        infolabel_coordinates = SecretaryWindow.format_coordinates("170, 83")
        self.setup_infolabel("Welcome to CSC395 Group 3 bowling interface. This is the secretary page.", infolabel_coordinates)
        add_bowler_button_coordinates = SecretaryWindow.format_coordinates("356, 155")
        self.setup_add_bowler_button("Add bowler", add_bowler_button_coordinates)

        

    def setup_infolabel(self, txt, coordinates):
        infoLabel = Label(self, text=txt)
        infoLabel.place(x=coordinates[0], y=coordinates[1])

    def setup_add_bowler_button(self, txt, coordinates):
        addBowlerButton = Button(self, text=txt, command=self.create_add_bowler_button)
        addBowlerButton.place(x=coordinates[0], y=coordinates[1])

    def create_add_bowler_button(self):
        addbowler_root = Tk()
        addbowler_root.geometry("800x800")
        addbowler_root.title("Add Bowler")
        addbowler_root.maxsize(width=800, height=800)
        addbowler_root.resizable(False, False)
        addbowler_app = Frame(addbowler_root)
        addbowler_app.pack(fill=BOTH, expand=1)
        bowlernamelabel_coordinates = SecretaryWindow.format_coordinates("180, 133")
        self.setup_bowlernamelabel("Add bowler name", bowlernamelabel_coordinates, addbowler_app)
        bowlernameentry_coordinates = SecretaryWindow.format_coordinates("311, 133")
        self.setup_bowlernameentry(bowlernameentry_coordinates, addbowler_app)
        addbowler_app.bind("<Button-1>", SecretaryWindow.show_dynamic_coordinates)
        teamnamelabel_coordinates = AddBowlerWindow.format_coordinates("180, 207")
        self.setup_teamnamelabel("Add team name", teamnamelabel_coordinates, addbowler_app)
        teamnameentry_coordinates = AddBowlerWindow.format_coordinates("311, 207")
        self.setup_teamnameentry(teamnameentry_coordinates, addbowler_app)
        #birthday
        birthdaylabel_coordinates = AddBowlerWindow.format_coordinates("180, 267")
        self.setup_birthdaylabel("Add birthday", birthdaylabel_coordinates, addbowler_app)
        birthdayentry_coordinates = AddBowlerWindow.format_coordinates("311, 267")
        self.setup_birthdayentry(birthdayentry_coordinates, addbowler_app)
        #address
        addresslabel_coordinates = AddBowlerWindow.format_coordinates("180, 336")
        self.setup_addresslabel("Add address", addresslabel_coordinates, addbowler_app)
        addressentry_coordinates = AddBowlerWindow.format_coordinates("311, 336")
        self.setup_addressentry(addressentry_coordinates, addbowler_app)
        #phone number
        phonenumberlabel_coordinates = AddBowlerWindow.format_coordinates("180, 395")
        self.setup_phonenumberlabel("Add phone number", phonenumberlabel_coordinates, addbowler_app)
        phonenumber_coordinates = AddBowlerWindow.format_coordinates("311, 395")
        self.setup_phonenumberentry(phonenumber_coordinates, addbowler_app)
        #which hand they use to bowl
        handlabel_coordinates = AddBowlerWindow.format_coordinates("180, 456")
        self.setup_handlabel("Add player hand", handlabel_coordinates, addbowler_app)
        hand_coordinates = AddBowlerWindow.format_coordinates("311, 456")
        self.setup_handentry(hand_coordinates, addbowler_app)
        #usbc number
        usbc_coordinates = AddBowlerWindow.format_coordinates("180, 524")
        self.setup_usbclabel("Add player usbc number", usbc_coordinates, addbowler_app)
        usbc_coordinates = AddBowlerWindow.format_coordinates("336, 524")
        self.setup_usbcentry(usbc_coordinates, addbowler_app)
        #submit button
        submit_coordinates = AddBowlerWindow.format_coordinates("180, 603")
        self.setup_submitbtn("Submit", submit_coordinates, addbowler_app)
        addbowler_root.mainloop()
                                     
    def setup_bowlernamelabel(self,txt,coordinates,frame):
        bowlerNameLabel = Label(frame, text=txt)
        bowlerNameLabel.place(x=coordinates[0], y=coordinates[1])

    def setup_bowlernameentry(self, coordinates, frame):
        self.bowlerNameEntry = Entry(frame)
        self.bowlerNameEntry.place(x=coordinates[0], y=coordinates[1])

    def setup_teamnamelabel(self,txt,coordinates,frame):
        teamNameLabel = Label(frame, text=txt)
        teamNameLabel.place(x=coordinates[0], y=coordinates[1])

    def setup_teamnameentry(self, coordinates, frame):
        self.teamNameEntry = Entry(frame)
        self.teamNameEntry.place(x=coordinates[0], y=coordinates[1])


    #birthday
    def setup_birthdaylabel(self,txt,coordinates, frame):
        birthdayLabel = Label(frame, text=txt)
        birthdayLabel.place(x=coordinates[0], y=coordinates[1])

    def setup_birthdayentry(self, coordinates, frame):
        self.birthdayEntry = Entry(frame)
        self.birthdayEntry.place(x=coordinates[0], y=coordinates[1])

    #address
    def setup_addresslabel(self,txt,coordinates, frame):
        addressLabel = Label(frame, text=txt)
        addressLabel.place(x=coordinates[0], y=coordinates[1])

    def setup_addressentry(self, coordinates, frame):
        self.addressEntry = Entry(frame)
        self.addressEntry.place(x=coordinates[0], y=coordinates[1])


    #phone number
    def setup_phonenumberlabel(self,txt,coordinates, frame):
        phonenumberLabel = Label(frame, text=txt)
        phonenumberLabel.place(x=coordinates[0], y=coordinates[1])

    def setup_phonenumberentry(self, coordinates, frame):
        self.phoneNumberEntry = Entry(frame)
        self.phoneNumberEntry.place(x=coordinates[0], y=coordinates[1])


    #which hand they use to bowl
    def setup_handlabel(self,txt,coordinates, frame):
        handLabel = Label(frame, text=txt)
        handLabel.place(x=coordinates[0], y=coordinates[1])

    def setup_handentry(self, coordinates, frame):
        self.handEntry = Entry(frame)
        self.handEntry.place(x=coordinates[0], y=coordinates[1])



     #usbc number
    def setup_usbclabel(self,txt,coordinates, frame):
        usbcLabel = Label(frame, text=txt)
        usbcLabel.place(x=coordinates[0], y=coordinates[1])

    def setup_usbcentry(self, coordinates, frame):
        self.usbcEntry = Entry(frame)
        self.usbcEntry.place(x=coordinates[0], y=coordinates[1])

    #submit button
    def setup_submitbtn(self, txt, coordinates, frame):
        submitButton = Button(frame, text=txt, command=self.submit)
        submitButton.place(x=coordinates[0], y=coordinates[1])

    def submit(self):
        bowlerName = self.get_text(self.bowlerNameEntry)
        teamName = self.get_text(self.teamNameEntry)
        self.insert_into_team_name(teamName)
        teamid = self.get_teamid(teamName)
        birthDay = self.get_text(self.birthdayEntry)
        address = self.get_text(self.addressEntry)
        phoneNumber = self.get_text(self.phoneNumberEntry)
        hand = self.get_text(self.handEntry)
        bid = self.get_text(self.usbcEntry)
        teamid = self.get_teamid(teamName)
        all_entries = [bowlerName,teamName,birthDay,address,phoneNumber,hand,bid]
        mydb = pymysql.connect(host="brahe.canisius.edu", port=3306, user="neppallv", passwd="snake609", db="neppallv_software")
        mycursor = mydb.cursor()
        sql = "INSERT INTO bowler (bowlerName, teamName, birthDay, address, phoneNumber,hand, bid) VALUES (%s, %s,%s, %s,%s, %s,%s)"
        values = (bowlerName,teamName,birthDay,address,phoneNumber,hand,bid)
        mycursor.execute(sql, values)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")

    def get_text(self, txtbox):
        return str(txtbox.get())

    def get_teamid(self, name):
        try:
            mydb = pymysql.connect(host="brahe.canisius.edu", port=3306, user="neppallv", passwd="snake609", db="neppallv_software")
            mycursor = mydb.cursor()
            sql = "SELECT tid FROM team WHERE teamName = %s" % (name)
            mycursor.execute(sql)
            mydb.commit()
            retid = mycursor.fetchone()
            retid  = int(retid)
            return retid
        except:
            return 0

    def insert_into_team_name(self, name):
        #try:
            mydb = pymysql.connect(host="brahe.canisius.edu", port=3306, user="neppallv", passwd="snake609", db="neppallv_software")
            mycursor = mydb.cursor()
            select_statement = "SELECT teamName FROM team WHERE teamName = '%s'" % (name)
            mycursor.execute(select_statement)
            mydb.commit()
            retname = mycursor.fetchone()
            if retname:
                return
            sql = "INSERT INTO team (teamName) VALUES (%s)"
            mycursor.execute(sql, name)
            mydb.commit()
        #except:
         #   self.show_error("ERROR")
        
                                     
    def show_dynamic_coordinates(event):
        print("%d, %d" % (event.x, event.y))

    def show_error(self, message):
        '''This function will throw up a window with a custom error message'''
        showinfo(message)
        return

    # Bowler
    def update_bowler_name(self, name):
        '''string'''
        pass

    def position_change(self, pos):
        '''string'''
        pass

    def is_returning(self):
        '''boolean'''
        pass

    def avg(self):
        '''int'''
        pass

    def set_hand(self):
        '''string'''
        pass

    def team_change(self):
        '''string'''
        pass

    def enter_scores(self):
        '''string'''
        pass

    def balance_update(self):
        '''float'''
        pass



    #Team

    def update_team_name(self, new_name):
        '''string'''
        pass

    def update_player(self, command, player_name):
        '''char, string'''
        pass

    def update_rank(self, new_rank):
        '''int'''
        pass

    def update_team_average(self):
        '''int'''
        pass
    

    

    
        

    def format_coordinates(s):
        newl = []
        l = s.strip().split(",")
        for i in l:
            i = i.strip()
            newl.append(int(i))
        return newl
        

        
    
        
