## miniChessDriver.py
## version 0.1
## September 5, 2018

## Here's the crude, unpolished first version of a user
## interface for your miniChess function

## It doesn't really know much about who wins the game
## or when...although it does know that if it can't make
## a move, the human player wins.

## It does not validate the coordinates for the move
## that is entered by the user.  You can move any pawn
## on either side to any square.  So be careful.

## We have supplied "dummy" move_maker and
## move_chooser functions so that this
## program will run without causing an
## error.  But the program will not play
## the game correctly until you replace
## our two functions with your functions.

## Put your definitions for move_maker and
## move_chooser up here in this space.
##
## Replace the two function definitions below
## with your functions.
##
## DO NOT LEAVE OUR FUNCTIONS HERE

import copy

white=1
black=2
empty=0

def move_maker(board,color):
    
    indexr=0
    result=[]  
    original_board=copy.deepcopy(board)
    length=len(original_board)
    
    for row in original_board:
        
        indexc=0
        for col in row:
            
            if col == color:
                
                result.extend(move_piece(color, board, length, indexr, indexc))
            indexc+=1
        indexr+=1
    return result

def move_piece(color, board, length, indexr, indexc):
    
    if color == white:
        
        return movewht(board,length,indexr,indexc)
    
    elif color == black:
        
        return moveblk(board,length,indexr,indexc)

def movewht(board,length,indexr,indexc):
    
    moves=[]
    
    #move left if possible
    
    if check(board,length,indexr+1,indexc-1, black):
        #print('moving left')
        moves.append(mover(board,indexr,indexc,indexr+1,indexc-1))
    #move right if possible
    
    if check(board,length,indexr+1,indexc+1, black):
        
        moves.append(mover(board,indexr,indexc,indexr+1,indexc+1))
    #move foward if possible
    
    if check(board,length,indexr+1,indexc, empty):
        
        moves.append(mover(board,indexr,indexc,indexr+1,indexc))
    
        
    
    return moves

#black moves
def moveblk(board,length,indexr,indexc):
    
    moves = []
    
    
    #move left if possible
    if check(board,length,indexr-1,indexc-1, white):
        #print('moving left')
        moves.append(mover(board,indexr,indexc,indexr-1,indexc-1))
    
    #move right if possible    
    if check(board,length,indexr-1,indexc+1, white):
        #print('moving right')
        moves.append(mover(board,indexr,indexc,indexr-1,indexc+1))
    
    #move foward if possible
    if check(board,length,indexr-1,indexc, empty):
        
        moves.append(mover(board,indexr,indexc,indexr-1,indexc))
    
    return moves

#check blacks

def check(board, length, indexR, indexC, checkVal):
    
    withinBounds = False
    
    if indexR >= 0 and indexR < length:
        if indexC >= 0 and indexC < length:
            withinBounds = True
        
            
    
        

    if withinBounds:
        
        return board[indexR][indexC] == checkVal


#piece mover
def mover(mboard,mrow,mcol,mnrow,mncol):
    
    copy_mboard=copy.deepcopy(mboard)#makecopy
    copy_mboard[mnrow][mncol]=copy_mboard[mrow][mcol]
    copy_mboard[mrow][mcol]=0
    
    return copy_mboard  
                    
def move_chooser(boards,color):
    
    minimum=100
    indexD=0
    for boardIndex in range(len(boards)):
        count=0
        for line in boards[boardIndex]:
            for value in line:
                if value == color:
                    count+=1
        if count<minimum:
            minimum=count
            indexD=boardIndex
    return boards[indexD]
        
## keep everything below as is ======================================


## print a board
## 0 prints as '-', 1 prints as 'w', 2 prints as 'b'

def printBoard(board):
    print("   ", end = "")
    for i in range(0, len(board[0])):
        print(str(i)+" ", end = "")

    print("\n")
    row = 0
    for r in board:
        print(row, " ", end = "")
        for c in r:
            if c == 1:
                print("w ", end = "")
            elif c == 2:
                print("b ", end = "")
            else:
                print("- ", end = "")
        print()
        row = row + 1
    print()
            

## create an initial board, with dimension
## passed as the argument. 1s at the top,
## 2s at the bottom, 0s everywhere else
    
def makeInitBoard(dim):
    board = []
    for i in range(0,dim):
        row = []
        for j in range(0,dim):
            row.append(0)
        board.append(row)

    for i in range(0,dim):
        board[0][i] = 1
        board[dim - 1][i] = 2
        
    return board


## this is the user interface for the miniChess game.
## just run the program and type 'miniChess()' in the
## interaction window

def miniChess():
    from random import randint

    print("Welcome to miniChess")

    ## ask for board size and create initial board
    
    dim = int(input("What size board would you like? \n(enter an integer greater than 2): "))
    bheight = dim
    bwidth = dim
    b = makeInitBoard(dim)
    
    print("\nHere's the initial board...\n")
    
    printBoard(b)

    ## ask user to select color of pawns
    ## if user selects white, then the program's color is 2 (i.e., black)
    ## if user selects black, then the program's color is 1 (i.e., white)

    while True:
        answer = input("Choose the white pawns or black pawns (enter 'w' or 'b' or 'quit'): ")
        if answer == "w":
            mycolor = 2
            break
        if answer == "b":
            mycolor = 1
            break
        if answer == "quit":
            print("Ending the game")
            return

    ## if program has white pawns, generate program's first move

    if mycolor == 1:
        print("Here's my opening move...\n")
        column = randint(0, bwidth - 1)
        b[1][column] = b[0][column]
        b[0][column] = 0
        printBoard(b)

    ## game loop

    while True:
        
        ## ask for user's move
        ## coordinates are not validated at this time
        
        print("\nEnter the coordinates of the pawn you wish to move:")
        fromrow = int(input("   row: "))
        fromcol = int(input("   col: "))
        print("Enter the coordinates of the destination square: ")
        torow = int(input("   row: "))
        tocol = int(input("   col: ")) # oops
        b[torow][tocol] = b[fromrow][fromcol]
        b[fromrow][fromcol] = 0
        print("This is your move...\n")
        printBoard(b)

        ## here is where the program uses the functions created by the student
        
        possiblemoves = move_maker(b, mycolor)  # don't change this function call
        if possiblemoves == []:
            print("I can't move\nCongratulations! You win!")
            return
        b = move_chooser(possiblemoves, mycolor) # don't change this function call


        print("Here's my response...\n")
        printBoard(b)
    
