import random

board = [" "," "," ",
         " "," "," ",
         " "," "," "]

currentPlayer = "X"

winner = None
gameRunning = True
# printing the game board
def printBoard(board):
    print(board[0]+" | " + board[1] +" | "+ board[2])
    print("---------")
    print(board[3]+" | " + board[4] +" | "+ board[5])
    print("---------")
    print(board[6]+" | " + board[7] +" | "+ board[8])

# take player input
def playerInput(board):
    inp = int(input("Enter a number 1-9: "))
    if inp >=1 and inp <= 9 and board[inp-1] == " ":
        board[inp-1] = currentPlayer
    else:
        print("Oops player is already in that spot")

def checkHorizontal(board):
    global winner 
    if board[0] == board[1] == board[2] and board[0] != " ":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] !=" ":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] !=" ":
        winner = board[3]
        return True
def checkRow (board):
    global winner
    if board[0] == board[3] == board[6] and board[0] !=" ":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] !=" ":
        winner = board[3]
        return True
    elif board[2] == board[5] == board[8] and board[2] !=" ":
        winner = board[3]
        return True
def checkDiagnol(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] !=" ":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] !=" ":
        winner = board[3]
        return True
def checkTie(board):
    global gameRunning 
    if " " not in board:
        printBoard(board)
        print("its a tie")
        gameRunning = False

def checkForWin():
    if checkDiagnol(board)  or checkHorizontal(board) or checkDiagnol(board):
        print(f"The winner is {winner}")

def switchPlayer():
    global currentPlayer
    if currentPlayer =="X":
        currentPlayer = "O"
    else:
        currentPlayer ="X"

def computer(board):
    while currentPlayer =="O":
        position = random.randint(0,8)
        if board[position] ==" ":
            board[position] = "O"
            switchPlayer()






# check for win or tie

# switch the player

# check for win or tie again




while gameRunning:
    printBoard(board)
    playerInput( board)
    checkForWin()
    checkTie(board)
    switchPlayer()
    computer(board)
    checkForWin()
    checkTie(board)
        



