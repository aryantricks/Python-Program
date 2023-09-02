from tkinter import *

board=[['-','-','-'],['-','-','-'],['-','-','-']]
buttons=[['-','-','-'],['-','-','-'],['-','-','-']]

player='X'

def reset():
    global board , buttons , player
    board=[['-','-','-'],['-','-','-'],['-','-','-']]
    buttons=[['-','-','-'],['-','-','-'],['-','-','-']]
    player='X'
    can2.delete('all')
    create_button()
    
def show_winner(x):
    can2.create_text(100,50,text='The Winner is '+x)
    for row in range(3):
        for col in range(3):
            (buttons[row][col])['state']=DISABLED
            
    rb=Button(can2,text='RESET',width=10,height=2,command=reset)
    rb.place(x=100,y=100)
    

def button_click(row,column):
    global board , buttons , player
    if board[row][column]=='-':
        board[row][column]=player
        (buttons[row][column])['text']=player
        
        if player=='X':
            player='O'
        else:
            player='X'
            
    check_status()
        
        
        
        
def check_status():
    wf=False
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != '-':
            show_winner(board[row][0])
            wf=True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] !='-':
            show_winner(board[0][col])
            wf=True
            
    if board[0][0] == board[1][1] == board[2][2] != "-":
        show_winner(board[0][0])
        wf=True
    elif board[0][2] == board[1][1] == board[2][0] != "-":
        show_winner(board[0][2])
        wf=True
        
    if wf==False:
        empty=False
        for row in range(3):
            for col in range(3):
                if board[row][col]=='-':
                    empty=True
                    break
        if empty==False:
            can2.create_text(20,20,text='TIE')


def create_button():
    for row in range(3):
        for col in range(3):
            buttons[row][col]=Button(can1,width=10,height=4,command=lambda r=row, c=col: button_click(r, c))
            buttons[row][col].grid(row=row,column=col)
        
        
root=Tk()

can1=Canvas(root,width=300,height=300)
can1.pack()

can2=Canvas(root,width=300,height=300)
can2.pack()

create_button()


mainloop()
