import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

label1 = tk.Label(root, text="Label 1", bg="red")
label2 = tk.Label(root, text="Label 2", bg="green")
label3 = tk.Label(root, text="Label 3", bg="blue")

label1.grid(row=0, column=0, padx=5, pady=5)
label2.grid(row=0, column=1, padx=5, pady=5)
label3.grid(row=1, column=0, columnspan=2, sticky="ew")

root.mainloop()