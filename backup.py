from tkinter import *

root = Tk()
root.title('Quiz')
root.geometry("800x500")
data = {
        1 : ("What is the output of the following code : \nprint type(type(int))", 'type "int"', 'type "type"', 'Error', '0', '2'),
        2 : ("What is the output of the following code :\nL = ['a','b','c','d']", 'Error', 'None', 'abcd', '[‘a’,’b’,’c’,’d’]', '3'),
        3 : ("What is the output of the following segment :\nchr(ord('A'))", 'A', 'B', 'a', 'Error', '1'),
        4 : ("What is the output of the following code :\nL = ['a','b','c','d']", 'Error', 'None', 'abcd', '[‘a’,’b’,’c’,’d’]', '3'),
        5 : ("What is the output of the following segment :\nchr(ord('A'))", 'A', 'B', 'a', 'Error', '1'),
        6 : ("What is the output of the following code :\nL = ['a','b','c','d']", 'Error', 'None', 'abcd', '[‘a’,’b’,’c’,’d’]', '3'),
        7 : ("What is the output of the following segment :\nchr(ord('A'))", 'A', 'B', 'a', 'Error', '1'),
    }

# Display Questions
nextQuestion = 0

def clicked():
    global nextQuestion
    nextQuestion = nextQuestion+1

clicked()

for question_no, (QuestionText, op1, op2, op3, op4, ans) in data.items():
    if question_no == nextQuestion:
        q_no = question_no
        questionText = QuestionText
        disp_op1 = op1
        disp_op2 = op2
        disp_op3 = op3
        disp_op4 = op4
        actualAns = ans
        
        

        

# UI Components

# Question No.
Label(root, text='Question %d. '%(q_no), font=(
    "Helvetica", 15), fg="black").place(x=20, y=10)

# Question in textarea
# questionText = "Text Area"
text = Text(root, height=5, width=700, font=("Helvetica", 13))
scroll = Scrollbar(root, command=text.yview)
text.configure(yscrollcommand=scroll.set)
text.insert(END, questionText)
text.place(x=20, y=50)
scroll.pack(side=RIGHT, fill=Y)

# Options list

def selected():
    clickAns = str(var.get()) 
    rightAns = ""
    wrongAns = ""

    for question_no, (QuestionText, op1, op2, op3, op4, ans) in data.items():
        if question_no == q_no:
            actualAns = ans
            if ans == clickAns:
                rightAns = " Your Answer is correct !"
            else:
                wrongAns = " Your Answer is incorrect !"
        
        # Correct Answer
            # if ans == '1':
            #     actualAnslabel.config(text=" Correct Answer : %s" % op1)
            # elif ans == '2':
            #     actualAnslabel.config(text=" Correct Answer : %s" % op2)
            # elif ans == '3':
            #     actualAnslabel.config(text=" Correct Answer : %s" % op3)
            # elif ans == '4':
            #     actualAnslabel.config(text=" Correct Answer : %s" % op4)
            # else:
            #     pass
        rightAnslabel.config(text=rightAns)
        wrongAnslabel.config(text=wrongAns)
    

var = IntVar()
R1 = Radiobutton(root, text=disp_op1, font=("Helvetica", 10),
                    variable=var, value=1, command=selected)
R1.place(x=20, y=200)

R2 = Radiobutton(root, text=disp_op2, font=("Helvetica", 10),
                    variable=var, value=2, command=selected)
R2.place(x=20, y=240)

R3 = Radiobutton(root, text=disp_op3, font=("Helvetica", 10),
                    variable=var, value=3, command=selected)
R3.place(x=20, y=280)

R4 = Radiobutton(root, text=disp_op4, font=("Helvetica", 10),
                    variable=var, value=4, command=selected)
R4.place(x=20, y=320)


# Display Correct Answer, Wrong Anser and Actual Answer

rightAnslabel = Label(root, font=("Helvetica", 13), fg="green")
rightAnslabel.place(x=20, y=360)

wrongAnslabel = Label(root, font=("Helvetica", 13), fg="red")
wrongAnslabel.place(x=20, y=360)

actualAnslabel = Label(root, font=("Helvetica", 13), fg="green")
actualAnslabel.place(x=20, y=380)


B = Button(text="Next", command=clicked)
B.place(x=20, y=420)

root.mainloop()



######################################################################
################## UI ##########################

from tkinter import *

root = Tk()
root.title('Quiz')
root.geometry("800x500")

# UI Components

# Question No.
Label(root, text='Question 1. ', font=(
    "Helvetica", 15), fg="black").place(x=20, y=10)

# Question in textarea
questionText = "Text Area"
text = Text(root, height=5, width=700, font=("Helvetica", 13))
scroll = Scrollbar(root, command=text.yview)
text.configure(yscrollcommand=scroll.set)
text.insert(END, questionText)
text.place(x=20, y=50)
scroll.pack(side=RIGHT, fill=Y)

# Options list

def selected():
    clickAns = str(var.get()) 

var = IntVar()
R1 = Radiobutton(root, text="disp_op1", font=("Helvetica", 10),
                    variable=var, value=1, command=selected)
R1.place(x=20, y=200)

R2 = Radiobutton(root, text="disp_op2", font=("Helvetica", 10),
                    variable=var, value=2, command=selected)
R2.place(x=20, y=240)

R3 = Radiobutton(root, text="disp_op3", font=("Helvetica", 10),
                    variable=var, value=3, command=selected)
R3.place(x=20, y=280)

R4 = Radiobutton(root, text="disp_op4", font=("Helvetica", 10),
                    variable=var, value=4, command=selected)
R4.place(x=20, y=320)


# Display Correct Answer, Wrong Anser and Actual Answer

rightAnslabel = Label(root, font=("Helvetica", 13), fg="green")
rightAnslabel.place(x=20, y=360)

wrongAnslabel = Label(root, font=("Helvetica", 13), fg="red")
wrongAnslabel.place(x=20, y=360)

actualAnslabel = Label(root, font=("Helvetica", 13), fg="green")
actualAnslabel.place(x=20, y=380)


B = Button(text="Next")
B.place(x=20, y=420)

root.mainloop()

############################################### New Backup #########################################################

from tkinter import *

class UiComponents:
    def __init__(self):
        self.root = Tk()
        self.root.title('Quiz')
        self.root.geometry("800x500")
        self.QuestionNo()
        self.TextArea()
        self.OptioList()
        self.AnserLabels()
        self.NextButton()
        self.root.mainloop()

    def QuestionNo(self):
        # Question No.
        Label(root, text='Question 1. ', font=("Helvetica", 15), fg="black").place(x=20, y=10)

    def TextArea(self):
        # Question in textarea
        questionText = "Text Area"
        text = Text(root, height=5, width=700, font=("Helvetica", 13))
        scroll = Scrollbar(root, command=text.yview)
        text.configure(yscrollcommand=scroll.set)
        text.insert(END, questionText)
        text.place(x=20, y=50)
        scroll.pack(side=RIGHT, fill=Y)
    
    def OptioList(self):
        # Options list
        self.selectedOption()
        var = IntVar()
        R1 = Radiobutton(root, text="disp_op1", font=("Helvetica", 10),
                            variable=var, value=1, command=selected)
        R1.place(x=20, y=200)

        R2 = Radiobutton(root, text="disp_op2", font=("Helvetica", 10),
                            variable=var, value=2, command=selected)
        R2.place(x=20, y=240)

        R3 = Radiobutton(root, text="disp_op3", font=("Helvetica", 10),
                            variable=var, value=3, command=selected)
        R3.place(x=20, y=280)

        R4 = Radiobutton(root, text="disp_op4", font=("Helvetica", 10),
                            variable=var, value=4, command=selected)
        R4.place(x=20, y=320)

    def selectedOption(self):
        clickAns = str(var.get()) 

    def AnserLabels(self):
        rightAnslabel = Label(root, font=("Helvetica", 13), fg="green")
        rightAnslabel.place(x=20, y=360)

        wrongAnslabel = Label(root, font=("Helvetica", 13), fg="red")
        wrongAnslabel.place(x=20, y=360)

        actualAnslabel = Label(root, font=("Helvetica", 13), fg="green")
        actualAnslabel.place(x=20, y=380)

    def NextButton(self):
        B = Button(text="Next")
        B.place(x=20, y=420)

UiComponents()


########################################## Creat new multi pages app ###########################################

# The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/	

import tkinter as tk


LARGE_FONT= ("Verdana", 12)


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = tk.Button(self, text="Visit Page 1",
                            command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2 = tk.Button(self, text="Visit Page 2",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()
        


app = SeaofBTCapp()
app.geometry("400x400")
app.title("MY APP")
app.mainloop()