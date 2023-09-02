import random as r
from tkinter import *

fruits = ['mango', 'banana', 'papaya', 'guava', 'watermelon', 'pomegranate', 'grapes', 'orange', 'pineapple', 'apple', 'kiwi', 'strawberry', 'lychee', 'muskmelon', 'jackfruit']
vegetables = ['potato', 'onion', 'tomato', 'carrot', 'cucumber', 'cauliflower', 'spinach', 'beans', 'peas', 'garlic', 'ginger', 'radish', 'pumpkin', 'sweet potato', 'cabbage']
cities = ['tokyo', 'new york city', 'london', 'paris', 'dubai', 'singapore', 'sydney', 'los angeles', 'rome', 'barcelona', 'moscow', 'tokyo', 'beijing', 'mumbai', 'istanbul', 'berlin', 'bangkok', 'toronto']
hindi_names = ['abhinav', 'arya', 'aditi', 'aditya', 'arav', 'arush', 'arohi', 'arjun', 'aman', 'ayush', 'ayushman', 'bharat', 'divya', 'gauri', 'harsh', 'ishan', 'jay', 'kavita', 'kiran', 'krishna']
lst_main=[fruits,vegetables,cities,hindi_names]

lst_name=''
word=''
right=0
wrong=0

def rand_word(lst):
    global lst_name
    global word
    words=r.choice(lst)
    if words==fruits:
        lst_name='fruit'
    elif words==vegetables:
        lst_name='vegetable'
    elif words==cities:
        lst_name='city'
    elif words==hindi_names:
        lst_name='hindi name'
        
    word=r.choice(words)
    word_lst=list(word)
    r.shuffle(word_lst)
    wordf=''
    for i in word_lst:
        wordf+=i
    return wordf

    
def start():
    start_button.destroy()
    canva.delete('all')
    start_game()
    def close():
        root.destroy()
    close_button=Button(canva,text='close')
    close_button.place(x=700,y=20)
    
def start_game():
    global entry
    canva.create_text(400, 50, text="Your Word is",fill="red", font=('Helvetica 25'))
    canva.create_text(400, 120, text=rand_word(lst_main),fill="black", font=('Helvetica 30'))
    canva.create_text(400, 380, text="Hint: This is a "+lst_name,fill="black", font=('Helvetica 15 '))
    entry=Entry(canva,width=15,font=('Helvetica',30))
    entry.place(x=235,y=200)
    check_button=Button(canva,text='CHECK',font=('Helvetica 15'),width='10',command=check)
    check_button.place(x=330,y=270)
    
    
def check(a=1):
    global right, wrong
    if entry.get().strip()==word:
        canva.delete('all')
        start_game()
        canva.create_text(400, 335, text="you was right",fill="green", font=('Helvetica 15 '))
        right+=1
        
        
    else:
        canva.delete('all')
        start_game()
        canva.create_text(400, 335, text="wrong !!!",fill="red", font=('Helvetica 15 '))
        wrong+=1
        
    entry.delete(0,'end')
    canva.create_text(100, 60, text='correct words : '+str(right),fill="green", font=('Helvetica 15'))
    canva.create_text(100, 80, text='incorrect words : '+str(wrong),fill="red", font=('Helvetica 15'))
    
root=Tk()
canva=Canvas(root,width=800,height=400)
canva.pack()
    
    
canva.create_text(400, 50, text="Press The Button to Start ", fill="black", font=('Helvetica 25'))    
    
    
start_button=Button(canva,text='Start',font=('Helvetica 15'),width='10',command=start)
start_button.place(x=330,y=200)
root.bind('<Return>',check)

mainloop()
