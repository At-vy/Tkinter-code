# Creating a Canvas where 
# 1.clicking on a place will create a Dot 
# 2.pressing C will erase the canvas 
# 3.holding a button will change a color
from tkinter import *
root = Tk()
root.title("Canvas")
root.geometry("1100x700")
canvas = Canvas(root, width=1000, height=650, bg="orange")
canvas.pack()
# A label to track the position of the cursor
def update_label(e):
    x,y = e.x,e.y
    track_label.config(text=f"Coordinates:{(x,y)}")
track_label  =Label(root, text="Coordinates:(x,y)",border=2)
track_label.pack()
root.bind("<Motion>",update_label)
# left click -> Blue 
def blue_circle(e):
    x,y= e.x,e.y
    r = 10
    canvas.create_oval(x-r, y-r, x+r, y+r, fill="blue")
# right click -> Red
def red_circle(e):
    x,y= e.x,e.y
    r = 10
    canvas.create_oval(x-r, y-r, x+r, y+r, fill="red")
# Erasing the canvas 
def Erase(e):
    canvas.delete("all")
def Save(e):
    canvas.postscript(file = "Canvas_output.ps")
    print("The file was saved in .ps")
    # Converting .ps file to .png file 
    from PIL import Image
    img = Image.open("Canvas_output.ps")
    img.save("canvas_output.png")
    print("the image was saved as .png")
# binding the functions 
canvas.bind("<Button-1>",blue_circle)
canvas.bind("<Button-3>",red_circle)
root.bind("<KeyPress-c>",Erase)
root.bind("<KeyPress-s>",Save)




root.mainloop()
