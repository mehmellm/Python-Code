from tkinter import *
import mysql.connector


class AddBowlerWindow(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.bowlerNameEntry = None
        self.teamNameEntry = None
        self.birthdayEntry = None
        self.addressEntry = None
        self.phoneNumberEntry = None
        self.handEntry = None
        self.usbcEntry = None
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Add Bowler")
        self.pack(fill=BOTH, expand=1)
        infolabel_coordinates = AddBowlerWindow.format_coordinates("170, 83")
        self.setup_infolabel("Welcome to CSC395 Group 3 bowling interface. Add bowler here.", infolabel_coordinates)
        #bowler name
        bowlernamelabel_coordinates = AddBowlerWindow.format_coordinates("180, 133")
        self.setup_bowlernamelabel("Add bowler name", bowlernamelabel_coordinates)
        bowlernameentry_coordinates = AddBowlerWindow.format_coordinates("311, 133")
        self.setup_bowlernameentry(bowlernameentry_coordinates)
        #team name
        teamnamelabel_coordinates = AddBowlerWindow.format_coordinates("180, 207")
        self.setup_teamnamelabel("Add team name", teamnamelabel_coordinates)
        teamnameentry_coordinates = AddBowlerWindow.format_coordinates("311, 207")
        self.setup_teamnameentry(teamnameentry_coordinates)
        #birthday
        birthdaylabel_coordinates = AddBowlerWindow.format_coordinates("180, 267")
        self.setup_birthdaylabel("Add birthday", birthdaylabel_coordinates)
        birthdayentry_coordinates = AddBowlerWindow.format_coordinates("311, 267")
        self.setup_birthdayentry(birthdayentry_coordinates)
        #address
        addresslabel_coordinates = AddBowlerWindow.format_coordinates("180, 336")
        self.setup_addresslabel("Add address", addresslabel_coordinates)
        addressentry_coordinates = AddBowlerWindow.format_coordinates("311, 336")
        self.setup_addressentry(addressentry_coordinates)
        #phone number
        phonenumberlabel_coordinates = AddBowlerWindow.format_coordinates("180, 395")
        self.setup_phonenumberlabel("Add phone number", phonenumberlabel_coordinates)
        phonenumber_coordinates = AddBowlerWindow.format_coordinates("311, 395")
        self.setup_phonenumberentry(phonenumber_coordinates)
        #which hand they use to bowl
        handlabel_coordinates = AddBowlerWindow.format_coordinates("180, 456")
        self.setup_handlabel("Add player hand", handlabel_coordinates)
        hand_coordinates = AddBowlerWindow.format_coordinates("311, 456")
        self.setup_handentry(hand_coordinates)
        #usbc number
        usbc_coordinates = AddBowlerWindow.format_coordinates("180, 524")
        self.setup_usbclabel("Add player usbc number", usbc_coordinates)
        usbc_coordinates = AddBowlerWindow.format_coordinates("336, 524")
        self.setup_usbcentry(usbc_coordinates)
        #submit button
        submit_coordinates = AddBowlerWindow.format_coordinates("180, 603")
        self.setup_submitbtn("Submit", submit_coordinates)


        
    def setup_infolabel(self, txt, coordinates):
        infoLabel = Label(self, text=txt)
        infoLabel.place(x=coordinates[0], y=coordinates[1])

    #bowler name
    def setup_bowlernamelabel(self,txt,coordinates):
        bowlerNameLabel = Label(self, text=txt)
        bowlerNameLabel.place(x=coordinates[0], y=coordinates[1])

    def setup_bowlernameentry(self, coordinates):
        self.bowlerNameEntry = Entry(self)
        self.bowlerNameEntry.place(x=coordinates[0], y=coordinates[1])


    #team name
    def setup_teamnamelabel(self,txt,coordinates):
        teamNameLabel = Label(self, text=txt)
        teamNameLabel.place(x=coordinates[0], y=coordinates[1])

    def setup_teamnameentry(self, coordinates):
        self.teamNameEntry = Entry(self)
        self.teamNameEntry.place(x=coordinates[0], y=coordinates[1])



    #birthday
    def setup_birthdaylabel(self,txt,coordinates):
        birthdayLabel = Label(self, text=txt)
        birthdayLabel.place(x=coordinates[0], y=coordinates[1])

    def setup_birthdayentry(self, coordinates):
        self.birthdayEntry = Entry(self)
        self.birthdayEntry.place(x=coordinates[0], y=coordinates[1])


    #address
    def setup_addresslabel(self,txt,coordinates):
        addressLabel = Label(self, text=txt)
        addressLabel.place(x=coordinates[0], y=coordinates[1])

    def setup_addressentry(self, coordinates):
        self.addressEntry = Entry(self)
        self.addressEntry.place(x=coordinates[0], y=coordinates[1])




    #phone number
    def setup_phonenumberlabel(self,txt,coordinates):
        phonenumberLabel = Label(self, text=txt)
        phonenumberLabel.place(x=coordinates[0], y=coordinates[1])

    def setup_phonenumberentry(self, coordinates):
        self.phoneNumberEntry = Entry(self)
        self.phoneNumberEntry.place(x=coordinates[0], y=coordinates[1])



    #which hand they use to bowl
    def setup_handlabel(self,txt,coordinates):
        handLabel = Label(self, text=txt)
        handLabel.place(x=coordinates[0], y=coordinates[1])

    def setup_handentry(self, coordinates):
        self.handEntry = Entry(self)
        self.handEntry.place(x=coordinates[0], y=coordinates[1])



     #usbc number
    def setup_usbclabel(self,txt,coordinates):
        usbcLabel = Label(self, text=txt)
        usbcLabel.place(x=coordinates[0], y=coordinates[1])

    def setup_usbcentry(self, coordinates):
        self.usbcEntry = Entry(self)
        self.usbcEntry.place(x=coordinates[0], y=coordinates[1])

    #submit button
    def setup_submitbtn(self, txt, coordinates):
        submitButton = Button(self, text=txt, command=self.submit)
        submitButton.place(x=coordinates[0], y=coordinates[1])

    def submit(self):
        bowlerName = self.get_text(self.bowlerNameEntry)
        teamName = self.get_text(self.teamNameEntry)
        birthDay = self.get_text(self.birthdayEntry)
        address = self.get_text(self.addressEntry)
        phoneNumber = self.get_text(self.phoneNumberEntry)
        hand = self.get_text(self.handEntry)
        usbc = self.get_text(self.usbcEntry)
        all_entries = [bowlerName,teamName,birthDay,address,phoneNumber,hand,usbc]
        mydb = mysql.connector.connect(host="brahe.canisius.edu",user="neppallv",passwd="Snake609",database="neppallv_software")
        mycursor = mydb.cursor()
        sql = "INSERT INTO bowler (bowlerName, teamName, birthDay, address, phoneNumber,hand,usbc) VALUES (%s, %s,%s, %s,%s, %s,%s)"
        values = (bowlerName,teamName,birthDay,address,phoneNumber,hand,usbc)
        mycursor.execute(sql, values)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
        
    def get_text(self, txtbox):
        return str(txtbox.get())


    def format_coordinates(s):
        newl = []
        l = s.strip().split(",")
        for i in l:
            i = i.strip()
            newl.append(int(i))
        return newl

    def show_dynamic_coordinates(event):
        print("%d, %d" % (event.x, event.y))
