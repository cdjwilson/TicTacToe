""" Python tic-tac-toe Game
    X goes first
    O goes second
    first to get 3 in a row wins
    if all 9 squares are full and no one has 3 in a row then it is a draw"""
import AI


def getPlayer(turn):
    """Gets which players turn it is"""
    if turn % 2 == 0: return 'X'
    return 'O'


def AvailableMoves(board):
    """Prints a board that shows all available moves and has them numbered and returns that board"""
    count = 1
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '':
                board[i][j] = str(count)
                count += 1
    return board


def printBoard(board):
    """Prints the board"""
    for i in range(len(board)):
        print(board[i])
    print('\n')


def makeMove(turn, move, board, availableMovesBoard):
    """Finds what row and collum they are placing their move and places that in the board"""
    player = getPlayer(turn)
    for i in range(len(board)):
        for j in range(len(board[i])):
            if move == availableMovesBoard[i][j]:
                board[i][j] = player
                availableMovesBoard[i][j] = player
    return board


def validMove(move, availableMovesBoard):
    """Checks if the input move is in the available moves board"""
    for i in range(len(availableMovesBoard)):
        for j in range(len(availableMovesBoard[i])):
            if move == availableMovesBoard[i][j]:
                return True
    return False


def checkWinner(board):
    """Checks each row, collum, and diaganol to see if there is three in a row and if they are X's or O's"""
    if board[0][0] == board[0][1] and board[0][0] == board[0][2]:  # if the top row has three in a row
        if board[0][0] == 'O' or board[0][0] == 'X':
            return board[0][0]
    if board[1][0] == board[1][1] and board[1][0] == board[1][2]:  # if the middle row has three in a row
        if board[1][0] == 'O' or board[1][0] == 'X':
            return board[1][0]
    if board[2][0] == board[2][1] and board[2][0] == board[2][2]:  # if the bottom row has three in a row
        if board[2][0] == 'O' or board[2][0] == 'X':
            return board[2][0]
    if board[0][0] == board[1][0] and board[0][0] == board[2][0]:  # if the left collum has three in a row
        if board[0][0] == 'O' or board[0][0] == 'X':
            return board[0][0]
    if board[0][1] == board[1][1] and board[0][1] == board[2][1]:  # if the middle collum has three in a row
        if board[0][1] == 'O' or board[0][1] == 'X':
            return board[0][1]
    if board[0][2] == board[1][2] and board[0][2] == board[2][2]:  # if the right collum has three in a row
        if board[0][2] == 'O' or board[0][2] == 'X':
            return board[0][2]
    if board[0][0] == board[1][1] and board[0][0] == board[2][2]:  # if the diagonal from top left has three in a row
        if board[0][0] == 'O' or board[0][0] == 'X':
            return board[0][0]
    if board[0][2] == board[1][1] and board[0][2] == board[2][0]:  # if the diagonal from top right has three in a row
        if board[0][2] == 'O' or board[0][2] == 'X':
            return board[0][2]
    return False


def newBoard():
    tboard = [['', '', ''],
              ['', '', ''],
              ['', '', '']]
    return tboard


def play(numPlayers=1):
    '''Starts the game, number of players may be specified between 0 and 2 '''
    turn = 0
    board = newBoard()
    availableMovesBoard = AvailableMoves(newBoard())
    printBoard(board)
    if numPlayers == 2:
        while 9 > turn:
            print("The possible moves for {} are:".format(getPlayer(turn)))
            printBoard(availableMovesBoard)

            move = input("Please choose a move by entering the number where you want to play: ")
            while not validMove(move, availableMovesBoard):
                move = input("That is not a valid move, Please choose a valid move: ")
            board = makeMove(turn, move, board, availableMovesBoard)

            print("Current state of the board")
            printBoard(board)

            winner = checkWinner(board)
            if winner != False:
                return "{} Wins the game".format(winner)
            turn += 1
    elif numPlayers == 1:
        difficulty = input("What difficulty would you like, Easy or Hard, please type easy or hard: ").lower()
        while difficulty != 'easy' and difficulty != 'hard':
            difficulty = input("Please type either 'easy' or 'hard': ").lower()
        player = input("Do you want to be X or O, please type X or O: ").upper()
        while player != 'X' and player != 'O':
            player = input("Please type either X or O: ").upper()
        if player == 'X':
            while 9 > turn:
                print("The possible moves for you are: ")
                printBoard(availableMovesBoard)

                move = input("Please choose a move by entering the number where you want to play: ")
                while not validMove(move, availableMovesBoard):
                    move = input("That is not a valid move, Please choose a valid move: ")
                board = makeMove(turn, move, board, availableMovesBoard)

                if checkWinner(board):
                    return "{} Wins the game".format(getPlayer(turn))
                turn += 1

                print("Current state of the board")
                printBoard(board)

                print("AI is making their move")
                if difficulty == 'easy':
                    move = AI.easyAI(availableMovesBoard)
                    board = makeMove(turn, move, board, availableMovesBoard)
                else:
                    move = AI.hardAI(availableMovesBoard, turn)
                    board = makeMove(turn, move, board, availableMovesBoard)

                print("Current state of the board")
                printBoard(board)

                winner = checkWinner(board)
                if winner != False:
                    return "{} Wins the game".format(winner)
                turn += 1
        else:
            while 9 > turn:
                print("AI is making their move")
                if difficulty == 'easy':
                    move = AI.easyAI(availableMovesBoard)
                    board = makeMove(turn, move, board, availableMovesBoard)
                else:
                    move = AI.hardAI(availableMovesBoard, turn)
                    board = makeMove(turn, move, board, availableMovesBoard)

                print("Current state of the board")
                printBoard(board)

                if checkWinner(board):
                    return "{} wins the game".format(getPlayer(turn))
                turn += 1
                if 9 == turn:
                    return "It's a draw"
                print("The possible moves for you are: ")
                printBoard(availableMovesBoard)

                move = input("Please choose a move by entering the number where you want to play: ")
                while not validMove(move, availableMovesBoard):
                    move = input("That is not a valid move, Please choose a valid move: ")
                board = makeMove(turn, move, board, availableMovesBoard)

                print("Current state of the board")
                printBoard(board)

                winner = checkWinner(board)
                if winner != False:
                    return "{} wins the game".format(winner)
                turn += 1
    elif numPlayers == 0:
        difficulty = input("What difficulty would you like, Easy or Hard, please type easy or hard: ").lower()
        while difficulty != 'easy' and difficulty != 'hard':
            difficulty = input("Please type either 'easy' or 'hard': ").lower()
        while 9 > turn:
            if difficulty == 'easy':
                move = AI.easyAI(availableMovesBoard)
                board = makeMove(turn, move, board, availableMovesBoard)
            else:
                move = AI.hardAI(availableMovesBoard, turn)
                board = makeMove(turn, move, board, availableMovesBoard)

            print("Current state of the board")
            printBoard(board)

            winner = checkWinner(board)
            if winner != False:
                return "{} wins the game".format(winner)
            turn += 1
    return "It's a draw"
