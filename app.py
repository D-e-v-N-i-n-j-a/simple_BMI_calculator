from pydoc import text
from tkinter import *
from tkinter import font
import sqlite3


class BMI_CALCULATOR:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI CALCULATOR")
        self.root.geometry("500x800")
        # CALCUALTE
        def calculate():
            userName = usernameVariable.get()
            age = ageVariable.get()
            weight = int(weightVariable.get())
            height = int(heightVariable.get())
            getUnit = clicked.get()
            convertHieght = height/100
            if getUnit == OPTIONS[0]:
                result = weight/convertHieght
                print(round(result, 2))
                if result > 30.00:
                    outcome = Label(labelFrame, text="Hello " + userName + ' ' + 'you weighed ' + str(round(result, 2)) + "kg/m²\n " +
                                    'you are obessed' + ' ' + "You need to see your doctor\n and exercise regularly to reduce weight").grid(row=1, column=1)
                elif result < 18.50:
                    outcome = Label(
                        self.root, text="You are underweight and you need to take more food to gain weight")

            elif getUnit == OPTIONS[1]:
                result = (weight/height)
                print(round(result, 2))

        # VARIABLES
        usernameVariable = StringVar()
        ageVariable = StringVar()
        weightVariable = StringVar()
        heightVariable = StringVar()
        clicked = StringVar()
        clicked.set("SELECT UNIT")
        OPTIONS = ["KG(Killogram)", "Ib(Pounds)"]
        # LABEL
        label = Label(self.root, text="CALCULATE YOUR BMI HERE", font=(
            "Gloudy old style", 25, "bold")).place(x=45, y=50)

        # USERNAME
        username = Label(self.root, text="Username", font=(
            "Gloudy old style", 15, "bold")).place(x=45, y=120)
        # usernameEntry
        usernameEntry = Entry(
            self.root, textvariable=usernameVariable, bg="#E7E6E6", width=30)
        usernameEntry.place(x=150, y=120)
        usernameEntry.insert(0, "Enter your name")

        # USER-AGE
        userAge = Label(self.root, text="Age", font=(
            "Gloudy old style", 15, "bold")).place(x=45, y=170)
        userAgeEntry = Entry(
            self.root, textvariable=ageVariable, bg="#E7E6E6", width=30)
        userAgeEntry.place(x=150, y=170)
        userAgeEntry.insert(0, "Enter your age")

        # WEIGHT HERE
        userWeight = Label(self.root, text="Weight", font=(
            "Gloudy old style", 15, "bold",)).place(x=45, y=220)
        userWightEntry = Entry(
            self.root, textvariable=weightVariable, bg="#E7E6E6", width=30).place(x=150, y=220)
        # HEIGHT
        userHeight = Label(self.root, text="Height", font=(
            "Gloudy old style", 15, "bold",)).place(x=45, y=270)
        userHeightEntry = Entry(
            self.root, textvariable=heightVariable, bg="#E7E6E6", width=30).place(x=150, y=270)
        # UNIT
        unit = Label(self.root, text="Unit", font=(
            "Gloudy old style", 15, "bold",)).place(x=45, y=320)
        dropDown = OptionMenu(
            self.root, clicked, *OPTIONS,).place(x=150, y=320)

        # BUTTON
        calculate = Button(self.root, text="CALCULATE BMI", command=calculate,
                        bg="blue", fg="black", width=30, height=3).place(x=150, y=360)

        # RESULTS HERE
        resultLabel = Label(self.root, text="RESULT", font=(
            "Gloudy old style", 25, "bold")).place(x=45, y=420)

        # RESULT FRAME
        labelFrame = Frame(self.root, width=400, height=200,
                        bg="blue", bd=5)
        labelFrame.place(x=45, y=470)


root = Tk()

obj = BMI_CALCULATOR(root)

root.mainloop()
