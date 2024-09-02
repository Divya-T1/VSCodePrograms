from tkinter import *

root = Tk() #establishes frame as in JFrame frame=new JFrame
root.geometry("300x300") #gives dimensions to frame

l = Label(root, text="Hey!") #initializes a variable with the given Label and its parameters
l.pack() #adds label to the frame

text1=text("Hola!")
text1.pack()

root.mainloop() #Allows for frame to show up