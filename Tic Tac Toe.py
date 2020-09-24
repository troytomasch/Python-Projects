## Troy Tomasch
## Tic Tac Toe

import random

## Instructions and How to Play
def intro():
    print('Welcome to Tic Tac Toe!')
    print('Get 3 in a row to Win!')

## Resets Board
def resetBoard(board):
    for i in range(0, 9):
        board = board + ['-']
    return board

## Displays the Board    
def displayBoard(board):
    print('=============')
    print('    ' + str(board[0]) + ' ' + str(board[1]) + ' ' + str(board[2]))
    print('    ' + str(board[3]) + ' ' + str(board[4]) + ' ' + str(board[5]))
    print('    ' + str(board[6]) + ' ' + str(board[7]) + ' ' + str(board[8]))    
    print('=============')

## Turn 
def playGame(record):
    board = []
    board = resetBoard(board)
    while not gameWon(board):
        displayBoard(board)
        print("Which space would you like to choose?")
        board = updateBoardU(chooseSpace("Space: ", board), board)
        if gameWon(board) == True:
            userWins(board)
            record[0] += 1
            break
        if gameTie(board) == True:
            gameT(board)
            record[2] += 1
            break
        print("Opponent's turn...")
        board = updateBoardC(computerMove(board), board)
        if gameWon(board) == True:
            computerWins(board)
            record[1] += 1
            break
    playAgain(AplayAgain("Would you like to play again? (Yes or No): "), record)

## The game ties
def gameT(board):
    displayBoard(board)
    print("It's a tie!")

## The user winning
def userWins(board):
    displayBoard(board)
    print('You win!')

## The computer winning
def computerWins(board):
    displayBoard(board)
    print('You lost!')

       
## Updates Board for User
def updateBoardU(space, board):
    lBoard = board
    lBoard[int(space)-1] = 'X'
    return lBoard

## Updates Board for Computer
def updateBoardC(space, board):
    lBoard = board
    lBoard[int(space)-1] = 'O'
    return lBoard


## Choosing Space
def chooseSpace(prompt, board):
    ans = input(prompt)
    while not board[int(ans)-1] == '-':
        ans = input(prompt)
    while int(ans) > 9 or int(ans) < 0:
        ans = input(prompt)
    return ans

## Computer Move
def computerMove(board):
    count = 0
    for i in range(0,9):
        if not board[i] == '-':
            count += 1
    if count == 1: ## first move
        if board[4] == 'X':
            return str(random.choice([1, 3, 7, 9]))
        else:
            return str(5)
    elif count >= 3: ## later moves
        if board[4] == 'X': ## if the user has played the middle
            if board[0] == 'X' and board[8] == '-':
                return str(9)
            elif board[1] == 'X' and board[7] == '-':
                return str(8)
            elif board[2] == 'X' and board[6] == '-':
                return str(7)
            elif board[3] == 'X' and board[5] == '-':
                return str(6)
            elif board[5] == 'X' and board[3] == '-':
                return str(4)
            elif board[6] == 'X' and board[2] == '-':
                return str(3)
            elif board[7] == 'X' and board[1] == '-':
                return str(2)
            elif board[8] == 'X' and board[0] == '-':
                return str(1)
            else:
                num = random.randint(1,9)
                while not board[int(num)-1] == '-':
                    num = random.randint(1,9)
                return str(num)
        elif board[0] == 'X' and board[2] == 'X' and board[1] == '-':
            return str(2)
        elif board[0] == 'X' and board[6] == 'X' and board[3] == '-':
            return str(4)
        elif board[8] == 'X' and board[2] == 'X' and board[5] == '-':
            return str(6)
        elif board[8] == 'X' and board[6] == 'X' and board[7] == '-':
            return str(8)
        elif board[0] == 'X' and board[1] == 'X' and board[2] == '-':
            return str(3)
        elif board[1] == 'X' and board[2] == 'X' and board[0] == '-':
            return str(1)
        elif board[0] == 'X' and board[3] == 'X' and board[6] == '-':
            return str(7)
        elif board[3] == 'X' and board[7] == 'X' and board[0] == '-':
            return str(1)
        elif board[6] == 'X' and board[7] == 'X' and board[8] == '-':
            return str(9)
        elif board[7] == 'X' and board[8] == 'X' and board[6] == '-':
            return str(7)
        elif board[2] == 'X' and board[5] == 'X' and board[8] == '-':
            return str(9)
        elif board[8] == 'X' and board[5] == 'X' and board[2] == '-':
            return str(2)
        else:
            num = random.randint(1,9)
            while not board[int(num)-1] == '-':
                num = random.randint(1,9)
            return str(num)

## Checks whether the game is won
def gameWon(board):
    if (board[0] == 'X') or (board[0] == 'O'):
        if board[0] == board[1] == board[2]:
            return True
        elif board[0] == board[3] == board[6]:
            return True
        elif board[0] == board[4] == board[8]:
            return True
    if (board[4] == 'X' or board[4] == 'O'):      
        if board[3] == board[4] == board[5]:
            return True
        elif board[1] == board[4] == board[7]:
            return True
        elif board[2] == board[4] == board[6]:
            return True
    if (board[8] == 'X' or board[8] == 'O'):
        if board[2] == board[5] == board[8]:
            return True
        elif board[6] == board[7] == board[8]:
            return True
    else:
        return False

## Checks if the game is a tie
def gameTie(board):
    for i in range(0,9):
        if board[i] == '-':
            return False
    return True
        
        
## Asks to play again
def AplayAgain(prompt):
    ans = input(prompt)
    while not (ans == "Yes" or ans == "No"):
        ans = input(prompt)
    return ans

## Plays Again
def playAgain(ans, record):
    if ans == "Yes":
        print("New Game!")
        print("User Wins: " + str(record[0]) + ", Computer Wins: " + str(record[1]) + ", Ties: " + str(record[2]))
        playGame(record)
    else:
        print("User Wins: " + str(record[0]) + ", Computer Wins: " + str(record[1]) + ", Ties: " + str(record[2]))

## Main
def main():
    record = [0, 0, 0]
    intro()
    playGame(record)
    
if __name__ == '__main__':
  main()
