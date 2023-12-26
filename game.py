import random

class Game():
    def __init__(self):
        self.vector= [1,2,3,4,5,6,7,8,9]
        self.board = ['','','','','','','','','']
        self.win= False
        #player, True-user, False-computer
        self.player = True
    
    def show_board(self):
        b = f"""  {self.board[0]}  |  {self.board[1]}  |  {self.board[2]}  \n\n________________\n\n  {self.board[3]}  |  {self.board[4]}  |  {self.board[5]}  \n\n________________\n\n  {self.board[6]}  |  {self.board[7]}  |  {self.board[8]}  \n"""
        
    def choice(self,value):
        n = 1
        while n == 1:
            try:
                nval= int(value)
                n = 0
            except(ValueError):
                value= input('please, provide a number from 1 to 8\n')
                n = 1
            if nval < 1 or nval > 8:
                n = 1
                value= input('please, provide a number from 1 to 8\n')
        c = 1
        while c == 1:
            if nval in self.vector:
                self.vector.remove(nval)
                c = 0
            else:
                value = input('this position is taken. please pick a different number\n')
    
    def user_req(self):
        value = input('please, type the number  \n')
        value = random.choice(self.vector)
        self.choice(value)
        self.board[value-1]='X'
        self.player = True
        self.show_board()
        self.win()
        
    
    def comp_req(self):
        value = random.choice(self.vector)
        self.choice(value)
        self.board[value-1]='O'
        self.player = False
        self.show_board()
        self.win()
        
        
    def win(self):
        #rows
        if self.board[1] == self.board[2] == self.board[3]:
            self.wining_note()
        elif self.board[4] == self.board[5] == self.board[6]:
            self.wining_note()
        elif self.board[7] == self.board[8] == self.board[9]:
            self.wining_note()
        #cross
        elif self.board[1] == self.board[5] == self.board[9]:
            self.wining_note()
        elif self.board[3] == self.board[5] == self.board[7]:
            self.wining_note
        #columns
        elif self.board[1] == self.board[4] == self.board[7]:
            self.wining_note()
        elif self.board[2] == self.board[5] == self.board[8]:
            self.wining_note()
        elif self.board[3] == self.board[6] == self.board[9]:
            self.wining_note()
            
    def wining_note(self):
        if self.player == True:
            print('Congratulations! You won the game. see you on the next game.')  
        else:
            print('You lost! maybe next time : - )')    
        

