from tkinter import *
from math import *

root = Tk()
root.title("PyCalc")
root.config(bg='red')

e = Entry(root, width=24, borderwidth=5, bg='grey', fg='white', font='Helvetica 20',)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_click(num):
    current = e.get()

    # Replace String
    e.delete(0, END)
    e.insert(0, str(current) + str(num))

def button_equal():
    current = e.get()
    answer = eval(current)

    # Replace String
    e.delete(0, END)
    e.insert(0, str(current) + '=' + str(answer))

def button_clear():
    e.delete(0, END)

def button_delete():
    current = e.get()

    # Delete up to the '=' if it is present
    if -1 != current.find('='):

        # Cut string off at '='
        index = current.find('=')
        current = current[:index]

        # Replace String
        e.delete(0, END)
        e.insert(0, current)
        
    else:
        e.delete(len(current)-1, END)

def E():
    current = e.get()
    e.delete(0, END)
    e.insert(0, current + '*10**')

def binary():
    current = e.get()

    # Check if equals was left in input string
    if -1 != current.find('='):

        # Cut string off at '='
        index = current.find('=')
        current = current[:index]

    answer = bin(int(eval(current)))
    e.delete(0, END)
    e.insert(0, current + '=' + str(answer))

def hexadecimal():
    current = e.get()

    # Check if equals was left in input string
    if -1 != current.find('='):
        
        #cut string off at '='
        index = current.find('=')
        current = current[:index]
        
    answer = hex(int(eval(current)))
    e.delete(0, END)
    e.insert(0, current + '=' + str(answer))

def squareroot():
    current = e.get()

    # Check if equals was left in input string
    if -1 != current.find('='):
        
        # Cut string off at '='
        index = current.find('=')
        current = current[:index]

    current = ("sqrt(" + current + ")")
    answer = str(eval(current))

    # Find decimal and round to 5 decimal places
    index = answer.find('.') + 6
    answer = answer[:index]
    
    e.delete(0, END)
    e.insert(0, current + '=' + str(answer))
    
    
# Define buttons
button_0 = Button(root, text="0", padx=30, pady=6, bg='grey', fg='white', font='Helvetica 20', command=lambda: button_click('0'))
button_1 = Button(root, text="1", padx=30, pady=6, bg='grey', fg='white', font='Helvetica 20', command=lambda: button_click('1'))
button_2 = Button(root, text="2", padx=30, pady=6, bg='grey', fg='white', font='Helvetica 20', command=lambda: button_click('2'))
button_3 = Button(root, text="3", padx=30, pady=6, bg='grey', fg='white', font='Helvetica 20', command=lambda: button_click('3'))
button_4 = Button(root, text="4", padx=30, pady=6, bg='grey', fg='white', font='Helvetica 20', command=lambda: button_click('4'))
button_5 = Button(root, text="5", padx=30, pady=6, bg='grey', fg='white', font='Helvetica 20', command=lambda: button_click('5'))
button_6 = Button(root, text="6", padx=30, pady=6, bg='grey', fg='white', font='Helvetica 20', command=lambda: button_click('6'))
button_7 = Button(root, text="7", padx=30, pady=6, bg='grey', fg='white', font='Helvetica 20', command=lambda: button_click('7'))
button_8 = Button(root, text="8", padx=30, pady=6, bg='grey', fg='white', font='Helvetica 20', command=lambda: button_click('8'))
button_9 = Button(root, text="9", padx=30, pady=6, bg='grey', fg='white', font='Helvetica 20', command=lambda: button_click('9'))
button_dec = Button(root, text=".", padx=30, pady=6, bg='grey', fg='white', font='Helvetica 20', command=lambda: button_click('.'))
button_add = Button(root, text="+", padx=30, pady=6, bg='grey', fg='white', font='Helvetica 20', command=lambda: button_click('+'))
button_subtract = Button(root, text="-", padx=30, pady=6, bg='grey', fg='white', font='Helvetica 20', command=lambda: button_click('-'))
button_divide = Button(root, text="/", padx=30, pady=6, bg='grey', fg='white', font='Helvetica 20', command=lambda: button_click('/'))
button_multply = Button(root, text="*", padx=30, pady=6, bg='grey', fg='white', font='Helvetica 20', command=lambda: button_click('*'))
button_openpar = Button(root, text="(", padx=30, pady=6, bg='grey', fg='white', font='Helvetica 20', command=lambda: button_click('('))
button_closepar = Button(root, text=")", padx=30, pady=6, bg='grey', fg='white', font='Helvetica 20', command=lambda: button_click(')'))
button_equal = Button(root, text="=", padx=73, pady=6, bg='red', fg='white', font='Helvetica 20', command=button_equal)
button_clr = Button(root, text="Clear", padx=30, pady=6, bg='orange', fg='white', font='Helvetica 20', command=button_clear)
button_del = Button(root, text="Del", padx=30, pady=6, bg='orange', fg='white', font='Helvetica 20', command=button_delete)
button_E = Button(root, text="E", padx=30, pady=6, bg='grey', fg='white', font='Helvetica 20', command=E)
button_binary = Button(root, text="Binary", padx=30, pady=6, bg='grey', fg='white', font='Helvetica 20', command=binary)
button_hexadecimal = Button(root, text="Hex", padx=30, pady=6, bg='grey', fg='white', font='Helvetica 20', command=hexadecimal)
button_sqrt = Button(root, text="\u221A \u0305", padx=30, pady=6, bg='grey', fg='white', font='Helvetica 20', command=squareroot)
button_pi = Button(root, text="\u03C0", padx=30, pady=6, bg='grey', fg='white', font='Helvetica 20', command=lambda: button_click('\u03C0'))

# Put buttons on screen
# Row 1
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_add.grid(row=1, column=3)

button_7.config(height=1, width=2)
button_8.config(height=1, width=2)
button_9.config(height=1, width=2)
button_add.config(height=1, width=2)

# Row 2
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_subtract.grid(row=2, column=3)

button_4.config(height=1, width=2)
button_5.config(height=1, width=2)
button_6.config(height=1, width=2)
button_subtract.config(height=1, width=2)

# Row 3
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_multply.grid(row=3, column=3)

button_1.config(height=1, width=2)
button_2.config(height=1, width=2)
button_3.config(height=1, width=2)
button_multply.config(height=1, width=2)

# Row 4
button_0.grid(row=4, column=0)
button_dec.grid(row=4, column=1)
button_E.grid(row=4, column=2)
button_divide.grid(row=4, column=3)

button_0.config(height=1, width=2)
button_dec.config(height=1, width=2)
button_E.config(height=1, width=2)
button_divide.config(height=1, width=2)

# Row 5
button_sqrt.grid(row=5, column=0)
button_pi.grid(row=5, column=1)

button_sqrt.config(height=1, width=2)
button_pi.config(height=1, width=2)

# Row 6
button_binary.grid(row=6, column=0)
button_hexadecimal.grid(row=6, column=1)
button_openpar.grid(row=6, column=2)
button_closepar.grid(row=6, column=3)

button_openpar.config(height=1, width=2)
button_closepar.config(height=1, width=2)
button_binary.config(height=1, width=2)
button_hexadecimal.config(height=1, width=2)


# Row 7
button_del.grid(row=7, column=0)
button_clr.grid(row=7, column=1)
button_equal.grid(row=7, column=2, columnspan=2)

button_del.config(height=1, width=2)
button_clr.config(height=1, width=2)
button_equal.config(height=1, width=3)

root.mainloop()
