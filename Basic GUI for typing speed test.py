import tkinter as tk
import time as t
import random as r
word_lst=[]
flst=['andreia', 'gets', 'point', 'connection', 'multimedia', 'innovation', 'from', 'escola', 'master', 'educacao', 'coimbra', 'leading', 'developer', 'hijiffy', 'favorite', 'film', 'containers', 'maze', 'guillermo', 'toro', 'moms', 'arroz', 'cabidela', 'portuguese', 'container', 'created', 'with', 'bird', 'rabbit', 'cooked', 'blood', 'brought', 'food', 'taste', 'vinegar', 'favorite', 'food', 'olive', 'park', 'topelected', 'color', 'when', 'andreia', 'younger', 'nearly', 'sucked', 'parents', 'room', 'because', 'decided', 'with', 'playing', 'cooking', 'stacks', 'wood', 'heater', 'during', 'childhood', 'times', 'knew', 'ride', 'bicycle', 'through', 'woods', 'presently', 'loves', 'watching', 'television', 'broadcast', 'starting', 'with', 'their', 'acquaintances', 'concerts', 'concerts', 'concerts', 'lots', 'lots', 'them', 'really', 'admires', 'sister', 'this', 'female', 'just', 'with', 'years', 'older', 'andreia', 'identifies', 'herself', 'resilient']



def t_speed(main_lst,lst2):
    count=0
    for i in main_lst:
        if i in lst2:
            count+=1
    return count
    
def get_rand(lst):
    return r.choice(lst)
    

def change(a=1):
    
    time_f=t.time()
    if int((time_f)-int(time_i))>60:
        canva_1.delete('all')
        
        canva_1.create_text(300,50,text='YOUR TIME IS OVER',fill='red', font=('Helvetica 15 bold'))
        
        canva_1.create_text(250,150,text=('your typing speed is with correct spelling is '+str(t_speed(word_lst,flst))+ ' words per minute'),fill='black', font=('Helvetica 10 bold'))
        canva_1.create_text(250,180,text=('and with all correct or incorrect word is '+str(len(word_lst))+' words per minute'),fill='black', font=('Helvetica 10 bold'))
        button_2=tk.Button(canva_1,text='click to close ',width=12,command=close)
        button_2.place(x=500,y=150)
    else:
        canva_1.delete('all')
        canva_1.create_text(300,50,text=get_rand(flst),fill='black', font=('Helvetica 15 bold'))
        canva_1.pack()
        string=entry.get()
        if string!='':
            word_lst.append(string.strip())
        entry.delete(0,'end')
        
    
def start():
    global time_i
    time_i=t.time()
    button_1.destroy()
    change()
    
def close():
    root.destroy()

root=tk.Tk()
canva_1=tk.Canvas(root,width=600,height=200,background='white')
canva_1.pack()
root.bind('<Return>',change)
root.bind('<space>',change)

canva_1.create_text(300, 50, text="Press The Button to Start ", fill="black", font=('Helvetica 15 bold'))
canva_1.pack()

button_1=tk.Button(canva_1,text='start',width=10,command=start)
button_1.place(x=250,y=150)

entry=tk.Entry(canva_1,width=30)
entry.place(x=200,y=100)



tk.mainloop()
