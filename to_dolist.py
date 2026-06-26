# A to do list to store and manage tasks 
# 1. Add tasks via an Entry + Button.
# 2. Display tasks in a Listbox.
# 3. Delete selected tasks.
# 4. Mark tasks as complete (change color or prefix).
# 5. Save tasks to a file and reload them when the app starts
from tkinter import *
root = Tk()
root.title("To-Do List")
root.geometry("700x750")
tasks = [] # creating an empty list named task 
# creating a label 
head_label = Label(root, text="Tasks", font="Sans 15 bold",borderwidth=3)
head_label.grid(column=2,row=0,pady=5)
# Listbox 
listbox = Listbox(root,width=50,height=15,relief= RIDGE, borderwidth=3)
listbox.grid(column=2,row=1,pady=5)
# Adiing a label 
Entry_label = Label(root, text="Enter the task")
Entry_label.grid(column=2,row=2,pady=3)
# Entry widget to add the tasks 
entry = Entry(root,relief=SUNKEN, highlightbackground="#fed7ba", highlightthickness=2, width=40)
entry.grid(column=2,row=3,pady=5)

# a function to add tasks to the listbox 
def Add_tasks(e = None):
    task_text = entry.get()
    if task_text != "":
        task = {"text":task_text,"done" : False} # storing task as a dictionaries 
        tasks.append(task)
        listbox.insert(END,task_text)
        entry.delete(0,END)
add_btn = Button(root, text="Add",command=Add_tasks)
add_btn.grid(column=3,row=1,pady=15,padx=20,sticky=N)
root.bind("<Return>",Add_tasks)

# creating a function to delete 
def Delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        listbox.delete(index)
        tasks.pop(index)
delete_btn = Button(root,text="Delete task", command=Delete_task)
delete_btn.grid(column=3,row=1,pady=15,padx=20)

# Making a load button to upload tasks in a file 
def load_tasks():
    try:
        with open ("task.txt","r") as f:
            loaded = f.readlines()
        tasks.clear()
        listbox.delete(0,END)
        for line in loaded:
            status , text = line.strip().split("|",1)
            done = (status == "Done")
            task = {"text":text,"done":done}
            tasks.append(task)
            listbox.insert(END,text)
            if done:
                listbox.itemconfig(END,fg = "green")
        print("task loaded from task.txt")
    except FileNotFoundError:
        print("Nosaved tasks found.")     
load_btn = Button(root, text="Load task",command=load_tasks)
load_btn.grid(column=3,row=1,pady=15,padx=20)  

# Marking completion of tasks 
def completion_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        tasks[index]["done"] = True
        listbox.itemconfigure(index,fg = "green")
completion_btn = Button(root,text= "completed",command=completion_task)
completion_btn.grid(column=3,row=1,pady=15,padx=20,sticky=S)

# save function
def save_task():
    with open("task.txt","w") as f:
        for task in tasks:
            status = "Done" if task["done"] else ["To-Do"]
            f.write(f"{status}|{task['text']}\n")
        print("Task saved Succesfully")
save_btn = Button(root,text= "Save",command=save_task)
save_btn.grid(column=3,row=1,pady=15,padx=20)


root.mainloop()