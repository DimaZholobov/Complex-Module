from tkinter import *
from tkinter import messagebox
from math import sqrt
 
 
def modul():
    messagebox.showinfo("GUI Python",  sqrt(float(re.get())**2 + float(im.get())**2))
 
root = Tk()
root.title("GUI на Python")
 
re = IntVar()
re.set(0)
im = IntVar()
im.set(0)
 
re_label = Label(text="Введите действительную часть:")
im_label = Label(text="Введите мнимую часть")
 
re_label.grid(row=0, column=0, sticky="w")
im_label.grid(row=1, column=0, sticky="w")
 
re_entry = Entry(textvariable=re)
im_entry = Entry(textvariable=im)

#restr = re.get()
#imstr = im.get()

#modul = sqrt(float(re.get())**2 + float(im.get())**2)
 
re_entry.grid(row=0,column=1, padx=5, pady=5)
im_entry.grid(row=1,column=1, padx=5, pady=5)
 
 
message_button = Button(text="Click Me", command=modul)
message_button.grid(row=2,column=1, padx=5, pady=5, sticky="e")
 
root.mainloop()
