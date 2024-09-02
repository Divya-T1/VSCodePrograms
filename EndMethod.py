from tkinter import *
class End:
   root2=Tk()
   root2.geometry("250x200+475+225")
   global frame3
   frame3=Frame(root2)
   quit=Button(frame3, text="Quit", command=stop)
   quit.pack(side=LEFT)
   repeat=Button(frame3, text="Play Again", command=again)
   repeat.pack(side=LEFT)
   frame3.pack(side=BOTTOM)
   root2.mainloop()