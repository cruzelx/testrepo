from tkinter import *
import sys

class Window(Frame):
    def __init__(self,master = None):
        super().__init__(master)
        self.master = master
        self.gui()

    def gui(self):
        self.master.title("WINDOWS GUI")
        self.pack(fill = BOTH, expand = 1)
        quitButton = Button(self, text="Quit", command =self)
        quitButton.place(x=10, y=10)

root = Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop()
        
