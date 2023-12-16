import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk


class main_window(tk.Tk):
    def __init__(self):
        super().__init__()
        
        
        ########################        Main Window      ########################
        #Creates the Main Window, Main Window Configurations
        self.geometry('425x200')
        self.title('Burger Builder')        
        self.config(bg="#8d96a6")
        
        
        ########################         Header      ########################
        #Creates the Header of the Main Window with a phrase and an image
        label1 = Label(self, text="Build your Customized Burger",
                       font=('Papyrus', 16),
                       bg="#8d96a6",                        
                       padx=10,
                       pady=10)
        label1.grid(row=0, column=0, columnspan=3)
        
        photo = Image.open('burger_icon.png').resize((50,50))
        self.imageTk = ImageTk.PhotoImage(photo)
        
        imageLabel1 = Label(self, image= self.imageTk, bg="#8d96a6", text="Burger")
        imageLabel1.grid(row=0, column=3)
        
        
        
        ########################        Buns Options      ########################
        #Creates the Header for the Buns Options and creates each bun options as radio buttons
        label3 = Label(self,text="Buns", borderwidth=1, relief="ridge",
                       font=(10),
                       bg="#b2bccf")
        label3.grid(row=1, column=0)
        
        self.B = IntVar()
        
        rb1 = Radiobutton(self, text="Regular Bun", variable=self.B, value=1, bg="#8d96a6")
        rb1.grid(row=2, column=0, sticky="W")
        rb2 = Radiobutton(self, text="Potato Bun", variable=self.B, value=2, bg="#8d96a6")          
        rb2.grid(row=3, column=0, sticky="W")
        rb3 = Radiobutton(self, text="Pretzel Bun", variable=self.B, value=3, bg="#8d96a6")
        rb3.grid(row=4, column=0, sticky="W")
        
        ########################        Cheese Options      ########################
        #Creates the Header for the Cheese Options and creates each cheese options as radio buttons
        label4 = Label(self,text="Cheese", borderwidth=1, relief="ridge",
                       font=(10),
                       bg="#b2bccf")
        label4.grid(row=1, column=1)
              
        self.C = IntVar()
        
        rb4 = Radiobutton(self, text="American Cheese", variable=self.C, value=1, bg="#8d96a6")
        rb4.grid(row=2, column=1, sticky="W")
        rb5 = Radiobutton(self, text="PepperJack Cheese", variable=self.C, value=2, bg="#8d96a6")
        rb5.grid(row=3, column=1, sticky="W")
        rb6 = Radiobutton(self, text="Colby Jack Cheese", variable=self.C, value=3, bg="#8d96a6")
        rb6.grid(row=4, column=1, sticky="W")
        
        ########################        Meat Options      ########################
        #Creates the Header for the Meats Options and creates each meat options as radio buttons
        label5 = Label(self,text="Meat", borderwidth=1, relief="ridge",
                       font=(10),
                       bg="#b2bccf")
        label5.grid(row=1, column=2)
        
        self.M = IntVar()
        
        rb7 = Radiobutton(self, text="Beef", variable=self.M, value=1, bg="#8d96a6")
        rb7.grid(row=2, column=2, sticky="W")
        rb8 = Radiobutton(self, text="Chicken", variable=self.M, value=2, bg="#8d96a6")
        rb8.grid(row=3, column=2, sticky="W")
        rb9 = Radiobutton(self, text="Veggie", variable=self.M, value=3, bg="#8d96a6")
        rb9.grid(row=4, column=2, sticky="W")
        
        ########################        Toppings Options      ########################
        #Creates the Header for the Toppings Options and creates each toppings options as checkboxes
        label6 = Label(self,text="Toppings", borderwidth=1, relief="ridge",
                       font=(10),
                       bg="#b2bccf")
        label6.grid(row=1, column=3)
        
        self.T1 = IntVar()
        self.T2 = IntVar()
        self.T3 = IntVar()
        
        cb1 = Checkbutton(self, text="Pickles", variable=self.T1, onvalue=1, offvalue=0, bg="#8d96a6")
        cb1.grid(row=2, column=3, sticky="W")
        cb2 = Checkbutton(self, text="Onions", variable=self.T2, onvalue=1, offvalue=0, bg="#8d96a6")
        cb2.grid(row=3, column=3, sticky="W")
        cb3 = Checkbutton(self, text="Lettuce", variable=self.T3, onvalue=1, offvalue=0, bg="#8d96a6")
        cb3.grid(row=4, column=3, sticky="W")
        
        ########################        Misc Buttons      ########################
        #Creates the Preview Burger Button to open second window and Close Burger Builder Button to close main window
        button1 = Button(self, text="Preview Burger", command=self.preview_window, bg="#b2bccf", borderwidth=1, relief="ridge")
        button1.grid(row=8, column=0, columnspan=2, rowspan=3)
        
        
        button2 = Button(self, text="Close Burger Builder", command=self.destroy, bg="#b2bccf", borderwidth=1, relief="ridge")
        button2.grid(row= 8, column=2, columnspan=2, rowspan=3)
        
    ########################        Preview Window Function      ########################
    #Creates the preview_window function to open the second window
    def preview_window(self):
        
        window = window2(self)              
        window.grab_set()
        
    
class window2(tk.Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        
        ########################        Second Window      ########################
        #Creates the Second Window, Second Window Configurations
        self.title('Preview Window')
        self.config(bg='#5f6f7f')
        
        
        ########################        Buns Options      ########################
        #Gets the value of the Radio Buttons from the Main Window and sets bunOption variable and bunPrice variable accordingly
        bunFromMain = parent.B.get()
        if (bunFromMain == 1):
            bunOption = "Regular Bun:"
            bunPrice = 1.00
        elif (bunFromMain == 2):
            bunOption = "Potato Bun:"
            bunPrice = 1.50
        elif (bunFromMain == 3):
            bunOption = "Pretzel Bun:"
            bunPrice = 2.25
        else:
            bunOption = "No Bun Selected"
            bunPrice = 0.00
        #Creates the label for what bun option was chosen
        label2 = Label(self, text=bunOption, bg='#6d8194')
        label2.grid(row=1, column=0, sticky="W")
        
        
        ########################        Cheese Options      ########################
        #Gets the value of the Radio Buttons from the Main Window and sets cheeseOption variable and cheesePrice variable accordingly
        cheeseFromMain = parent.C.get()
        if(cheeseFromMain == 1):
            cheeseOption = "American Cheese:"
            cheesePrice = 1.00
        elif(cheeseFromMain == 2):
            cheeseOption = "Pepper Jack Cheese:"
            cheesePrice = 1.75
        elif(cheeseFromMain == 3):
            cheeseOption = "Colby Jack Cheese:"
            cheesePrice = 1.25
        else:
            cheeseOption = "No Cheese Selected"
            cheesePrice = 0.00
        #Creates the label for what cheese option was chosen
        label3 = Label(self, text=cheeseOption, bg='#5f6f7f')
        label3.grid(row=2, column=0, sticky="W")
        
        
        ########################        Meat Options      ########################
        #Gets the value of the Radio Buttons from the Main Window and sets meatOption variable and meatPrice variable accordingly
        meatFromMain = parent.M.get()
        if(meatFromMain == 1):
            meatOption = "Beef:"
            meatPrice = 3.25
        elif(meatFromMain == 2):
            meatOption = "Chicken:"
            meatPrice = 3.00
        elif(meatFromMain == 3):
            meatOption = "Veggie:"
            meatPrice = 4.25
        else:
            meatOption = "No Meat Selected"
            meatPrice = 0.00
        #Creates the label for what meat options was chosen
        label4 = Label(self, text=meatOption, bg='#6d8194')
        label4.grid(row=3, column=0, sticky="W")
        
        
        ########################        Toppings Options      ########################
        #Gets the value of the CheckBoxes from the Main Window and sets T#Option variable and T#Price variable accordingly
        T1FromMain = parent.T1.get()
        T2FromMain = parent.T2.get()
        T3FromMain = parent.T3.get()
        if(T1FromMain == 1):
            T1Option = "Pickles:"
            T1Price = 1.00
        elif(T1FromMain == 0):
            T1Option = "No Pickles:"
            T1Price = 0.00
        if(T2FromMain == 1):
            T2Option = "Onions:"
            T2Price = 1.50
        elif(T2FromMain == 0):
            T2Option = "No Onions:"
            T2Price = 0.00
        if(T3FromMain == 1):
            T3Option = "Lettuce:"
            T3Price = 0.99
        elif(T3FromMain == 0):
            T3Option = "No Lettuce:"
            T3Price = 0.00
        #Creates the labels for each of the T# options that were chosen
        label5 = Label(self, text=T1Option, bg='#5f6f7f')
        label5.grid(row=4, column=0, sticky="W")
        
        label6 = Label(self, text=T2Option, bg='#6d8194')
        label6.grid(row=5, column=0, sticky="W")
        
        label7 = Label(self, text=T3Option, bg='#5f6f7f')
        label7.grid(row=6, column=0, sticky="W")
                
        ########################        Price Controller      ########################
        #Calculates the Total Price of all of the options chosen and creates labels for each individual item selected
        strTotal = "Total: $"
        
        floatTotal = bunPrice + cheesePrice + meatPrice + T1Price + T2Price + T3Price
        
        finalTotal = strTotal + "%5.2f" % floatTotal
        
        label1 = Label(self, text=finalTotal,
                       font=(16),
                       bg='#5f6f7f')
        label1.grid(row=0, column=3, sticky="E")
        
        label8 = Label(self, text="$%5.2f" % bunPrice, bg='#6d8194')
        label8.grid(row=1, column=3, sticky="E")
        
        label9 = Label(self, text="$%5.2f" % cheesePrice, bg='#5f6f7f')
        label9.grid(row=2, column=3, sticky="E")
        
        label10 = Label(self, text="$%5.2f" % meatPrice, bg='#6d8194')
        label10.grid(row=3, column=3, sticky="E")
        
        label11 = Label(self, text="$%5.2f" % T1Price, bg='#5f6f7f')
        label11.grid(row=4, column=3, sticky="E")
        
        label12 = Label(self, text="$%5.2f" % T2Price, bg='#6d8194')
        label12.grid(row=5, column=3, sticky="E")
        
        label13 = Label(self, text="$%5.2f" % T3Price, bg='#5f6f7f')
        label13.grid(row=6, column=3, sticky="E")
        
        ########################        Misc      ########################
        #Creates a miscellaneous label for extra design and creates an image
        label14 = Label(self, text="All orders come with a side of fries!", bg='#6d8194')
        label14.grid(row=7, column=0, sticky="E")
        
        photo2 = Image.open('fries_icon.png').resize((50,50))
        self.imageTk = ImageTk.PhotoImage(photo2)
        
        imageLabel2 = Label(self, image= self.imageTk, bg='#6d8194', text="Fries")
        imageLabel2.grid(row=7, column=3, sticky="E")
        
        btn1 = Button(self, text="Close Burger Preview", command=self.destroy, bg='#b2bccf')
        btn1.grid(row=9, column=0, columnspan=5)
        
        
        
if __name__ == "__main__":
    main_window().mainloop()