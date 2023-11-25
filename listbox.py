from tkinter import *
root = Tk()
root.geometry("700x300")
root.title("listbox")



def add():
    global i
    lbx.insert(ACTIVE, f"{i}")
    i+=1



i= 0 
lbx= Listbox(root)
lbx.pack()
lbx.insert(END,"item in the End")

button = Button(root,text="Add item", command=add)
button.pack()



root.mainloop()