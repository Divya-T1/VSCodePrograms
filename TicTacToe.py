from tkinter import *

list_buttons=list()
num=0
bool=FALSE
bool2=FALSE

class Create:
   def __init__(self, root):
      self.root=root
      self.root.geometry("250x320+400+100")

class TicTacToe:

   '''global list_buttons
   global root
   global label
   root.geometry("250x320+400+100")
   frame1=Frame()
   frame2=Frame()
   frame3=Frame()
   label=Label(frame2, text="Tic Tac Toe!")
   label.pack()
   num=0'''

   '''def stop(self):
      root.destroy()
   def again(self):
      TTT()
   '''

   '''quit=Button(frame3, text="Quit", command=stop)
   again=Button(frame3, text="Play Again", command=again)
   quit.pack(side=LEFT)
   again.pack(side=LEFT)'''

   def click(self, button):
      global num
      global bool2, bool
      if num%2==0:
         label.config(text="Player 1's Turn")
         button.config(text="X", bg="blue", fg="black")
      else:
         label.config(text="Player 2's Turn")
         button.config(text="O", bg="red", fg="black")
      num+=1

      if((list_buttons[0]['text']=="X" and list_buttons[1]['text']=="X" and list_buttons[2]['text']=="X")
         or (list_buttons[0]['text']=="O" and list_buttons[1]['text']=="O" and list_buttons[2]['text']=="O")):
         bool=TRUE
         bool2=TRUE
         list_buttons[0].config(bg="green")
         list_buttons[1].config(bg="green")
         list_buttons[2].config(bg="green")
         if(list_buttons[0]['text']=="X"):
            label.config(text="Player 1 wins!")
         else:
            label.config(text="Player 2 wins!")
         

      elif((list_buttons[3]['text']=="X" and list_buttons[4]['text']=="X" and list_buttons[5]['text']=="X")
         or (list_buttons[3]['text']=="O" and list_buttons[4]['text']=="O" and list_buttons[5]['text']=="O")):
         bool=TRUE
         bool2=TRUE
         list_buttons[3].config(bg="green")
         list_buttons[4].config(bg="green")
         list_buttons[5].config(bg="green")
         if(list_buttons[3]['text']=="X"):
            label.config(text="Player 1 wins!")
         else:
            label.config(text="Player 2 wins!")

      elif((list_buttons[6]['text']=="X" and list_buttons[7]['text']=="X" and list_buttons[8]['text']=="X")
         or (list_buttons[6]['text']=="O" and list_buttons[7]['text']=="O" and list_buttons[8]['text']=="O")):
         bool=TRUE
         bool2=TRUE
         list_buttons[6].config(bg="green")
         list_buttons[7].config(bg="green")
         list_buttons[8].config(bg="green")
         if(list_buttons[6]['text']=="X"):
            label.config(text="Player 1 wins!")
         else:
            label.config(text="Player 2 wins!")

      elif((list_buttons[0]['text']=="X" and list_buttons[3]['text']=="X" and list_buttons[6]['text']=="X")
         or (list_buttons[0]['text']=="O" and list_buttons[3]['text']=="O" and list_buttons[6]['text']=="O")):
         bool=TRUE
         bool2=TRUE
         list_buttons[0].config(bg="green")
         list_buttons[3].config(bg="green")
         list_buttons[6].config(bg="green")
         if(list_buttons[0]['text']=="X"):
            label.config(text="Player 1 wins!")
         else:
            label.config(text="Player 2 wins!")

      elif((list_buttons[1]['text']=="X" and list_buttons[4]['text']=="X" and list_buttons[7]['text']=="X")
         or (list_buttons[1]['text']=="O" and list_buttons[4]['text']=="O" and list_buttons[7]['text']=="O")):
         bool=TRUE
         bool2=TRUE
         list_buttons[1].config(bg="green")
         list_buttons[4].config(bg="green")
         list_buttons[7].config(bg="green")
         if(list_buttons[1]['text']=="X"):
            label.config(text="Player 1 wins!")
         else:
            label.config(text="Player 2 wins!")

      elif((list_buttons[2]['text']=="X" and list_buttons[5]['text']=="X" and list_buttons[8]['text']=="X")
         or (list_buttons[2]['text']=="O" and list_buttons[5]['text']=="O" and list_buttons[8]['text']=="O")):
         bool=TRUE
         bool2=TRUE
         list_buttons[2].config(bg="green")
         list_buttons[5].config(bg="green")
         list_buttons[8].config(bg="green")
         if(list_buttons[2]['text']=="X"):
            label.config(text="Player 1 wins!")
         else:
            label.config(text="Player 2 wins!")

      elif((list_buttons[0]['text']=="X" and list_buttons[4]['text']=="X" and list_buttons[8]['text']=="X")
         or (list_buttons[0]['text']=="O" and list_buttons[4]['text']=="O" and list_buttons[8]['text']=="O")):
         bool=TRUE
         bool2=TRUE
         list_buttons[0].config(bg="green")
         list_buttons[4].config(bg="green")
         list_buttons[8].config(bg="green")
         if(list_buttons[0]['text']=="X"):
            label.config(text="Player 1 wins!")
         else:
            label.config(text="Player 2 wins!")

      elif((list_buttons[2]['text']=="X" and list_buttons[4]['text']=="X" and list_buttons[6]['text']=="X")
         or (list_buttons[2]['text']=="O" and list_buttons[4]['text']=="O" and list_buttons[6]['text']=="O")):
         bool=TRUE
         bool2=TRUE
         list_buttons[2].config(bg="green")
         list_buttons[4].config(bg="green")
         list_buttons[6].config(bg="green")
         if(list_buttons[2]['text']=="X"):
            label.config(text="Player 1 wins!")
         else:
            label.config(text="Player 2 wins!")
      if bool2:
         for x in list_buttons:
            x.config(state=DISABLED, disabledforeground="black")

   '''for x in range(3):
      for y in range(3):
         button=Button(frame1, width=10, height=5)
         button.config(command=lambda button1=button: click(button1)) #using lambda to define a function with 1 variable button1, and using it to fill in parameter for the function click
         list_buttons.append(button)
         button.grid(row=x, column=y)
   frame2.pack(side=TOP)
   frame1.pack(side=TOP, pady=5)
   frame3.pack(side=TOP)
   root.mainloop()
'''

class TTT:
   run=Create(Tk())
   def stop():
      TTT().run.root.destroy()
   def again():
      TTT().run.root.destroy()
      global bool
      bool=TRUE
      TTT()
   def execute(self):
      bool=FALSE
      global ttt
      ttt=TicTacToe()
      global list_buttons
      global label
      frame1=Frame(TTT.run.root)
      frame2=Frame(TTT.run.root)
      label=Label(frame2, text="Tic Tac Toe!")
      label.pack()
      num=0
      for x in range(3):
         for y in range(3):
            button=Button(frame1, width=10, height=5)
            button.config(command=lambda button1=button: ttt.click(button1)) #using lambda to define a function with 1 variable button1, and using it to fill in parameter for the function click
            list_buttons.append(button)
            button.grid(row=x, column=y)
      frame2.pack(side=TOP)
      frame1.pack(side=TOP, pady=5)
      global frame3
      frame3=Frame(TTT.run.root)
      quit=Button(frame3, text="Quit", command=TTT.stop)
      quit.pack(side=LEFT)
      repeat=Button(frame3, text="Play Again", command=TTT.again)
      repeat.pack(side=RIGHT)
      frame3.pack(side=TOP)
      TTT.run.root.mainloop()
        










      
    