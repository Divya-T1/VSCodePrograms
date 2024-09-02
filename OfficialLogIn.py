from tkinter import *
import csv, sqlite3
from tkinter.font import Font
import LoginPage

class OffLogIn:
    def __init__(self, root):

        global submit
        global back
        global entry1
        global entry2
        global exist
        self.con = sqlite3.connect("LogInData.db")
        self.cur = self.con.cursor()

        global button1
        global frame1
        global text1
        self.root=root
        self.root.title("LogIn")
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
        back=Button(frame3, text="Restart")
        self.addButton()
        self.addButton2()
        submit.grid(row=0, column=0)
        back.grid(row=0, column=1)

        frame3.pack()

        
        frame4=Frame(root, padx=0, pady=0)
        exist=Button(frame4, height=0, width=20, padx=0, pady=10, text="Create Login", state="normal", fg='blue', relief="flat", font=Font(size=10,underline=True))
        self.addButton3()
        exist.pack()

        frame4.pack()

        self.frame5=Frame(root, padx=0, pady=0)

    def click(self):
        index=0
        self.cur.execute("Select username FROM UserPass")
        userRow=self.cur.fetchall()
        errorUser=Label(self.frame5, height=0, width=50, padx=0, pady=10, text="This username does not exist. \nSelect \"Back\" to go back to the create LogIn screen")


        for x in userRow:
            if entry1.get()==x[0]:
                index+=1
                break
        if index==0:
            errorUser.pack()
            self.frame5.pack()

        else:
            print(type(entry1.get()))
            self.cur.execute("SELECT password FROM UserPass WHERE username=?", (entry1.get(),))
            password=self.cur.fetchall()
            print(type(password))
            if password[0][0]==entry2.get():
                if errorUser.winfo_exists()==True:
                    errorUser.destroy()
                sucUser=Label(self.frame5, height=0, width=30, padx=0, pady=10, text="LogIn was successful!")
                sucUser.pack()
                self.frame5.pack()
                newWin=Toplevel()
            else:
                if errorUser.winfo_exists()==True:
                    errorUser.destroy()
                errorUser2=Label(self.frame5, height=0, width=50, padx=0, pady=10, text="This password does not exist. \nSelect \"Back\" to go back to the create LogIn screen")
                errorUser2.pack()
                self.frame5.pack()
            
    
    def restart(self):
        self.root.destroy()
        root=Tk()
        OffLogIn(root)
        root.mainloop()
    
    def click2(self):
        self.root.destroy()
        root=Tk()
        LoginPage.StartPage(root)
        root.mainloop()

    def addButton(self):
        submit.configure(command=self.click)
    
    def addButton2(self):
        back.configure(command=self.restart)

    def addButton3(self):
        exist.configure(command=self.click2)


