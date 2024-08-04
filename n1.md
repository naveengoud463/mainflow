```python
from tkinter import *
from PIL import ImageTK,Image

def init__calculator():
    rt = TK()
    rt.title("basic calculator")

    rt.iconbitmap("C:\\Users\\karne\\Downloads\\Calc-icon.ico")
    rt.geometry("300x430")

    bg = ImageTK.PhotoImage(file="C:\\Users\\karne\\Downloads\\300x430_background.png")
    bg_label = Label(rt, image=bg)
    bg_label.place(x=0, y=0)

    e = Entry(rt,width=35, borderwidth=10, font=("Times", 10))
    e.grid(row=0, column=0, pady=20, padx=30, columnspan=3)

    images = {
        "1": ImageTK.PhotoImage(file="C:\\Users\\karne\\Downloads\\1 (1).png"),
        "2": ImageTK.PhotoImage(file="C:\\Users\\karne\\Downloads\\2.png"),
        "3": ImageTK.PhotoImage(file="C:\\Users\\karne\\Downloads\\3.png"),
        "4": ImageTK.PhotoImage(file="C:\\Users\\karne\\Downloads\\4.png"),
        "5": ImageTK.PhotoImage(file="C:\\Users\\karne\\Downloads\\5.png"),
        "6": ImageTK.PhotoImage(file="C:\\Users\\karne\\Downloads\\6.png"),
        "7": ImageTK.PhotoImage(file="C:\\Users\\karne\\Downloads\\7.png"),
        "8": ImageTK.PhotoImage(file="C:\\Users\\karne\\Downloads\\8.png"),
        "9": ImageTK.PhotoImage(file="C:\\Users\\karne\\Downloads\\9.png"),
        "0": ImageTK.PhotoImage(file="C:\\Users\\karne\\Downloads\\10.png"),
        "+": ImageTK.PhotoImage(file="C:\\Users\\karne\\Downloads\\11.png"),
        "-": ImageTK.PhotoImage(file="C:\\Users\\karne\\Downloads\\12.png"),
        "*": ImageTK.PhotoImage(file="C:\\Users\\karne\\Downloads\\13.png"),
        "/": ImageTK.PhotoImage(file="C:\\Users\\karne\\Downloads\\14.png"),
        "=": ImageTK.PhotoImage(file="C:\\Users\\karne\\Downloads\\15.png"),
        "C": ImageTK.PhotoImage(file="C:\\Users\\karne\\Downloads\\16.png"),
    }
    def button_click(number):
        current = e.get()
        e.delete(0,END)
        e.insert(0, str(current) + str(number))

    def buttton_add():
        first_number = e.get()
        global f_num
        global maths
        maths = "addition"
        f_num = int(first_number)
        e.delete(0, END)
    def buttton_sub():
        first_number = e.get()
        global f_num
        global maths
        maths = "subtraction"
        f_num = int(first_number)
        e.delete(0, END)
    def buttton_div():
        first_number = e.get()
        global f_num
        global maths
        maths = "division"
        f_num = int(first_number)
        e.delete(0, END)
    def buttton_mult():
        first_number = e.get()
        global f_num
        global maths
        maths = "multiplication"
        f_num = int(first_number)
        e.delete(0, END)
    def button_equals():
        second_number = e.get()
        e.delete(0, END)

        if maths == "addition":
            e.insert(0, f_num + int(second_number))
        if maths == "subtraction":
            e.insert(0, f_num - int(second_number))
        if maths == "multiplication":
            e.insert(0, f_num * int(second_number))
        if maths == "division":
            e.insert(0, f_num / int(second_number))
    def button_clear():
        e.delete(0, END)

    buttons = {
        "1": (1, 0, lambda: button_click(1)),
        "2": (1, 1, lambda: button_click(2)),
        "3": (1, 2, lambda: button_click(3)),
        "4": (2, 0, lambda: button_click(4)),
        "5": (2, 1, lambda: button_click(5)),
        "6": (2, 2, lambda: button_click(6)),
        "7": (3, 0, lambda: button_click(7)),
        "8": (3, 1, lambda: button_click(8)),
        "9": (3, 2, lambda: button_click(9)),
        "0": (4, 1, lambda: button_click(0)),
        "+": (4, 2, button_add),
        "-": (4, 0, button_sub),
        "*": (5, 1, button_mult),
        "/": (5, 0, button_div),
        "=": (5, 2, button_equals),
        "C": (6, 1, button_clear),

    }
    for btn, (row, col, cmd) in buttons.items():
        Button(rt, border="3", image=images[btn], command=cmd).grid(row=row, column=col)
    rt.images = images
    rt.mainloop()
init__calculator()


```


    ---------------------------------------------------------------------------

    ImportError                               Traceback (most recent call last)

    Cell In[3], line 2
          1 from tkinter import *
    ----> 2 from PIL import ImageTK,Image
          4 def init__calculator():
          5     rt = TK()
    

    ImportError: cannot import name 'ImageTK' from 'PIL' (C:\Users\karne\AppData\Local\Programs\Python\Python312\Lib\site-packages\PIL\__init__.py)



```python

```
