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

        for F in (HomePage, StartQuiz, PageTwo):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Play Quiz", font=LARGE_FONT)
        label.pack(pady=20,padx=10)

        name = tk.Label(self, text="Full Name")
        name.pack()
        name_TextF = tk.Entry(self, bd =5)
        name_TextF.pack()

        roll_no = tk.Label(self, text="Roll No.")
        roll_no.pack()
        roll_no_TextF = tk.Entry(self, bd =5)
        roll_no_TextF.pack()

        email = tk.Label(self, text="Email Address")
        email.pack()
        email_TextF = tk.Entry(self, bd =5)
        email_TextF.pack()


        button2 = tk.Button(self, text="Start Now",
                            command=lambda: controller.show_frame(StartQuiz))
        button2.pack(pady=20,padx=10)


class StartQuiz(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.components()
        self.count = 0
        
        
    def components(self):
        data = {
            1 : ("What is the output of the following code : \nprint type(type(int))", 'type "int"', 'type "type"', 'Error', '0', '2'),
            2 : ("What is the output of the following code :\nL = ['a','b','c','d']", 'Error', 'None', 'abcd', '[‘a’,’b’,’c’,’d’]', '3'),
            3 : ("What is the output of the following segment :\nchr(ord('A'))", 'A', 'B', 'a', 'Error', '1'),
            4 : ("What is the output of the following code :\nL = ['a','b','c','d']", 'Error', 'None', 'abcd', '[‘a’,’b’,’c’,’d’]', '3'),
            5 : ("What is the output of the following segment :\nchr(ord('A'))", 'A', 'B', 'a', 'Error', '1'),
            6 : ("What is the output of the following code :\nL = ['a','b','c','d']", 'Error', 'None', 'abcd', '[‘a’,’b’,’c’,’d’]', '3'),
            7 : ("What is the output of the following segment :\nchr(ord('A'))", 'A', 'B', 'a', 'Error', '1'),
        }
        for question_no, (QuestionText, op1, op2, op3, op4, ans) in data.items():
            if question_no == 3:
                q_no = question_no
                questionText = QuestionText
                disp_op1 = op1
                disp_op2 = op2
                disp_op3 = op3
                disp_op4 = op4
                actualAns = ans
        question_no = tk.Label(self, text="Question %d"%q_no, font=LARGE_FONT)
        question_no.pack(pady=10,padx=10)

        question = tk.Label(self, text=questionText, font=LARGE_FONT)
        question.pack(pady=20,padx=10)

        def selectedOption(): 
            points = 0
            clickAns = str(var.get())
            if clickAns == '1':
                if actualAns == '1':
                    points+=1
            elif clickAns == '2':
                if actualAns == '2':
                    points+=1
            elif clickAns == '3':
                if actualAns == '3':
                    points+=1
            else:
                if actualAns == '4':
                    points+=1

        var = tk.IntVar()

        R1 = tk.Radiobutton(self, text=disp_op1, font=("Helvetica", 10), variable=var, value=1, command=selectedOption)
        R1.pack()

        R2 = tk.Radiobutton(self, text=disp_op2, font=("Helvetica", 10), variable=var, value=2, command=selectedOption)
        R2.pack()

        R3 = tk.Radiobutton(self, text=disp_op3, font=("Helvetica", 10), variable=var, value=3, command=selectedOption)
        R3.pack()

        R4 = tk.Radiobutton(self, text=disp_op4, font=("Helvetica", 10), variable=var, value=4, command=selectedOption)
        R4.pack()


        button2 = tk.Button(self, text="Next",command=self.nextQuestion)
        button2.pack(pady=20,padx=10) 


    def nextQuestion(self):
        self.count+=1
        print(self.count)
        return self.count


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(HomePage))
        button1.pack()

        button2 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()
        


app = SeaofBTCapp()
app.geometry("450x350")
app.title("Quiz APP")
app.mainloop()