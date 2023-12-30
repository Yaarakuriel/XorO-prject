import random
#after fixing, generalize for NxN board
class Game():
    def __init__(self):
        self.vector = list(range(1, 10))
        self.board = [[' ' for i in range(3)] for i in range(3) ]
        self.moves=0
        self.end=False
        
    def opening(self):
        print('Welocme to X Mix Drix Game! You will play X. the numbers are the locations on the board as will be presented below. pick a number and let\'s play')
        for i in range(3):
            for j in range(3):
                print(f"  {self.vector[i*3+j]}  ",end="") 
                if j!=2:
                    print(" | ",end="")
            if i!=2:
                print('\n_______________________\n')
            else:
                print('\n')
        
    def show_board(self):
        for i in range(3):
            for j in range(3):
                print(f"  {self.board[i][j]} ",end="")
                if j!=2:
                    print(" | ",end="")
            print('\n________________________\n')
            
    def choice(self,val):
        if val in [i for i in range(1,10)] and val in self.vector:
            return True
        return False
    
    def req(self):
        val=None
        self.moves+=1

        user=self.moves%2==1
        if user:
            value = int(input('please, type the number  \n'))
            val='X'
            check=self.choice(value)
            if not check:
                print("not an int or not in [1,2,3,4,5,6,7,8,9],or taken, try again:")
                self.moves-=1
                self.req()
        else:
            value = random.choice(self.vector)
            val='O'
          
            # Adjust index to be within the valid range
        index = int(value) - 1
        row, col = divmod(index, 3)

        self.board[row][col] = val
        self.vector.remove(value)  

        self.show_board()
        self.end=self.victory()
        if self.end:
            self.wining_note(user)
        
        
    def victory(self):
        if self.moves<5:
            return False
        
        #rows
        for i in range(3):
            row=self.board[i]
            if all(i == row[0] for i in row) and row[0]!=" ":
                return True

        #cross
        diagonal1 = [self.board[i][i] for i in range(3)]
        diagonal2 = [self.board[i][2 - i] for i in range(3)]

        if all(element == diagonal1[0] and element != " " for element in diagonal1):
            return True

        if all(element == diagonal2[0] and element != " " for element in diagonal2):
            return True
        #columns
        column=[]
        for j in range(3):
            for i in range(3):
                column.append(self.board[i][j])
            if all(i == column[0] for i in column) and column[0]!=" ":
                return True
            column=[]
        
        return False
            
    def wining_note(self,win):
        if win:
            print('Congratulations! You won the game. see you on the next game.')  
        else:
            print('You lost! maybe next time : - )')    
        
    
    def active_game(self):
        self.opening()
        while not self.end :
            self.req()
    
