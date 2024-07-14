import tkinter

calculator = tkinter.Tk()

calculator.title("Calculator")
calculator.iconbitmap("icon.ico")
calculator.geometry("300x300")

#--------------------------------------------------------------------------
#Variables
num1 = tkinter.IntVar()
num2 = tkinter.IntVar()
answer = tkinter.StringVar()
check = tkinter.StringVar()
check.set(None)




#-----------------------------------------------------------------------------
#Entries
entry1 = tkinter.Entry(calculator, textvariable=num1)
entry1.pack()

entry2 = tkinter.Entry(calculator, textvariable=num2)
entry2.pack()

#----------------------------------------------------------------------------
#Functions

def calc():
    if check.get()=="add":
        result = num1.get() + num2.get()
        answer.set(f"Answer is \n{result}")
    elif check.get()=="sub":
        result = num1.get() - num2.get()
        answer.set(f"Answer is \n{result}")
    elif check.get()=="mul":
        result = num1.get() * num2.get()
        answer.set(f"Answer is \n{result}")
    elif check.get()=="div":
        result = num1.get() / num2.get()
        answer.set(f"Answer is \n{result}")
    else:
        answer.set("Please select a operator")



#----------------------------------------------------------------------------
#Radio Buttons
addition = tkinter.Radiobutton(calculator, text="+", value="add", variable=check)
addition.pack()

subtraction = tkinter.Radiobutton(calculator, text="-", value="sub", variable=check)
subtraction.pack()

multiplication = tkinter.Radiobutton(calculator, text="x", value="mul", variable=check)
multiplication.pack()

division = tkinter.Radiobutton(calculator, text="/", value="div", variable=check)
division.pack()



button = tkinter.Button(calculator, text="Calculate", command=calc)
button.pack()

label = tkinter.Label(calculator, textvariable=answer)
label.pack()


#Run(execute) the program
calculator.mainloop()