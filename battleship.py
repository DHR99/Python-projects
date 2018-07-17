import random

def battleship():
    board=[]
    for x in range(0,5):
        board.append(['O']*5)
    
    ship_row = random.randint(0,4)
    ship_col = random.randint(0,4)
    board[ship_row][ship_col] = 'B'
    
    def print_board(board):
        for i in board:
            print("".join(i))
  
    #def random_row(board):
    #    return random.randint(0, len(board)-1)
  
    #def random_col(board):
     #   return random.randint(0, len(board)-1)
    
    def guess():
        trials=1
        guess_row = int(input("Which row? "))
        guess_col = int(input("Which column? "))
    
        while (trials <= 6):
            if (trials >= 5):
                print()
                print("RUN OUT OF CHANCES")
                break
                
            elif (guess_row == 99 or guess_col == 99):
                print("BYE")
                break
        
            elif (guess_row == ship_row and guess_col == ship_col):
                print('RIGHT')
                trials += 1
                break
      
            elif (guess_row != ship_row or guess_col != ship_col):
                print("You missed the battleship!")
                print("Trial num: ", trials)
                trials += 1
                guess_row=int(input("Which row? "))
                guess_col=int(input("Which column? "))
        
              
    print_board(board)
  
    guess()
  
      
battleship()
