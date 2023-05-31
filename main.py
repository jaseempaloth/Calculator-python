from tkinter import *

window = Tk()
window.title("Calculator")
window.configure(bg="black")
value = ""
txt = StringVar()


def action_click(num):
    global value
    value = value + str(num)
    txt.set(value)


def action_result(val):
    try:
        global value
        res = str(eval(value))
        cris = value + " = " + res
        txt.set(cris)

    except ZeroDivisionError:
        txt.set("Zero Division Error")


def clear(_clear):
    global value
    value = ""
    txt.set("")


entry = Entry(window, textvariable=txt, bg="green", bd=5).grid(columnspan=10, padx=72, pady=120)

Button(window, text="7", padx=15, pady=15, font=("arial", 30, "bold"), command=lambda: action_click("7")).grid(row=2,
                                                                                                               column=0)
Button(window, text="8", padx=15, pady=15, font=("arial", 30, "bold"), command=lambda: action_click("8")).grid(row=2,
                                                                                                               column=1)
Button(window, text="9", padx=15, pady=15, font=("arial", 30, "bold"), command=lambda: action_click("9")).grid(row=2,
                                                                                                              column=2)
Button(window, text="+", padx=15, pady=15, font=("arial", 30, "bold"), command=lambda: action_click("+")).grid(row=2,
                                                                                                              column=3)

Button(window, text="4", padx=15, pady=15, font=("arial", 30, "bold"), command=lambda: action_click("4")).grid(row=3,
                                                                                                               column=0,
                                                                                                               pady=2)
Button(window, text="5", padx=15, pady=15, font=("arial", 30, "bold"), command=lambda: action_click("5")).grid(row=3,
                                                                                                             column=1)
Button(window, text="6", padx=15, pady=15, font=("arial", 30, "bold"), command=lambda: action_click("6")).grid(row=3,
                                                                                                             column=2)
Button(window, text="-", padx=15, pady=15, font=("arial", 30, "bold"), command=lambda: action_click("-")).grid(row=3,
                                                                                                             column=3)

Button(window, text="1", padx=15, pady=15, font=("arial", 30, "bold"), command=lambda: action_click("1")).grid(row=4,
                                                                                                             column=0)
Button(window, text="2", padx=15, pady=15, font=("arial", 30, "bold"), command=lambda: action_click("2")).grid(row=4,
                                                                                                             column=1)
Button(window, text="3", padx=15, pady=15, font=("arial", 30, "bold"), command=lambda: action_click("3")).grid(row=4,
                                                                                                             column=2)
Button(window, text="*", padx=15, pady=15, font=("arial", 30, "bold"), command=lambda: action_click("*")).grid(row=4,
                                                                                                             column=3)

Button(window, text="C", padx=15, pady=15, font=("arial", 30, "bold"), command=lambda: clear("c")).grid(row=5, column=0,
                                                                                                      pady=2)
Button(window, text="0", padx=15, pady=15, font=("arial", 30, "bold"), command=lambda: action_click("0")).grid(row=5,
                                                                                                             column=1)
Button(window, text="=", padx=15, pady=15, font=("arial", 30, "bold"), command=lambda: action_result("=")).grid(row=5,
                                                                                                              column=2)
Button(window, text="/", padx=15, pady=15, font=("arial", 30, "bold"), command=lambda: action_click("/")).grid(row=5,
                                                                                                             column=3)

window.mainloop()
