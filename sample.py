from tkinter import *
import time
class App(Frame):
    def __init__(self, master=None):
        'Start Application'
        Frame.__init__(self, master)
        self.pack()
        self.countdown(120) # Start Timer      
        
    def countdown(self, remaining = None):
        'Countdown Timer'
        self.label = Label(text="Time  ", fg="Red", font=("Helvetica", 18))
        self.label.place(x=150,y=13)
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            self.label.configure(text="'s up!")
        else:
            self.label.configure(text="%d" % self.remaining)
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)
            
class NewWindow():
    def show(self):
        root = Tk() 
        root.title('Create New Quiz')
        root.geometry("800x500") 
        top.mainloop()


newWin = NewWindow()

# here are method calls to the window manager class
myapp = App()
   
# Create the Application here
myapp.master.title("Quiz Application")
myapp.master.geometry("800x500")
myapp.master.resizable(True, True)
menu = Menu(myapp)
myapp.master.config(menu=menu) 
filemenu = Menu(menu) 
menu.add_cascade(label='File', menu=filemenu) 
filemenu.add_command(label='Create New Quiz',command=newWin.show) 
filemenu.add_command(label='Start Quiz') 
filemenu.add_separator() 
filemenu.add_command(label='Exit', command=myapp.master.quit) 
helpmenu = Menu(menu) 
menu.add_cascade(label='Help', menu=helpmenu) 
helpmenu.add_command(label='About') 

labelTimer = Label(text="Timer : ", fg="Red", font=("Helvetica", 18))
labelTimer.place(x=40,y=10)
# labelTimer.grid(row = 0, column = 0, pady = 2)

# text = Label(myapp, text="Just do it",font=("Helvetica", 15)).grid(row = 0, column = 0, pady = 2) 


# # this wil create a label widget 
# l1 = Label(myapp, text = "First:") 
# l2 = Label(myapp, text = "Second:") 
  
# # grid method to arrange labels in respective 
# # rows and columns as specified 
# l1.grid(row = 0, column = 0, sticky = W, pady = 20) 
# l2.grid(row = 1, column = 0, sticky = W, pady = 20) 
  
# # entry widgets, used to take entry from user 
# e1 = Entry(myapp) 
# e2 = Entry(myapp) 
  
# # this will arrange entry widgets 
# e1.grid(row = 0, column = 1, pady = 2) 
# e2.grid(row = 1, column = 1, pady = 2) 



# Label(myapp, text = 'It\'s a Quiz Application',font=("Helvetica", 18),fg="black").pack(side = TOP, pady = 10)
# start the program
myapp.mainloop()





# # from tkinter import *
# # root = Tk() 
# # root.title('GfG') 

# # top = Toplevel(bg="red") 
# # top.title('Python') 

# # top.mainloop()


# # import tkinter module 
# from tkinter import * 
# from tkinter.ttk import *

# # creating main tkinter window/toplevel 
# master = Tk() 

# # this will create a label widget 
# l1 = Label(master, text = "Height") 
# l2 = Label(master, text = "Width") 

# # grid method to arrange labels in respective 
# # rows and columns as specified 
# l1.grid(row = 0, column = 0, sticky = W, pady = 2) 
# l2.grid(row = 1, column = 0, sticky = W, pady = 2) 

# # entry widgets, used to take entry from user 
# e1 = Entry(master) 
# e2 = Entry(master) 

# # this will arrange entry widgets 
# e1.grid(row = 0, column = 1, pady = 2) 
# e2.grid(row = 1, column = 1, pady = 2) 

# # checkbutton widget 
# c1 = Checkbutton(master, text = "Preserve") 
# c1.grid(row = 2, column = 0, sticky = W, columnspan = 2) 

# # adding image (remember image should be PNG and not JPG) 
# img = PhotoImage(file = r"C://Users/pradeepBhardwaj/Desktop/Machine_Lerning/Thinking-of-getting-a-cat.png") 
# img1 = img.subsample(2, 2) 

# # setting image with the help of label 
# Label(master, image = img1).grid(row = 0, column = 2, 
# 	columnspan = 2, rowspan = 2, padx = 5, pady = 5) 

# # button widget 
# b1 = Button(master, text = "Zoom in") 
# b2 = Button(master, text = "Zoom out") 

# # arranging button widgets 
# b1.grid(row = 2, column = 2, sticky = E) 
# b2.grid(row = 2, column = 3, sticky = E) 

# # infinite loop which can be terminated 
# # by keyboard or mouse interrupt 
# mainloop() 
