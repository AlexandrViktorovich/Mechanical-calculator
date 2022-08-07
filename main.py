import tkinter
from tkinter import *
from tkinter import messagebox as msg

root = Tk()
root.configure(background='#464746')
root.geometry('280x426')
root.resizable(0,0)
root.title('Mechanical')

input_field = tkinter.Entry(root,justify=tkinter.RIGHT,font='Helvetica 21 bold')
input_field.place(x=0,y=0,width=280,height=78)
input_field.insert(0,"0")

def add_digit(number):
    value = input_field.get()
    if value[0:1] == "0" and len(value) == 1:
        value = value[1:]
    input_field.delete(0,tkinter.END)
    input_field.insert(0,value+str(number))

def operation(operator):
    value = input_field.get()
    if value[-1] in '-+*/':
        value = value[:-1]
    elif '+' in value or '-' in value or '/' in value or '*' in value:
        calculate()
        value = input_field.get()
    input_field.delete(0, tkinter.END)
    input_field.insert(0, value+operator)

def calculate():
    value=input_field.get()
    if value[-1] in '-+*/':
        operation = value[-1]
        value = value[:-1]+operation+value[:-1]
        #value=value+value[:-1]
    input_field.delete(0,tkinter.END)
    try:
        input_field.insert(0,eval(value))
    except NameError:
        msg.showinfo('Attention','You need to enter only numbers')
        input_field.insert(0, 0)
    except SyntaxError:
        msg.showinfo('Attention', 'You need to enter only numbers')
        input_field.insert(0, 0)
    except ZeroDivisionError:
        msg.showinfo('Attention', 'You can`t division by zero')
        input_field.insert(0, 0)

def clear():
    input_field.delete(0,tkinter.END)
    input_field.insert(0,'0')

def is_key(event):
    print(event.char)
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '-+*/':
        operation(event.char)
    if event.char == '\r':
        calculate()

root.bind('<Key>',is_key)

photo_1 = PhotoImage(file=r'image\num.png')
photoimage_1 = photo_1.subsample(12,12)
photo_2 = PhotoImage(file=r'image\slash.png')
photoimage_2 = photo_2.subsample(12,12)
photo_3 = PhotoImage(file=r'image\star.png')
photoimage_3 = photo_3.subsample(12,12)
photo_4 = PhotoImage(file=r'image\minus.png')
photoimage_4 = photo_4.subsample(12,12)
photo_5 = PhotoImage(file=r'image\key_plus.png')
photoimage_5 = photo_5.subsample(12,12)
photo_6 = PhotoImage(file=r'image\key_enter.png')
photoimage_6 = photo_6.subsample(12,12)
photo_7 = PhotoImage(file=r'image\key_7.png')
photoimage_7 = photo_7.subsample(12,12)
photo_8 = PhotoImage(file=r'image\key_8.png')
photoimage_8 = photo_8.subsample(12,12)
photo_9 = PhotoImage(file=r'image\key_9.png')
photoimage_9 = photo_9.subsample(12,12)
photo_10 = PhotoImage(file=r'image\key_4.png')
photoimage_10 = photo_10.subsample(12,12)
photo_11 = PhotoImage(file=r'image\key_5.png')
photoimage_11 = photo_11.subsample(12,12)
photo_12 = PhotoImage(file=r'image\key_6.png')
photoimage_12 = photo_12.subsample(12,12)
photo_13 = PhotoImage(file=r'image\key_1.png')
photoimage_13 = photo_13.subsample(12,12)
photo_14 = PhotoImage(file=r'image\key_2.png')
photoimage_14 = photo_14.subsample(12,12)
photo_15 = PhotoImage(file=r'image\key_3.png')
photoimage_15 = photo_15.subsample(12,12)
photo_16 = PhotoImage(file=r'image\key_zero.png')
photoimage_16 = photo_16.subsample(12,11)
photo_17 = PhotoImage(file=r'image\key_dot.png')
photoimage_17 = photo_17.subsample(12,11)

button_1 = Button(root,command=lambda : clear(),background="#464746",padx='0',pady='0',image=photoimage_1,highlightthickness = 1, bd = 0)
button_2 = Button(root,command=lambda : operation("/"),background="#464746",padx='0',pady='0',image=photoimage_2,highlightthickness = 1, bd = 0)
button_3 = Button(root,command=lambda : operation("*"),background="#464746",padx='0',pady='0',image=photoimage_3,highlightthickness = 1, bd = 0)
button_4 = Button(root,command=lambda : operation("-"),background="#464746",padx='0',pady='0',image=photoimage_4,highlightthickness = 1, bd = 0)
button_5 = Button(root,command=lambda : operation("+"),background="#464746",padx='0',pady='0',image=photoimage_5,highlightthickness = 1, bd = 0)
button_6 = Button(root,command=lambda : calculate(),background="#464746",padx='0',pady='0',image=photoimage_6,highlightthickness = 1, bd = 0)
button_7 = Button(root,command=lambda : add_digit(7),background="#464746",padx='0',pady='0',image=photoimage_7,highlightthickness = 1, bd = 0)
button_8 = Button(root,command=lambda : add_digit(8),background="#464746",padx='0',pady='0',image=photoimage_8,highlightthickness = 1, bd = 0)
button_9 = Button(root,command=lambda : add_digit(9),background="#464746",padx='0',pady='0',image=photoimage_9,highlightthickness = 1, bd = 0)
button_10 = Button(root,command=lambda : add_digit(4),background="#464746",padx='0',pady='0',image=photoimage_10,highlightthickness = 1, bd = 0)
button_11 = Button(root,command=lambda : add_digit(5),background="#464746",padx='0',pady='0',image=photoimage_11,highlightthickness = 1, bd = 0)
button_12 = Button(root,command=lambda : add_digit(6),background="#464746",padx='0',pady='0',image=photoimage_12,highlightthickness = 1, bd = 0)
button_13 = Button(root,command=lambda : add_digit(1),background="#464746",padx='0',pady='0',image=photoimage_13,highlightthickness = 1, bd = 0)
button_14 = Button(root,command=lambda : add_digit(2),background="#464746",padx='0',pady='0',image=photoimage_14,highlightthickness = 1, bd = 0)
button_15 = Button(root,command=lambda : add_digit(3),background="#464746",padx='0',pady='0',image=photoimage_15,highlightthickness = 1, bd = 0)
button_16 = Button(root,command=lambda : add_digit(0),background="#464746",padx='0',pady='0',image=photoimage_16,highlightthickness = 1, bd = 0)
button_17 = Button(root,command=lambda : add_digit("."),background="#464746",padx='0',pady='0',image=photoimage_17,highlightthickness = 1, bd = 0)

button_1.place(x=0,y=80)
button_2.place(x=70,y=80)
button_3.place(x=140,y=80)
button_4.place(x=210,y=80)
button_5.place(x=210,y=148)
button_6.place(x=210,y=288)
button_7.place(x=0,y=148)
button_8.place(x=70,y=148)
button_9.place(x=140,y=148)
button_10.place(x=0,y=216)
button_11.place(x=70,y=216)
button_12.place(x=140,y=216)
button_13.place(x=0,y=284)
button_14.place(x=70,y=284)
button_15.place(x=140,y=284)
button_16.place(x=1,y=352)
button_17.place(x=140,y=352)

root.mainloop()