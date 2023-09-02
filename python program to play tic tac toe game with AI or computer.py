from tkinter import *
lst=[['-', '-', '-'], 
     ['-', '-', '-'], 
     ['-', '-', '-']]


def place_o():
    global lst
    found=False
    
    #fillin O to win
     # row
    for row in lst:
        
        for i in row:
            if i == '-' and found==False:
                if row[0] == row[1] == 'O':
                    row[2] = 'O'
                    found=True
                if row[1] == row[2] == 'O':
                    row[0] = 'O'
                    found=True
                if row[0] == row[2] == 'O':
                    row[1] = 'O'
                    found=True
                
                
      # column          
    for i in range(3):
        for j in range(3):
            if lst[j][i] == '-' and not found:
                if lst[0][i]==lst[1][i]=='O':
                    lst[2][i]='O'
                    found=True
                if lst[0][i]==lst[2][i]=='O':
                    lst[1][i]='O'
                    found=True
                if lst[1][i]==lst[2][i]=='O':
                    lst[0][i]='O'
                    found=True

        # diagonal
        
    for j in range(3):
        if lst[j][j]=='-' and not found:
                
            if lst[0][0]==lst[1][1]=='O':
                lst[2][2]='O'
                found=True
            if lst[1][1]==lst[2][2]=='O':
                lst[0][0]='O'
                found=True
            if lst[0][0]==lst[2][2]=='O':
                lst[1][1]='O'
                found=True
                    
    if (lst[0][2]=='-' or lst[1][1]=='-'or lst[2][0]=='-') and not found:
            if lst[0][2]==lst[1][1]=='O':
                lst[2][0]='O'
                found=True
            if lst[0][2]==lst[2][0]=='O':
                lst[1][1]='O'
                found=True
            if lst[1][1]==lst[2][0]=='O':
                lst[0][2]='O'
                found=True
                    
    # blocking X 
    
    
    # row
    for row in lst:
        
        for i in row:
            if i == '-' and found==False:
                if row[0] == row[1] == 'X':
                    row[2] = 'O'
                    found=True
                if row[1] == row[2] == 'X':
                    row[0] = 'O'
                    found=True
                if row[0] == row[2] == 'X':
                    row[1] = 'O'
                    found=True
                
                
      # column          
    for i in range(3):
        for j in range(3):
            if lst[j][i] == '-' and not found:
                if lst[0][i]==lst[1][i]== 'X':
                    lst[2][i]='O'
                    found=True
                if lst[0][i]==lst[2][i]== 'X':
                    lst[1][i]='O'
                    found=True
                if lst[1][i]==lst[2][i]== 'X':
                    lst[0][i]='O'
                    found=True

        # diagonal
        
    for j in range(3):
        if lst[j][j]=='-' and not found:
                
            if lst[0][0]==lst[1][1]== 'X':
                lst[2][2]='O'
                found=True
            if lst[1][1]==lst[2][2]== 'X':
                lst[0][0]='O'
                found=True
            if lst[0][0]==lst[2][2]== 'X':
                lst[1][1]='O'
                found=True
                    
    if (lst[0][2]=='-' or lst[1][1]=='-'or lst[2][0]=='-') and not found:
            if lst[0][2]==lst[1][1]== 'X':
                lst[2][0]='O'
                found=True
            if lst[0][2]==lst[2][0]== 'X':
                lst[1][1]='O'
                found=True
            if lst[1][1]==lst[2][0]== 'X':
                lst[0][2]='O'
                found=True
                
                
    # if both not possible
    for i in range(3):
        for j in range(3):
            if lst[i][j]=='-' and not found:
                lst[i][j]='O'
                found=True
                
            
        
            
        
def winner(lst):
    winner_found=False
    winner=None
    if not winner_found:
        for i in range(3):
            for j in range(3):
                if lst[i][0]==lst[i][1]==lst[i][2]=='X':
                    winner = 'X'
                    winner_found=True
                elif lst[i][0]==lst[i][1]==lst[i][2]=='O':
                    winner='O'
                    winner_found=True
    if not winner_found:
        for i in range(3):
            for j in range(3):
                if lst[0][i]==lst[1][i]==lst[2][i]=='X':
                    winner='X'
                    winner_found=True
                    
                elif lst[0][i]==lst[1][i]==lst[2][i]=='O':
                    winner='O'
                    winner_found=True
                    
                    
    if not winner_found:
        if lst[0][0]==lst[1][1]==lst[2][2]=='X':
            winner='X'
            winner_found=True
    if not winner_found:
        if lst[0][0]==lst[1][1]==lst[2][2]=='O':
            winner='O'
            winner_found=True
                
                
    if not winner_found:
        if lst[2][0]==lst[1][1]==lst[0][2]=='X':
            winner='X'
            winner_found=True
    if not winner_found:
        if lst[2][0]==lst[1][1]==lst[0][2]=='O':
            winner='O'
            winner_found=True
            
            
    return winner
                
    
    
    
buttons=[['-','-','-'],['-','-','-'],['-','-','-']]    
def create_buttons():
    global buttons
    
    for row in range(3):
        for col in range(3):
            txt=lst[row][col]
            buttons[row][col]=Button(can1,width=10,height=4,text=txt,command=lambda r=row , c=col : click(r,c))
            buttons[row][col].grid(row=row,column=col)
            
            
            
    
    
def click(row,col):
    global lst,buttons
    if lst[row][col]=='-':
        lst[row][col]='X'
        place_o()
        create_buttons()
        if winner(lst)=='X' or winner(lst)=='O':
            can2.delete('all')
            can2.create_text(100,100,text='The winner is '+winner(lst))
    
    
def reset():
    global lst,buttons
    buttons=[['-','-','-'],['-','-','-'],['-','-','-']]
    lst=[['-','-','-'],['-','-','-'],['-','-','-']]
    create_buttons()
    can2.delete('all')
    
    
root=Tk()

can1=Canvas(root,width=300,height=300)
can1.pack()


can2=Canvas(root,width=300,height=300)
can2.pack()

rb=Button(can2,width=10,height=4 ,text='reset',comman=reset)
rb.place(x=150,y=150)

create_buttons()

mainloop()

        
    
