# Kg to other metric convertors #
# It will convert in Gram,      #
# Pound and Ounces.             #
from tkinter import *

window = Tk()

def kg_to_gpo():
    gram = float(e2_value.get()) * 1000
    t1.delete("1.0", END)
    t1.insert(END, gram)

    pound = float(e2_value.get()) * 2.20
    t2.delete("1.0", END)
    t2.insert(END, pound)

    ouz = float(e2_value.get()) * 35.27
    t3.delete("1.0", END)
    t3.insert(END, ouz)

e1 = Label(window, text = "Kg")
e1.grid(row = 0, column = 0)

e2_value = StringVar()
e2 = Entry(window, textvariable = e2_value)
e2.grid(row = 0, column = 1)

b1 = Button(window, text = "Convert", command = kg_to_gpo)
b1.grid(row = 0, column = 2)

e1_g = Label(window, text = "Gram")
e1_g.grid(row = 1, column = 0)

t1 = Text(window, height = 1, width = 10)
t1.grid(row = 2, column = 0)

e1_p = Label(window, text = "Pound")
e1_p.grid(row = 1, column = 1)

t2 = Text(window, height = 1, width = 10)
t2.grid(row = 2, column = 1)

e1_o = Label(window, text = "Ounce")
e1_o.grid(row = 1, column = 2)

t3 = Text(window, height = 1, width = 10)
t3.grid(row = 2, column = 2)

window.mainloop()