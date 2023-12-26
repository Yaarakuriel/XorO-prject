from game import Game
opening = "Welcome To X Mix Drix Game! \nfrom now on, You'll play X . for you to play, enter the number you'd like X to be instead\n"
vector = [1,2,3,4,5,6,7,8,9]
board = f"""  {vector[0]}  |  {vector[1]}  |  {vector[2]}  \n\n________________\n\n  {vector[3]}  |  {vector[4]}  |  {vector[5]}  \n\n________________\n\n  {vector[6]}  |  {vector[7]}  |  {vector[8]}  \n"""
print(opening)
print(board)


XorO= Game()
XorO.user_req()
    