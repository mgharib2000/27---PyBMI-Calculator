from tkinter import *
from tkinter import messagebox

def calc():
    kg = int(weight_text.get())
    m = float(height_text.get())
    bmi = kg/(m**2)
    bmi = round(bmi, 1)
    messagebox.showinfo("Your BMI is ", bmi)

app = Tk()
app.title("PyBMI")
app.geometry("260x100")
app.config(bg="GREY")

height_label = Label(app, text="Enter height in metres: ")
height_label.grid(row=0, column=1, padx=1, pady=1, sticky="EW")

weight_label = Label(app, text="Enter weight in kg: ")
weight_label.grid(row=1, column=1, padx=1, pady=1, sticky="EW")

height_text = Entry(app)
height_text.grid(row=0, column=2, padx=1, pady=1, sticky="EW")

weight_text = Entry(app)
weight_text.grid(row=1, column=2, padx=1, pady=1, sticky="EW")


calc_button = Button(app, text="Calculate", command=calc)
calc_button.grid(row=2, column=1, padx=1, pady=1, sticky="EW")

quit_button = Button(app, text="Quit", command=app.destroy)
quit_button.grid(row=2, column=2, padx=1, pady=1, sticky="EW")


app.mainloop()
