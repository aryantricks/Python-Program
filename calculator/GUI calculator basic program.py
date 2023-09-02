from tkinter import *
import re

root=Tk()
txt=''
canva1=Canvas(root,height=80,width=300,background='white')
canva1.pack()


canva2=Canvas(root,height=400,width=400 , background='white')
canva2.pack()



def remove_leading_zeros(expression):
    pattern = r'\b0+(\d+)'
    repl = r'\1'
    result = re.sub(pattern, repl, expression)
    return result


def one(x=1):
    global txt
    txt += '1'
    canva1.delete('all')
    canva1.create_text(150, 40, text=txt, fill="black", font=('Helvetica 15'))

def two(x=1):
    global txt
    txt += '2'
    canva1.delete('all')
    canva1.create_text(150, 40, text=txt, fill="black", font=('Helvetica 15'))

def three(x=1):
    global txt
    txt += '3'
    canva1.delete('all')
    canva1.create_text(150, 40, text=txt, fill="black", font=('Helvetica 15'))

def four(x=1):
    global txt
    txt += '4'
    canva1.delete('all')
    canva1.create_text(150, 40, text=txt, fill="black", font=('Helvetica 15'))

def five(x=1):
    global txt
    txt += '5'
    canva1.delete('all')
    canva1.create_text(150, 40, text=txt, fill="black", font=('Helvetica 15'))

def six(x=1):
    global txt
    txt += '6'
    canva1.delete('all')
    canva1.create_text(150, 40, text=txt, fill="black", font=('Helvetica 15'))

def seven(x=1):
    global txt
    txt += '7'
    canva1.delete('all')
    canva1.create_text(150, 40, text=txt, fill="black", font=('Helvetica 15'))

def eight(x=1):
    global txt
    txt += '8'
    canva1.delete('all')
    canva1.create_text(150, 40, text=txt, fill="black", font=('Helvetica 15'))

def nine(x=1):
    global txt
    txt += '9'
    canva1.delete('all')
    canva1.create_text(150, 40, text=txt, fill="black", font=('Helvetica 15'))

def zero(x=1):
    global txt
    txt += '0'
    canva1.delete('all')
    canva1.create_text(150, 40, text=txt, fill="black", font=('Helvetica 15'))

def mins(x=1):
    global txt
    if len(txt)!=0:
        if txt[-1] in '+-*/':
            txt=txt[:-1:]
    txt += '-'
    canva1.delete('all')
    canva1.create_text(150, 40, text=txt, fill="black", font=('Helvetica 15'))

def div(x=1):
    global txt
    if len(txt)!=0:
        if txt[-1] in '+-*/':
            txt=txt[:-1:]
    txt += '/'
    canva1.delete('all')
    canva1.create_text(150, 40, text=txt, fill="black", font=('Helvetica 15'))

def mult(x=1):
    global txt
    if len(txt)!=0:
        if txt[-1] in '+-*/':
            txt=txt[:-1:]
    txt += '*'
    canva1.delete('all')
    canva1.create_text(150, 40, text=txt, fill="black", font=('Helvetica 15'))

def plus(x=1):
    global txt
    if len(txt)!=0:
        if txt[-1] in '+-*/':
            txt=txt[:-1:]
    txt += '+'
    canva1.delete('all')
    canva1.create_text(150, 40, text=txt, fill="black", font=('Helvetica 15'))

def equal(x=1):
    global txt
    try:
        txt=remove_leading_zeros(txt)
        txt=str(eval(txt))
        canva1.delete('all')
        canva1.create_text(150, 40, text=txt, fill="black", font=('Helvetica 15'))
    except:
        canva1.delete('all')
        canva1.create_text(150, 40, text='INVALID !!!', fill="black", font=('Helvetica 15'))
    
def c(x=1):
    global txt
    txt=txt[:-1]
    canva1.delete('all')
    canva1.create_text(150, 40, text=txt, fill="black", font=('Helvetica 15'))
    
    
def point(x=1):
    global txt
    if txt[-1].isnumeric():
        txt+='.'
    canva1.delete('all')
    canva1.create_text(150, 40, text=txt, fill="black", font=('Helvetica 15'))
    

b_one = Button(canva2, text='1',foreground='white', borderwidth=0,background='#505050',width=10, height=2, command=one)
b_one.grid(row=1, column=1)

b_two = Button(canva2, text='2',foreground='white', borderwidth=0,background='#505050',width=10, height=2 , command=two)
b_two.grid(row=1, column=2)

b_three = Button(canva2, text='3',foreground='white', borderwidth=0,background='#505050',width=10, height=2 ,command=three)
b_three.grid(row=1, column=3)

b_four = Button(canva2, text='4',foreground='white', borderwidth=0,background='#505050', width=10, height=2 ,command=four)
b_four.grid(row=2, column=1)

b_five = Button(canva2, text='5',foreground='white', borderwidth=0,background='#505050', width=10, height=2 ,command=five)
b_five.grid(row=2, column=2)

b_six = Button(canva2, text='6',foreground='white', borderwidth=0,background='#505050', width=10, height=2 ,command=six)
b_six.grid(row=2, column=3)

b_seven = Button(canva2, text='7',foreground='white', borderwidth=0,background='#505050', width=10, height=2 ,command=seven)
b_seven.grid(row=3, column=1)

b_eight = Button(canva2, text='8',foreground='white', borderwidth=0,background='#505050', width=10, height=2 ,command=eight)
b_eight.grid(row=3, column=2)

b_nine = Button(canva2, text='9', foreground='white', borderwidth=0,background='#505050',width=10, height=2 ,command=nine)
b_nine.grid(row=3, column=3)

b_zero = Button(canva2, text='0',foreground='white', borderwidth=0,background='#505050', width=10, height=2 ,command=zero)
b_zero.grid(row=4, column=2)

b_plus = Button(canva2, text='+',width=10,borderwidth=1, height=2 ,command=plus)
b_plus.grid(row=1, column=4)

b_mins = Button(canva2, text='-', width=10,borderwidth=1, height=2 ,command=mins)
b_mins.grid(row=2, column=4)

b_mult = Button(canva2, text='*', width=10,borderwidth=1, height=2 ,command=mult)
b_mult.grid(row=3, column=4)

b_div = Button(canva2, text="/",width=10, borderwidth=1,height=2 ,command=div)
b_div.grid(row=4, column=4)

b_equal = Button(canva2, text="=",width=10, borderwidth=1,background='#FF9500',height=2 ,command=equal)
b_equal.grid(row=5, column=4)

b_c = Button(canva2, text="C",width=10, borderwidth=1,height=2 ,command=c)
b_c.grid(row=4, column=3)

b_point = Button(canva2, text=".",width=10, borderwidth=1,height=2 ,command=point)
b_point.grid(row=4, column=1)



root.bind('1', one)
root.bind('2', two)
root.bind('3', three)
root.bind('4', four)
root.bind('5', five)
root.bind('6', six)
root.bind('7', seven)
root.bind('8', eight)
root.bind('9', nine)
root.bind('0',zero)
root.bind('<Return>', equal)
root.bind('=', equal)
root.bind('-', mins)
root.bind('+', plus)
root.bind('*', mult)
root.bind('/', div)
root.bind('<BackSpace>', c)
root.bind('c', c)
root.bind('.', point)




mainloop()
