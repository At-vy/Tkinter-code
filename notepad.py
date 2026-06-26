# Creating a notepad using Tkinter
from tkinter import *
import tkinter.messagebox as msg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
# defining functions 
def newfile():
    global file
    root.title("Untitled - Notepad")
    file = None
    text.delete(1.0, END)
def openfile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents","*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        text.delete(1.0, END)
        f = open(file, "r")
        text.insert(1.0, f.read())
        f.close()

def save():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='untitled.txt', defaultextension='.txt', filetypes=[("All files","*.*"), ("Text Documents", "*.txt")] )
        if file == "":
            file = None
        else: 
            # Saving the file 
            f = open(file, "w")
            f.write(text.get(1.0, END)) 
            f.close()
            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Saving the file 
        f = open(file, "w")
        f.write(text.get(1.0, END)) 
        f.close()

            
def Cut():
    text.event_generate(('<<Cut>>'))
def copy():
    text.event_generate(('<<Copy>>'))
def Paste():
    text.event_generate(('<<Paste>>'))
def about():
    msg.showinfo("About", "Trial Notepad By Atharva")

if __name__ == '__main__':
    # basic setup of tkinter 
    root = Tk()
    root.title("Untitlet - Notepad")
    root.geometry('400x600')
    # to add icon
    # root.iconbitmap(pass_the_file_location)

    # Text Area 
    text = Text(root, font=("lucida","15"))
    file = None # none means that no file will open initially till a file is opeaned 
    text.pack(fill=BOTH,expand=True)

    # Menu 
    menubar = Menu(root)

    # inside the menubar 
    # file menu starts 
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New File", command=newfile) # to create a new file
    filemenu.add_command(label="Open File", command=openfile) # to open a new file 
    filemenu.add_command(label="Save", command=save) # to save a file 
    filemenu.add_separator()
    filemenu.add_command(label="Quit", command=quit)
    menubar.add_cascade(label="File", menu=filemenu)
    # File menu ends 

    # edit menu starts 
    editmenu = Menu(menubar, tearoff=0)
    # commands to Cut Copy and Paste 
    editmenu.add_command(label="Cut", command=Cut)
    editmenu.add_command(label="Copy", command=copy)
    editmenu.add_command(label="Paste", command=Paste)
    menubar.add_cascade(label="Edit", menu=editmenu)
    # edit menu ends 

    # Help menu starts 
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="About", command=about)
    menubar.add_cascade(label="Help", menu=helpmenu)
    # help menu ends 
    root.config(menu=menubar)

    # Adding a scrollbar 
    scrollbar = Scrollbar(text)
    scrollbar.pack(side = RIGHT, fill = Y)
    scrollbar.config(command=text.yview)
    text.config(yscrollcommand=scrollbar.set)

    root.mainloop()
