from tkinter import *
import csv, sqlite3
from tkinter.font import Font
import OfficialLogIn

class StartPage:
    def __init__(self, root):
        global index
        index=1
        global submit
        global back
        global entry1
        global entry2
        try:
            self.con = sqlite3.connect("LogInData.db")
            self.cur = self.con.cursor()
            self.cur.execute(
            '''CREATE TABLE UserPass (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR(50),
            password VARCHAR(50)
        )
        ''')
        except:
            print("Table created")

        global button1
        global frame1
        global text1
        self.root=root
        self.root.geometry("330x200+465+200")
        frame1=Frame(root, padx=0, pady=0)
        text1=Label(frame1, height=0, width=10, padx=0, pady=10, text="Username")
        text1.grid(row=0, column=0)

        entry1=Entry(frame1)
        entry1.grid(row=0, column=1)


        frame2=Frame(root, padx=0, pady=0)
        text2=Label(frame2, height=0, width=10, padx=0, pady=10, text="Password")
        text2.grid(row=0, column=0)

        entry2=Entry(frame2, show="*")
        entry2.grid(row=0, column=1)

        frame1.pack()
        frame2.pack()

        frame3=Frame(root, padx=0, pady=0)
        submit=Button(frame3, text="Next")
        back=Button(frame3, text="Back")
        self.addButton()
        self.addButton2()
        submit.grid(row=0, column=0)
        back.grid(row=0, column=1)

        frame3.pack()

        
        frame4=Frame(root, padx=0, pady=0)
        self.exist=Button(frame4, height=0, width=20, padx=0, pady=10, text="Already have LogIn", state="normal", fg='blue', relief="flat", font=Font(size=10,underline=True))
        self.addButton3()
        self.exist.pack()

        frame4.pack()

        self.frame5=Frame(root, padx=0, pady=0)

    def click(self):
        index=0
        self.cur.execute("Select username FROM UserPass")
        userRow=self.cur.fetchall()

        for x in userRow:
            if entry1.get()==x[0]:
                index+=1
                errorUser=Label(self.frame5, height=0, width=30, padx=0, pady=10, text="This username already exists")
                errorUser.pack()
                self.frame5.pack()
                break
        if index!=1:
            errorUser=Label(self.frame5, height=0, width=30, padx=0, pady=10, text="LogIn created successfully!")
            errorUser.pack()
            self.frame5.pack()
            
            self.cur.execute(
            '''INSERT INTO UserPass (username, password) 
            VALUES (?, ?)''', (entry1.get(), entry2.get())
            )

            self.con.commit()

            self.root.destroy()
            root=Tk()
            OfficialLogIn.OffLogIn(root)
            root.mainloop()

    def click2(self):
        self.root.destroy()
        root=Tk()
        OfficialLogIn.OffLogIn(root)
        root.mainloop()
    
    def restart(self):
        self.root.destroy()
        root=Tk()
        StartPage(root)
        root.mainloop()
 
    def addButton(self):
        submit.configure(command=self.click)
    
    def addButton2(self):
        back.configure(command=self.restart)
    
    def addButton3(self):
        self.exist.configure(command=self.click2)


