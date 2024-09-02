from tkinter import *

from TicTacToe import TTT

class Intro:
    def __init__(self, root2):
        global entry1
        self.root2=root2
        self.root2.geometry("250x200+475+225")
        intro=Frame(self.root2)
        wel=Label(intro, text="Welcome, let's create usernames!")
        wel.pack()
        intro.pack(side=TOP,pady=10)
        frame4=Frame(self.root2)
        p1=Label(frame4, text="Player 1's Name: ")
        p1.pack(side=LEFT)
        entry1=Entry(frame4)
        entry1.pack(side=LEFT)
        frame4.pack(side=TOP, pady=10)
        frame5=Frame(self.root2)
        p2=Label(frame5, text="Player 2's Name: ")
        p2.pack(side=LEFT)
        entry2=Entry(frame5)
        entry2.pack(side=LEFT)
        frame5.pack(side=TOP, pady=10)
        frame6=Frame(self.root2)
        def start():
            TTT().execute()
            self.root2.destroy()
        submit=Button(frame6, text="Submit", command=start)
        submit.pack()
        frame6.pack(side=TOP)
        self.root2.mainloop()
i=Intro(Tk())