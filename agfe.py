import tkinter as tk
from datetime import date

def calculate_age():
    day = int(day_entry.get())
    month = int(month_entry.get())
    year = int(year_entry.get())
    today = date.today()
    age = today.year - year - ((today.month, today.day) < (month, day))
    result_label.config(text="your age is " + str(age))

win = tk.Tk()
win.title("age calculator")
win.geometry("300x200")

tk.Label(win, text="enter day").pack()
day_entry = tk.Entry(win)
day_entry.pack()

tk.Label(win, text="enter month").pack()
month_entry = tk.Entry(win)
month_entry.pack()

tk.Label(win, text="enter year").pack()
year_entry = tk.Entry(win)
year_entry.pack()

tk.Button(win, text="calculate age", command=calculate_age).pack()

result_label = tk.Label(win, text="")
result_label.pack()

win.mainloop()
