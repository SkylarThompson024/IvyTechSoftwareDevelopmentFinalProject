import tkinter as tk
from tkinter import *

class main_window(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.geometry('700x500')
        self.title('Burger Builder')        #Creates Main Window
        self.config(bg="#8d96a6")
        
        label1 = Label(self, text="Build your Customized Burger", 
                       font=('Papyrus', 16),
                       bg="#8d96a6",                        #Creates the Header
                       padx=10,
                       pady=10)
        label1.grid(row=0, column=0, columnspan=3)
        
        label2 = Label(self, text="Total: $",
                       font=(16),                           #Creates the Total Counter
                       bg="#8d96a6")
        label2.grid(row=0, column=5)
        
        label3 = Label(self,text="Buns",
                       font=(10),
                       bg="#b2bccf")
        label3.grid(row=1, column=0)
        
        label4 = Label(self,text="Cheese",
                       font=(10),
                       bg="#b2bccf")
        label4.grid(row=1, column=1)
        
        label5 = Label(self,text="Meat",
                       font=(10),
                       bg="#b2bccf")
        label5.grid(row=1, column=2)
        
        label6 = Label(self,text="Toppings",
                       font=(10),
                       bg="#b2bccf")
        label6.grid(row=1, column=3)
        
        
        
if __name__ == "__main__":
    main_window().mainloop()