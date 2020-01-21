from tkinter import *

def newQuiz():
    root = Tk()
    root.title('Create New Quiz')
    root.geometry("800x500")
    root.mainloop()


def HomeApp():
    mainframe = Tk()
    mainframe.title("Quiz Application")
    mainframe.geometry("800x500")

    menubar = Menu(mainframe)
    file = Menu(menubar, tearoff=0)
    file.add_command(label="New", command=displayQuestions)
    file.add_command(label="Open")
    file.add_command(label="Save")
    file.add_command(label="Save as...")
    file.add_command(label="Close")

    file.add_separator()

    file.add_command(label="Exit", command=mainframe.quit)

    menubar.add_cascade(label="File", menu=file)
    edit = Menu(menubar, tearoff=0)
    edit.add_command(label="Undo")

    edit.add_separator()

    edit.add_command(label="Cut")
    edit.add_command(label="Copy")
    edit.add_command(label="Paste")
    edit.add_command(label="Delete")
    edit.add_command(label="Select All")

    menubar.add_cascade(label="Edit", menu=edit)
    help = Menu(menubar, tearoff=0)
    help.add_command(label="About")
    menubar.add_cascade(label="Help", menu=help)

    mainframe.config(menu=menubar)

    Label(mainframe, text='Quiz Application', font=(
        "Helvetica", 18), fg="black").pack(side=TOP, pady=10)

    B = Button(text="Start")
    B.place(x=500, y=10)

    mainframe.mainloop()

# Start Test Method


def testMethod():
    root = Tk()
    root.title('Test')
    root.geometry("800x500")
    root.mainloop()

# End Test Method


def Operations():
    pass


nextQuestion = 1

def displayQuestions():
    root = Tk()
    root.title('Display Quiz Questions')
    root.geometry("800x500")

    data = {
        0 : ("What is the output of the following code : \nprint type(type(int))", 'type "int"', 'type "type"', 'Error', '0', '2'),
        1 : ("What is the output of the following code :\nL = ['a','b','c','d']", 'Error', 'None', 'abcd', '[‘a’,’b’,’c’,’d’]', '3'),
        2 : ("What is the output of the following segment :\nchr(ord('A'))", 'A', 'B', 'a', 'Error', '1'),
    }

    Label(root, text='Question 1. ', font=(
        "Helvetica", 15), fg="black").place(x=20, y=10)

    def clicked(event):
        # event.x = event.x + 1
        global nextQuestion
        nextQuestion = nextQuestion+1
        # label1.configure(text=f'Button was clicked {event.x} times!!!')
        print("Button was clicked %d times!!!"%(nextQuestion))
        print("nextQuestion is ",nextQuestion)
        # Question No.
        Label(root, text='Question %d. '%nextQuestion, font=(
        "Helvetica", 15), fg="black").place(x=20, y=10)

    countRightAnswer = 0

    questionText = ""
    disp_op1 = ""
    disp_op2 = ""
    disp_op3 = ""
    disp_op4 = ""

    for question_no, (QuestionText, op1, op2, op3, op4, ans) in data.items():
        if question_no == 1:
            questionText = QuestionText
            disp_op1 = op1
            disp_op2 = op2
            disp_op3 = op3
            disp_op4 = op4

    # Question in textarea
    text = Text(root, height=5, width=700, font=("Helvetica", 13))
    scroll = Scrollbar(root, command=text.yview)
    text.configure(yscrollcommand=scroll.set)
    text.insert(END, questionText)
    text.place(x=20, y=50)
    scroll.pack(side=RIGHT, fill=Y)

    # Question Options

    def selected():
        rightAns = ""
        wrongAns = ""
        clickAns = str(var.get())

        for question_no, (QuestionText, op1, op2, op3, op4, ans) in data.items():
            if question_no == 1:
                actualAns = ans
                if ans == clickAns:
                    rightAns = " Your Answer is correct !"
                    countRightQuestions = countRightAnswer + 1

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
        

    # Options list
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

    # Correct Answer
    rightAnslabel = Label(root, font=("Helvetica", 13), fg="green")
    rightAnslabel.place(x=20, y=360)

    wrongAnslabel = Label(root, font=("Helvetica", 13), fg="red")
    wrongAnslabel.place(x=20, y=360)

    actualAnslabel = Label(root, font=("Helvetica", 13), fg="green")
    actualAnslabel.place(x=20, y=380)



    B = Button(text="Next")
    B.bind("<Button-1>", clicked)
    B.place(x=20, y=420)


    # display total number of right answer is countRightAnswer
    root.mainloop()


    



displayQuestions()
