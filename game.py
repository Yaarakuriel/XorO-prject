class Game():
    def __init__(self):
        self.vector= [1,2,3,4,5,6,7,8,9]
        
    def choice(self,value):
        n = 1
        while n == 1:
            try:
                nval= int(value)
                n = 0
            except(ValueError):
                value= input('please, provide a number from 1 to 8\n')
                n = 1
        c = 1
        while c == 1:
            if nval in self.vector:
                self.vector.remove(nval)
                c = 0
            else:
                value = input('this position is taken. please pick a different number\n')

