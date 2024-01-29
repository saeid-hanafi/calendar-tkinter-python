from tkinter import *
import calendar

app = Tk()
app.title('Calender')
app.geometry('600x600')
app.resizable(False, False)
canvas = Canvas(app, width=600, height=600, bg="cyan")
canvas.pack(fill=BOTH, expand=1)

month = Label(app, text="Month", bg="cyan", fg="white", font=("Arial", 15, "bold"))
month.place(x=100, y=100)

monthVal = DoubleVar()
monthInput = Spinbox(app, textvariable=monthVal, from_=1, to=12, font=("Arial", 15, "bold"), width=5, justify=CENTER)
monthInput.place(x=170, y=100)
monthInput.delete(0, "end")


year = Label(app, text="Year", bg="cyan", fg="white", font=("Arial", 15, "bold"))
year.place(x=350, y=100)

yearVal = DoubleVar()
yearInput = Spinbox(app, textvariable=yearVal, from_=2024, to=2050, font=("Arial", 15, "bold"), width=5, justify=CENTER)
yearInput.place(x=420, y=100)
yearInput.delete(0, "end")


cal = Text(app, font=("Arial", 15, "bold"), width=36, height=15)
cal.place(x=100, y=150)


def get_cal():
    m = int(monthVal.get())
    y = int(yearVal.get())
    calVal = calendar.month(y, m)
    cal.delete("1.0", "end")
    cal.insert(END, str(calVal))


btn = Button(app, text="Get Calendar", font=("Arial", 20, "bold"), bg="#FF1921", fg="white", command=get_cal)
btn.place(x=200, y=520)

app.mainloop()
