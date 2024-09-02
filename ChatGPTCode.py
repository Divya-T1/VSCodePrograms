import tkinter as tk

class WindowManager:
    def __init__(self, root):
        self.root = root
        self.create_first_window()

    def create_first_window(self):
        # Create the first window
        self.first_window = tk.Toplevel(self.root)
        self.first_window.title("First Window")

        # Add widgets to the first window
        label = tk.Label(self.first_window, text="This is the first window.")
        label.pack(padx=10, pady=10)

        button = tk.Button(self.first_window, text="Switch Window", command=self.switch_window)
        button.pack(pady=10)

    def create_second_window(self):
        # Create the second window
        self.second_window = tk.Toplevel(self.root)
        self.second_window.title("Second Window")

        # Add widgets to the second window
        label = tk.Label(self.second_window, text="This is the second window.")
        label.pack(padx=10, pady=10)

        button = tk.Button(self.second_window, text="Switch Window", command=self.switch_window)
        button.pack(pady=10)

    def switch_window(self):
        # Destroy the current window and create the next one
        if hasattr(self, 'first_window') and self.first_window.winfo_exists():
            self.first_window.destroy()
            self.create_second_window()
        elif hasattr(self, 'second_window') and self.second_window.winfo_exists():
            self.second_window.destroy()
            self.create_first_window()

if __name__ == "__main__":
    root = tk.Tk()
    app = WindowManager(root)
    root.mainloop()
