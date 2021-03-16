board=["1","2","3","4","5","6","7","8","9"]

currentPlayer="X"

def displayBoard():
    print("| "+board[0]+" | "+board[1]+" | "+board[2]+" |")
    print("| "+board[3]+" | "+board[4]+" | "+board[5]+" |")
    print("| "+board[6]+" | "+board[7]+" | "+board[8]+" |")


def gameChecker():
    if (board[0]==board[1]==board[2] 
    or board[3]==board[4]==board[5] 
    or board[6]==board[7]==board[8] 
    or board[0]==board[3]==board[6] 
    or board[1]==board[4]==board[7] 
    or board[2]==board[5]==board[8]
    or board[0]==board[4]==board[8] 
    or board[2]==board[4]==board[6]):
        print("The winner is {}".format(currentPlayer))
        displayBoard();
    else:
        playerSwitcher();
        startGame();
        

def playerSwitcher():
    global currentPlayer
    if currentPlayer=="X":
        currentPlayer="O"
    else:
        currentPlayer="X"

def playGame():
    pos=input("Type number where you want to play {} :".format(currentPlayer))
    board[int(pos)-1]=currentPlayer

def startGame():
    displayBoard();
    playGame();
    gameChecker();


startGame()



