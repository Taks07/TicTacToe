import copy, random, sys
from tkinter import *

root = Tk()
root.title("Tic-Tac-Toe")

size = 10

TurnLabel = Label(root)
ULButton = Button(root, width = size, height = int(size/2), state = DISABLED)
UMButton = Button(root, width = size, height = int(size/2), state = DISABLED)
URButton = Button(root, width = size, height = int(size/2), state = DISABLED)

MLButton = Button(root, width = size, height = int(size/2), state = DISABLED)
MMButton = Button(root, width = size, height = int(size/2), state = DISABLED)
MRButton = Button(root, width = size, height = int(size/2), state = DISABLED)

LLButton = Button(root, width = size, height = int(size/2), state = DISABLED)
LMButton = Button(root, width = size, height = int(size/2), state = DISABLED)
LRButton = Button(root, width = size, height = int(size/2), state = DISABLED)

TurnLabel.grid(column = 0, row = 3, columnspan = 3)
ULButton.grid(column = 0, row = 0)
UMButton.grid(column = 0, row = 1)
URButton.grid(column = 0, row = 2)

MLButton.grid(column = 1, row = 0)
MMButton.grid(column = 1, row = 1)
MRButton.grid(column = 1, row = 2)

LLButton.grid(column = 2, row = 0)
LMButton.grid(column = 2, row = 1)
LRButton.grid(column = 2, row = 2)




def DisplayBoard():
    ULButton.config(text = TheBoard["UL"])
    UMButton.config(text = TheBoard["UM"])
    URButton.config(text = TheBoard["UR"])

    MLButton.config(text = TheBoard["ML"])
    MMButton.config(text = TheBoard["MM"])
    MRButton.config(text = TheBoard["MR"])

    LLButton.config(text = TheBoard["LL"])
    LMButton.config(text = TheBoard["LM"])
    LRButton.config(text = TheBoard["LR"])

def CheckEnd():
    global end
    if not NotWin or Draw:
        end = Toplevel(root)
        end.title("Game has ended.")
        end.attributes('-topmost', True)
        
        label = Label(end)
        label.grid(column = 0, row = 0, columnspan = 2)
        
        if Draw and NotWin:
            label.config(text = "It was a draw")

        else:
            win = turn + " won the game!"
            label.config(text = win)
            
        ULButton.config(state = DISABLED)
        UMButton.config(state = DISABLED)
        URButton.config(state = DISABLED)

        MLButton.config(state = DISABLED)
        MMButton.config(state = DISABLED)
        MRButton.config(state = DISABLED)

        LLButton.config(state = DISABLED)
        LMButton.config(state = DISABLED)
        LRButton.config(state = DISABLED)
        
        RestartAIButton = Button(end, text = "Restart AI Game", command = lambda: AIRestart("end"))
        RestartPlayerButton = Button(end, text = "Restart Player Game", command = lambda: PlayerRestart("end"))
        EndButton = Button(end, text = "Close Program", command = root.destroy)
        
        RestartAIButton.grid(column = 0, row = 1)
        RestartPlayerButton.grid(column = 1, row = 1)
        EndButton.grid(column = 0, row = 2, columnspan = 2)

        
def Restart(N):
    global turn, NotWin, Draw, TheBoard
    
    root.attributes('-topmost', True)
    root.after_idle(root.attributes, '-topmost', False)

    if N == "option":
        option.destroy()

    else:
        end.destroy()
        
    
    TheBoard = {"UL":" ", "UM": " ", "UR": " ",
                "ML":" ", "MM": " ", "MR": " ",
                "LL":" ", "LM": " ", "LR": " "}

    turn = "X"
    NotWin = True
    Draw = False

    turntext = "It is " + turn + "'s turn now!"
    TurnLabel.config(text = turntext)    
    
    DisplayBoard()
            
def AIRestart(N):
    Restart(N)
    ULButton.config(command = lambda: AIGetInput("UL"), state = NORMAL)
    UMButton.config(command = lambda: AIGetInput("UM"), state = NORMAL)
    URButton.config(command = lambda: AIGetInput("UR"), state = NORMAL)

    MLButton.config(command = lambda: AIGetInput("ML"), state = NORMAL)
    MMButton.config(command = lambda: AIGetInput("MM"), state = NORMAL)
    MRButton.config(command = lambda: AIGetInput("MR"), state = NORMAL)

    LLButton.config(command = lambda: AIGetInput("LL"), state = NORMAL)
    LMButton.config(command = lambda: AIGetInput("LM"), state = NORMAL)
    LRButton.config(command = lambda: AIGetInput("LR"), state = NORMAL)

def PlayerRestart(N):
    Restart(N)
    ULButton.config(command = lambda: PlayerGetInput("UL"), state = NORMAL)
    UMButton.config(command = lambda: PlayerGetInput("UM"), state = NORMAL)
    URButton.config(command = lambda: PlayerGetInput("UR"), state = NORMAL)

    MLButton.config(command = lambda: PlayerGetInput("ML"), state = NORMAL)
    MMButton.config(command = lambda: PlayerGetInput("MM"), state = NORMAL)
    MRButton.config(command = lambda: PlayerGetInput("MR"), state = NORMAL)

    LLButton.config(command = lambda: PlayerGetInput("LL"), state = NORMAL)
    LMButton.config(command = lambda: PlayerGetInput("LM"), state = NORMAL)
    LRButton.config(command = lambda: PlayerGetInput("LR"), state = NORMAL)

    
def AIGetInput(I):
    global TheBoard, turn

    if TheBoard[I] != " ":
        return

    
        
    TheBoard[I] = turn    
        
    DisplayBoard()
    CheckBoard(TheBoard)
    CheckEnd()
    
    if not NotWin or Draw:
        return
    
    turn = ChangeTurn()

    
    AIMove()
    DisplayBoard()
    CheckBoard(TheBoard)
    CheckEnd()

    if not NotWin or Draw:
        return

    turn = ChangeTurn()
    turntext = "It is " + turn + "'s turn now!"
    TurnLabel.config(text = turntext)

def PlayerGetInput(I):
    global TheBoard, turn
    
    if TheBoard[I] != " ":
        return

    TheBoard[I] = turn

    DisplayBoard()
    CheckBoard(TheBoard)
    CheckEnd()

    turn = ChangeTurn()
    turntext = "It is " + turn + "'s turn now!"
    TurnLabel.config(text = turntext)
    
def ChangeTurn():
    if turn == "X":
        nextturn = "O"

    else:
        nextturn = "X"

    return nextturn

def CheckFullBoard():
    global Draw
    Draw = True
    
    board = list(TheBoard.values())
    for i in board:
        if i == " ":
            Draw = False
            break

def CheckRows(myBoard):
    global NotWin
    board = list(myBoard.values())
    for i in range(0,9,3):
        if board[i] == board[i+1] and board[i] == board[i+2] and board[i] != " ":
            NotWin =  False
            break


def CheckColumns(myBoard):
    global NotWin
    board = list(myBoard.values())
    for i in range(3):
        if board[i] == board[i+3] and board[i] == board[i+6] and board[i] != " ":
            NotWin = False
            break
        
def CheckDiagonals(myBoard):
    global NotWin
    board = list(myBoard.values())
    if (board[0] == board[4] and board[0] == board[8] and board[0] != " ") or (board[2] == board[4] and board[2] == board[6] and board[2] != " "):
        NotWin = False
    
def CheckBoard(myBoard):
    CheckFullBoard()
    CheckRows(myBoard)
    CheckColumns(myBoard)
    CheckDiagonals(myBoard)

def AICheckWin():
    global NotWin
    board = copy.deepcopy(TheBoard)
    
    for i in ("UL", "UM", "UR", "ML", "MM", "MR", "LL", "LM", "LR"):
        board[i] = turn
        CheckBoard(board)
        
        if NotWin == False and TheBoard[i] == " ":
            TheBoard[i] = turn
            NotWin = True
            return True
            break

        else:
            NotWin = True

        board = copy.deepcopy(TheBoard)
        
def AICheckPlayerWin():
    global NotWin
    board = copy.deepcopy(TheBoard)
    playerturn = ChangeTurn()

    for i in ("UL", "UM", "UR", "ML", "MM", "MR", "LL", "LM", "LR"):
        board[i] = playerturn
        CheckBoard(board)
        
        if NotWin == False and TheBoard[i] == " ":
            TheBoard[i] = turn
            NotWin = True
            return True
            break

        else:
            NotWin = True

        board = copy.deepcopy(TheBoard)

def AIRandomMove():
    move = random.choice(("UL", "UM", "UR", "ML", "MM", "MR", "LL", "LM", "LR"))

    while TheBoard[move] != " ":
        move = random.choice(("UL", "UM", "UR", "ML", "MM", "MR", "LL", "LM", "LR"))
        
    TheBoard[move] = turn

    
def AIMove():
    if not AICheckWin():
        if not AICheckPlayerWin():
            if TheBoard["MM"] == " ":
                TheBoard["MM"] = turn

            else:
                AIRandomMove()    

option = Toplevel(root)
option.title("Choose game mode.")

option.attributes('-topmost', True)


RestartAIButton = Button(option, text = "Play AI Game", command = lambda: AIRestart("option"))
RestartPlayerButton = Button(option, text = "Play Player Game", command = lambda: PlayerRestart("option"))

RestartAIButton.grid(column = 0, row = 0)
RestartPlayerButton.grid(column = 1, row = 0)



