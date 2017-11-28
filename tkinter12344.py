from tkinter import *
mast = Tk()
write = "hey there\nDelilah!!"
msg = Message(mast, text=write)
msg.config(takefocus='True',width='500',relief='raised', bg='lightblue',foreground='white',font=('ariel',20), justify='left',padx='15',pady='15')
msg.pack()
mainloop()
