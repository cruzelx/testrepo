from tkinter import *
import time

class body(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.gui()
        self.menu()
        self.frames()


    def gui(self):
        self.master.title("CHATBOX")
        self.master.geometry("700x400")
        self.pack(fill = BOTH, expand = False)

    def menu(self):
        #create menu instance
        menu = Menu(self.master) 
        self.master.config(menu=menu)

        #create file object
        file = Menu(menu)
        file.add_command(label="Exit", command=self.exit_window)
        menu.add_cascade(label="File", menu=file)

        #edit
        edit= Menu(menu)
        edit.add_command(label="Undo")
        edit.add_command(label="Redo")
        menu.add_cascade(label="Edit", menu=edit)

        #help
        helps=Menu(menu)
        helps.add_command(label="Tutorial")
        menu.add_cascade(label="Help", menu=helps)
        

    def frames(self):
        #create 3 verticle frames
        frame0 = Frame(self)
        frame0.pack()
        frame1 = Frame(frame0, borderwidth = 0 )
        label = Label(frame1, padx='0px', bg="red", width=20, height=20)
        label.pack()
        frame1.pack(side=LEFT)

        frame2 = Frame(frame0,  borderwidth = 0 )
        frameName = Frame(frame2, borderwidth = 0)
        frameName.pack()
        label2 = Label(frame2,padx='0px', bg="yellow",pady='0px', width=40, height=17)
        labelName = Label(frameName, bg="lightblue", pady = '0px',height=3, width=40)
        label2.pack()
        labelName.pack()
        
        frame2.pack(side=LEFT)

        frame3 = Frame(frame0,  borderwidth = 0 )
        label3 = Label(frame3,padx='0px', bg="blue", width=20, height=20)
        label3.pack()
        frame3.pack(side=LEFT)

        frame00 = Frame(self)
        frame00.pack(pady=10/2)
        frame4 = Frame(frame00, borderwidth = 0, width=82)
        label4 = Label(frame4, bg="green", width=20, height=7)
        label4.pack(side=LEFT)

        msg = Text(frame4, height=7, width=20)
        msg.pack(fill=BOTH, side=LEFT)
        frame4.pack()

    def exit_window(self):
        exit()
        
        
        
        

root = Tk()
root.resizable(width=False, height=False)
app = body(root)
root.mainloop()

    
        
