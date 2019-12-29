from tkinter import *
from tkinter.font import Font
from list import *
import tkinter.messagebox

root = Tk()
root.title('Quiz')
bg = PhotoImage(file="c.png")
w = bg.width()
h = bg.height()


myfont2= Font(family="Times New Roman", weight="bold", size=17)

#this method is executed when 'Yes' button is pressed
def ExecuteYes(b_id):
    f = open("answers.txt", "r")
    while f.tell() <= 58:
        if f.read(2) == b_id:
            f.seek(f.tell()+1)
            if f.read(1) == '1':
                Correct()
            else:
                Wrong()
        else:
            f.seek(f.tell()+4)
    f.close()

#this method is executed when 'No' button is pressed
def ExecuteNo(b_id):
    f = open("answers.txt", "r")
    while f.tell() <= 58:
        if f.read(2) == b_id:
            f.seek(f.tell()+1)
            if f.read(1) == '0':
                Correct()
            else:
                Wrong()
        else:
            f.seek(f.tell()+4)
    f.close()

#this method is executed when the button pressed is the correct answer
def Correct():
    tkinter.messagebox.showinfo("Response", "Correct Answer!")

#this method is executed when the button pressed is the wrong answer
def Wrong():
    tkinter.messagebox.showinfo("Response", "Wrong Answer!")

def showExplanation():
    root2 = Tk()
    root2.title("Explanations!")
    root2.geometry("600x400+110+10")

    label_1 = Label(root2, text="3. He is 45th.", fg="gray10", font=myfont2)
    label_1.place(x=0, y=80)

    label_2 = Label(root2, text="4. Mount Everest is!", fg="gray10", font=myfont2)
    label_2.place(x=0, y=120)

    label_3 = Label(root2, text="7. Aram Shah was!", fg="gray10", font=myfont2)
    label_3.place(x=0, y=160)

    label_4 = Label(root2, text="8. NASA stands for National Aeronautics and Space Administration.", fg="gray10", font=myfont2)
    label_4.place(x=0, y=200)

    label_5 = Label(root2, text="9. Vatican City also has a square flag.", fg="gray10", font=myfont2)
    label_5.place(x=0, y=240)

    label_6 = Label(root2, text="10. 'Uncopyrightables' is longer!", fg="gray10", font=myfont2)
    label_6.place(x=0, y=280)


    root2.mainloop()

def EasyIndia():
    label_1 = Label(cv, text="INDIA QUIZ", fg="azure")

    label_2 = Label(cv, text="1. New Delhi is the capital of India. Yes or No?", fg="white", font=myfont2, bg="black", relief=SUNKEN)
    label_2.place(x=0, y=80)

    button_1 = Button(cv, text="Yes", command=lambda: ExecuteYes('q1'))
    button_1.place(x=900, y=80)

    button_2 = Button(cv, text="No", command=lambda: ExecuteNo('q1'))
    button_2.place(x=950, y=80)

    label_2 = Label(cv, text="2. The Sun rises in the West and sets in the East. Yes or No?", fg="white", bg="black",
                    font=myfont2, relief=SUNKEN)
    label_2.place(x=0, y=120)

    button_1 = Button(cv, text="Yes", command=lambda: ExecuteYes('q2'))
    button_1.place(x=900, y=120)

    button_2 = Button(cv, text="No", command=lambda: ExecuteNo('q2'))
    button_2.place(x=950, y=120)

    label_2 = Label(cv, text="3. Donald Trump is the 44th President of United States. Yes or No?", fg="white",
                    font=myfont2,bg="black", relief=SUNKEN)
    label_2.place(x=0, y=160)

    button_1 = Button(cv, text="Yes", command=lambda: ExecuteYes('q3'))
    button_1.place(x=900, y=160)

    button_2 = Button(cv, text="No", command=lambda: ExecuteNo('q3'))
    button_2.place(x=950, y=160)

    label_2 = Label(cv, text="4. Mount Kilimanjaro is the tallest mountain in the world. Yes or No?", fg="white", bg="black",
                    font=myfont2, relief=SUNKEN)
    label_2.place(x=0, y=200)

    button_1 = Button(cv, text="Yes", command=lambda: ExecuteYes('q4'))
    button_1.place(x=900, y=200)

    button_2 = Button(cv, text="No", command=lambda: ExecuteNo('q4'))
    button_2.place(x=950, y=200)

    label_2 = Label(cv, text="5. Spiders have six legs. Yes or No?", fg="white", font=myfont2, bg="black", relief=SUNKEN)
    label_2.place(x=0, y=240)

    button_1 = Button(cv, text="Yes", command=lambda: ExecuteYes('q5'))
    button_1.place(x=900, y=240)

    button_2 = Button(cv, text="No", command=lambda: ExecuteNo('q5'))
    button_2.place(x=950, y=240)

    label_2 = Label(root, text="6. An ostrich's eye is bigger than its brain. Yes or No?", fg="white", font=myfont2, bg="black", relief=SUNKEN)
    label_2.place(x=0, y=280)

    button_1 = Button(root, text="Yes", command=lambda: ExecuteYes('q6'))
    button_1.place(x=900, y=280)

    button_2 = Button(root, text="No", command=lambda: ExecuteNo('q6'))
    button_2.place(x=950, y=280)

    label_2 = Label(root, text="7. Iltutmish was the successor of Qutub-ud-din Aibak. Yes or No?", fg="white", bg="black",
                    font=myfont2, relief=SUNKEN)
    label_2.place(x=0, y=320)

    button_1 = Button(root, text="Yes", command=lambda: ExecuteYes('q7'))
    button_1.place(x=900, y=320)

    button_2 = Button(root, text="No", command=lambda: ExecuteNo('q7'))
    button_2.place(x=950, y=320)

    label_2 = Label(root, text="8. The first 'A' in NASA stands for Administration. Yes or No?", fg="white", bg="black",
                    font=myfont2, relief=SUNKEN)
    label_2.place(x=0, y=360)

    button_1 = Button(root, text="Yes", command=lambda: ExecuteYes('q8'))
    button_1.place(x=900, y=360)

    button_2 = Button(root, text="No", command=lambda: ExecuteNo('q8'))
    button_2.place(x=950, y=360)

    label_2 = Label(root, text="9. Switzerland is not the only country to have a square flag. Yes or No?", fg="white", bg="black",
                    font=myfont2, relief=SUNKEN)
    label_2.place(x=0, y=400)

    button_1 = Button(root, text="Yes", command=lambda: ExecuteYes('q9'))
    button_1.place(x=900, y=400)

    button_2 = Button(root, text="No", command=lambda: ExecuteNo('q9'))
    button_2.place(x=950, y=400)

    label_2 = Label(root, text="10. The longest word in English without any letter repeated is 'Copyrightables'. Yes or No?",
                    fg="white", bg="black", font=myfont2, relief=SUNKEN)
    label_2.place(x=0, y=440)

    button_1 = Button(root, text="Yes", command=lambda: ExecuteYes('q0'))
    button_1.place(x=900, y=440)

    button_2 = Button(root, text="No", command=lambda: ExecuteNo('q0'))
    button_2.place(x=950, y=440)

    explain_bttn = Button(root, text="Show Explanations", command=showExplanation)
    explain_bttn.place(x=888, y=480)

    Quit_bttn = Button(root, text="Quit", command=root.quit)
    Quit_bttn.place(x=925, y=520)




cv = Canvas(width=w, height=h)
cv.pack(side='top', fill='both', expand='yes')
cv.create_image(0, 0, image=bg, anchor='nw')

myfont=Font(family="Monotype Corsiva", weight="bold", size=60)

cv.create_text(520, 300, text="Welcome to Quiz!", anchor='n', fill="firebrick3", font=myfont)

menu = Menu(root)
root.config(menu=menu)

menu1=Menu(menu)
menu.add_cascade(label="India Quiz", menu=menu1)
menu1.add_command(label="Easy", command=EasyIndia)
menu1.add_command(label="Medium", command=EasyIndia)
menu1.add_command(label="Difficult", command=EasyIndia)

menu2=Menu(menu)
menu.add_cascade(label="World Quiz", menu=menu2)
menu2.add_command(label="Easy", command=EasyIndia)
menu2.add_command(label="Medium", command=EasyIndia)
menu2.add_command(label="Difficult", command=EasyIndia)

menu3=Menu(menu)
menu.add_cascade(label="Sports Quiz", menu=menu3)
menu3.add_command(label="Easy", command=EasyIndia)
menu3.add_command(label="Medium", command=EasyIndia)
menu3.add_command(label="Difficult", command=EasyIndia)

menu4=Menu(menu)
menu.add_cascade(label="Bollywood Quiz", menu=menu4)
menu4.add_command(label="Easy", command=EasyIndia)
menu4.add_command(label="Medium", command=EasyIndia)
menu4.add_command(label="Difficult", command=EasyIndia)

menu5=Menu(menu)
menu.add_cascade(label="Current Affairs Quiz", menu=menu5)
menu5.add_command(label="Easy", command=EasyIndia)
menu5.add_command(label="Medium", command=EasyIndia)
menu5.add_command(label="Difficult", command=EasyIndia)

menu6=Menu(menu)
menu.add_cascade(label="History Quiz", menu=menu6)
menu6.add_command(label="Easy", command=EasyIndia)
menu6.add_command(label="Medium", command=EasyIndia)
menu6.add_command(label="Difficult", command=EasyIndia)

myfont3= Font(weight="bold", size=8)
labl= Label(cv, text="Developed by ISHU RAJ", font=myfont3, fg="white", bg="black")
labl.pack(side=BOTTOM)

photo = PhotoImage(file="Prismatic-Question-Mark-Fractal-4-No-Background.gif")
lbl= Label(cv, image=photo, bg="black")
lbl.pack(side=BOTTOM)

root.geometry("%dx%d+110+10" % (w, h))
root.mainloop()