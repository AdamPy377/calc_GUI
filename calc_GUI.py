import tkinter as tk

# create a function, at end of button say command = func name to use the function when executed

Operator = ""
first = ""
second = ""
Position = "First"
TotalNumber = ""
# to prevent variables being undefined

# the operator functions just set what operator is being used and change the input value for the second number
# rather than the first, also update the label at top to display the first number
def Add():
    global Operator, Position
    Operator = "Addition"
    Position = "Second"
    label1["text"] = first
    NumbersEnabled()


def Subtract():
    global Operator, Position
    Operator = "Subtraction"
    Position = "Second"
    label1["text"] = first
    NumbersEnabled()


def Multiply():
    global Operator, Position
    Operator = "Multiplication"
    Position = "Second"
    label1["text"] = first
    NumbersEnabled()


def Divide():
    global Operator, Position
    Operator = "Division"
    Position = "Second"
    label1["text"] = first
    NumbersEnabled()


def NumbersDisabled():
    button0["state"] = "disabled"
    button1["state"] = "disabled"
    button2["state"] = "disabled"
    button3["state"] = "disabled"
    button4["state"] = "disabled"
    button5["state"] = "disabled"
    button6["state"] = "disabled"
    button7["state"] = "disabled"
    button8["state"] = "disabled"
    button9["state"] = "disabled"


def NumbersEnabled():
    button0["state"] = "normal"
    button1["state"] = "normal"
    button2["state"] = "normal"
    button3["state"] = "normal"
    button4["state"] = "normal"
    button5["state"] = "normal"
    button6["state"] = "normal"
    button7["state"] = "normal"
    button8["state"] = "normal"
    button9["state"] = "normal"

def NumberClicked(number, position):
    # sets the number depending on what has been clicked
    buttonDivide["state"] = "normal"
    buttonMultiply["state"] = "normal"
    buttonSubtract["state"] = "normal"
    buttonPlus["state"] = "normal"
    global first, second, TotalNumber

    TotalNumber += str(number)
    if position == "Second":
        second += TotalNumber
        TotalNumber = ""
    else:
        first += TotalNumber
        TotalNumber = ""


def ClearCalc():
    global first, second, TotalNumber, Operator, Position
    NumbersEnabled()
    label1["text"] = "0"
    TotalNumber = ""
    second = ""
    first = ""
    Operator = ""
    Position = "First"


def Equals(Chosen, NumberOne, NumberTwo):
    # evaluates the equation entered by the user
    global first, second, TotalNumber, Operator
    NumbersDisabled()

    outcome = 0
    if (Chosen == "Addition"):
        outcome = float(NumberOne) + float(NumberTwo)
        first = outcome
    if (Chosen == "Subtraction"):
        outcome = float(NumberOne) - float(NumberTwo)
        first = outcome
    if (Chosen == "Multiplication"):
        outcome = float(NumberOne) * float(NumberTwo)
        first = outcome
    try:
        if (Chosen == "Division"):
            outcome = float(NumberOne) / float(NumberTwo)
            first = outcome
    except ZeroDivisionError: # for division by Zero error, sets screen to 0 rather than undefined check **
        label1["text"] = "Undefined"


    label1["text"] = outcome
    # resets the variables
    second = ""
    TotalNumber = ""
    Operator = ""


# creates the window
window = tk.Tk()
window.geometry("500x650")
window.title("Calculator")

# creates the label and all the buttons
label1 = tk.Label(window, text="0", width=55, height=6, bg="Grey", anchor="se", font=("ArialBold"))
label1.grid(row=0, column=0, columnspan=4, sticky="nsew")

button0 = tk.Button(window, text="0", width=8, height=3, command=lambda: NumberClicked(0, Position))
button0.grid(row=1, column=0, sticky="nsew")

button1 = tk.Button(window, text="1", width=8, height=3, command=lambda: NumberClicked(1, Position))
button1.grid(row=2, column=0, sticky="nsew")

button2 = tk.Button(window, text="2", width=8, height=3, command=lambda: NumberClicked(2, Position))
button2.grid(row=3, column=0, sticky="nsew")

button3 = tk.Button(window, text="3", width=8, height=3, command=lambda: NumberClicked(3, Position))
button3.grid(row=4, column=0, sticky="nsew")

button4 = tk.Button(window, text="4", width=8, height=3, command=lambda: NumberClicked(4, Position))
button4.grid(row=1, column=1, sticky="nsew")

button5 = tk.Button(window, text="5", width=8, height=3, command=lambda: NumberClicked(5, Position))
button5.grid(row=2, column=1, sticky="nsew")

button6 = tk.Button(window, text="6", width=8, height=3, command=lambda: NumberClicked(6, Position))
button6.grid(row=3, column=1, sticky="nsew")

button7 = tk.Button(window, text="7", width=8, height=3, command=lambda: NumberClicked(7, Position))
button7.grid(row=4, column=1, sticky="nsew")

button8 = tk.Button(window, text="8", width=8, height=3, command=lambda: NumberClicked(8, Position))
button8.grid(row=1, column=2, sticky="nsew")

button9 = tk.Button(window, text="9", width=8, height=3, command=lambda: NumberClicked(9, Position))
button9.grid(row=2, column=2, sticky="nsew")

buttonPlus = tk.Button(window, state="disabled", text="+", width=8, height=3, command=Add)
buttonPlus.grid(row=3, column=2, sticky="nsew")

buttonSubtract = tk.Button(window, state="disabled", text="-", width=8, height=3, command=Subtract)
buttonSubtract.grid(row=3, column=3, sticky="nsew")

buttonMultiply = tk.Button(window, state="disabled", text="*", width=8, height=3, command=Multiply)
buttonMultiply.grid(row=1, column=3, sticky="nsew")

buttonDivide = tk.Button(window, state="disabled", text="/", width=8, height=3, command=Divide)
buttonDivide.grid(row=2, column=3, sticky="nsew")

buttonEquals = tk.Button(window, text="=", width=8, height=3, command=lambda: Equals(Operator, first, second))
buttonEquals.grid(row=4, column=2, columnspan=2, sticky="nsew")

buttonClear = tk.Button(window, text="Clear Calculator", width=8, height=3, command=ClearCalc)
buttonClear.grid(row=5, columnspan=4, column=0, sticky="nsew")


window.mainloop()
