from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import scrolledtext


root = Tk(className="Ashraf personal text editor")
root.geometry("800x800")
textPad = scrolledtext.ScrolledText(root, width=100, height=100)

#create menu function for each menu item

def open_commnad():
    file = filedialog.askopenfile(parent=root, mode="rb", title="select a file")
    if file != None:
        contents = file.read()
        textPad.insert('1.0', contents)
        file.close()


def save_command():
    file = filedialog.asksaveasfile(mode="w")
    if file != None:
        data = textPad.get('1.0', END + '-1c')
        file.write(data)
        file.close()

def exit_command():
    if messagebox.askokcancel("Quit","Do your really want to quit"):
        root.distroy()

def about_command():
    label = messagebox.showinfo("About","This editor was created by ashraf for practice purpose")

menu = Menu(root)
root.config(menu=menu)
submenu = Menu(menu)
menu.add_cascade(label="File", menu=submenu)
menu.add_cascade(label="Edit")
menu.add_cascade(label="View")
menu.add_cascade(label="Navigate")
menu.add_cascade(label="Code")
menu.add_cascade(label="Refractor")
menu.add_cascade(label="copy")


submenu.add_command(label="New")
submenu.add_command(label="Open", command=open_commnad)
submenu.add_command(label="save as", command=save_command)
submenu.add_separator()
submenu.add_command(label="exit", command=exit_command)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About", command=about_command)

textPad.pack()
root.mainloop()
