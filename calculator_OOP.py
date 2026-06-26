# A GUI for a simple calculator using tkinter 
import tkinter as tk 
class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator By Atharva")
        self.root.geometry("500x700")
        self.expression = "" # stores the current input expression
        self.input_text = tk.StringVar() # variable to update the input feild
    # Creating a Input widget
        self.frame = tk.Frame(self.root, width=450, height=50, bd=0, highlightbackground="black",highlightcolor="black", highlightthickness=2)
        self.frame.grid(row=0, column=0, columnspan=4)
        self.input_feild = tk.Entry(self.root, font = ('lucida', 15, "bold"), textvariable=self.input_text, width=50,)
        self.input_feild.grid(row=0, column=0, columnspan=4)
        self.Create_buttons()
    # creating buttons 
    def Create_buttons(self):
        button = [
            ('7',1,0),('8',1,1),('9',1,2),('/',1,3),
            ('4',2,0),('5',2,1),('6',2,2),('*',2,3),
            ('3',3,0),('2',3,1),('1',3,2),('+',3,3),
            ('.',4,0),('0',4,1),('C',4,2),('=',4,3),
        ]
        for(text, row, column) in button:
            btn = tk.Button(self.root, text=text, width=10, height=3,command=lambda t = text: self.button_click(t) )
            btn.grid(row = row, column = column)
            # function for button click
    def button_click(self, text):
        if text == 'C':
            self.expression = ""
            self.input_text.set("")
        elif text == '=':
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result
        else:
            self.expression += text
            self.input_text.set(self.expression)
if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
