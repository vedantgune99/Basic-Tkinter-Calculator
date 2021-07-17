from tkinter import *

expression = " "


def press(n):
    global expression
    if n == "c":
        entryText.set(" ")
        expression = " "
    else:
        expression += n
        entryText.set(expression)


def calculate():
    global expression
    try:
        entryText.set(eval(expression))
    except:
        entryText.set("Unexpected Error!")


# Initial Window Design...
screen = Tk()
screen.geometry("439x378")
screen.title("Basic Calculator")
# screen.iconbitmap('calculator-icon.ico') - On windows you can use this .ico icon
entryText = StringVar()


# Display of calculator...
display = Frame(screen)
displayText = Entry(display, textvariable=entryText,
                    font="Gotham 27", width=17)
displayText.pack(pady=10)
display.pack(fill=X, side=TOP)


# Buttons grid of calculator...
# First Row of buttons.
buttonGrid1 = Frame(screen)
Button(buttonGrid1, text="C", fg="red", width=6, height=3, command=lambda: press("c")).pack(
    side=RIGHT, fill=X, padx=4, pady=4)

Button(buttonGrid1, text="/", width=6, height=3, command=lambda: press("/")).pack(
    side=RIGHT, fill=X, padx=4, pady=4)

Button(buttonGrid1, text="9", width=6, height=3, command=lambda: press("9")).pack(
    side=RIGHT, fill=X, padx=4, pady=4)

Button(buttonGrid1, text="8", width=6, height=3, command=lambda: press("8")).pack(
    side=RIGHT, fill=X, padx=4, pady=4)

Button(buttonGrid1, text="7", width=6, height=3, command=lambda: press("7")).pack(
    side=RIGHT, fill=X, padx=4, pady=4)
buttonGrid1.pack(fill=X, side=TOP, padx=10)


# Second Row of buttons.
buttonGrid2 = Frame(screen)
Button(buttonGrid2, text="%", width=6, height=3, command=lambda: press("/100*")).pack(
    side=RIGHT, fill=X, padx=4, pady=4)

Button(buttonGrid2, text="x", width=6, height=3, command=lambda: press("*")).pack(
    side=RIGHT, fill=X, padx=4, pady=4)

Button(buttonGrid2, text="6", width=6, height=3, command=lambda: press("6")).pack(
    side=RIGHT, fill=X, padx=4, pady=4)

Button(buttonGrid2, text="5", width=6, height=3, command=lambda: press("5")).pack(
    side=RIGHT, fill=X, padx=4, pady=4)

Button(buttonGrid2, text="4", width=6, height=3, command=lambda: press("4")).pack(
    side=RIGHT, fill=X, padx=4, pady=4)

buttonGrid2.pack(fill=X, side=TOP, padx=10)


# Third Row of buttons.
buttonGrid3 = Frame(screen)
Button(buttonGrid3, text="x²", width=6, height=3, command=lambda: press("**2")).pack(
    side=RIGHT, fill=X, padx=4, pady=4)

Button(buttonGrid3, text="-", width=6, height=3, command=lambda: press("-")).pack(
    side=RIGHT, fill=X, padx=4, pady=4)

Button(buttonGrid3, text="3", width=6, height=3, command=lambda: press("3")).pack(
    side=RIGHT, fill=X, padx=4, pady=4)

Button(buttonGrid3, text="2", width=6, height=3, command=lambda: press("2")).pack(
    side=RIGHT, fill=X, padx=4, pady=4)

Button(buttonGrid3, text="1", width=6, height=3, command=lambda: press("1")).pack(
    side=RIGHT, fill=X, padx=4, pady=4)

buttonGrid3.pack(fill=X, side=TOP, padx=10)


# Fourth (Zero's) Row.
buttonGrid4 = Frame(screen)
Button(buttonGrid4, text="=", bg="orange", width=6, height=3, command=calculate).pack(
    side=RIGHT, fill=X, padx=4, pady=4)

Button(buttonGrid4, text="+", width=6, height=3, command=lambda: press("+")).pack(
    side=RIGHT, fill=X, padx=4, pady=4)

Button(buttonGrid4, text=".", width=6, height=3, command=lambda: press(".")).pack(
    side=RIGHT, fill=X, padx=4, pady=4)

Button(buttonGrid4, text="0", width=17, height=3, command=lambda: press("0")).pack(
    side=RIGHT, fill=X, padx=4, pady=4)
buttonGrid4.pack(fill=X, side=TOP, padx=10)


screen.mainloop()
