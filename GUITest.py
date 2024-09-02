from tkinter import *

def new_Window():
    windowNew=Tk()
    canvas2=Canvas(windowNew, 100, 100)
    canvas2.pack()



root=Tk() #Establishes a window
root.geometry("300x300+500+200")  #Dimensions and size of window
root.title("Log-in Page") #Name of the window
image=PhotoImage(file="C:\\Users\\venki\\VSCode\\Python\\login.png")
root.iconphoto(True, image)
root.config(background="black")

text=Text(root, width=20, height=2)
text.pack(padx=20)


button=Button(root, text="Click Me!", command=new_Window)
button.pack()
root=mainloop()