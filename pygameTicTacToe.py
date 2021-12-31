"""pygame version of tictactoe"""
import pygame
import tictactoe
import AI

pygame.init()

screen = pygame.display.set_mode((800, 800))

clock = pygame.time.Clock()

pygame.display.set_caption("Tic-Tac-Toe")
font = pygame.font.Font('freesansbold.ttf', 32)
font2 = pygame.font.Font('freesansbold.ttf', 50)
image1 = pygame.image.load(r'taco.jpg')
image2 = pygame.image.load(r'oreo.jpg')
image3 = pygame.image.load(r'chloe.jpg')

board = tictactoe.newBoard()
availableMovesBoard = tictactoe.AvailableMoves(board)
turn = 0

choseDifficulty = False
chosePlayers = False
choseXorO = False
playGame = False

numPlayers = False
difficulty = False
playerXorO = False

def displayChloe():
    offset = 100
    screen.blit(image3, (800 / 2 - offset, 800 * (3 / 4) - offset))

def displayDraw():
    text = font2.render("It's a draw", True, (0, 255, 0))
    screen.blit(text, ((800 / 2) - 125, (800 / 2)))


def displayWinner(winner):
    if winner == 'X':
        player = 'Taco'
    else:
        player = 'Oreo'
    text = font2.render('{} wins the game'.format(player), True, (0, 255, 0))
    screen.blit(text, ((800 / 2) - 200, (800 / 2)))


def chosenXorO(position):
    if (800 / 2) - 10 < position[1] < (800 / 2) + 40:
        if (800 / 3) - 20 < position[0] < (800 / 3) + 80:
            return 'X'
        if (800 * (2 / 3)) - 20 < position[0] < (800 * (2 / 3)) + 80:
            return 'O'
    return


def chosenDifficulty(position):
    if (800 / 2) - 10 < position[1] < (800 / 2) + 40:
        if (800 / 3) - 110 < position[0] < (800 / 3) - 10:
            return 'easy'
        if (800 * (2 / 3)) - 110 < position[0] < (800 * (2 / 3)) - 10:
            return 'hard'
    return


def chosenPlayer(position):
    if (800 / 2) - 10 < position[1] < (800 / 2) + 40:  # if the y is within the box area
        if (800 / 4) - 110 < position[0] < (800 / 4) + 50:
            return 0
        elif (800 / 2) - 110 < position[0] < (800 / 2) + 50:
            return 1
        elif (800 * (3 / 4)) - 110 < position[0] < (800 * (3 / 4)) + 50:
            return 2
    return


def drawChoseXorO():
    text1 = font.render('Please choose the player you want', True, (0, 0, 0))
    text2 = font.render('Taco', True, (0, 0, 0))
    text3 = font.render('Oreo', True, (0, 0, 0))
    screen.blit(text1, ((800 / 4) - 100, 800 / 4))
    screen.blit(text2, ((800 / 3) - 10, 800 / 2))
    screen.blit(text3, ((800 * (2 / 3)) - 10, 800 / 2))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((800 / 3) - 20, (800 / 2) - 10, 100, 50), 2)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((800 * (2 / 3)) - 20, (800 / 2) - 10, 100, 50), 2)


def drawChosePlayer():
    text1 = font.render('Please choose the number of players', True, (0, 0, 0))
    text2 = font.render('0 Players', True, (0, 0, 0))
    text3 = font.render('1 Players', True, (0, 0, 0))
    text4 = font.render('2 Players', True, (0, 0, 0))
    screen.blit(text1, ((800 / 4) - 100, 800 / 4))
    screen.blit(text2, ((800 / 4) - 100, 800 / 2))
    screen.blit(text3, ((800 / 2) - 100, 800 / 2))
    screen.blit(text4, ((800 * (3 / 4)) - 100, 800 / 2))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((800 / 4) - 110, (800 / 2) - 10, 160, 50), 2)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((800 / 2) - 110, (800 / 2) - 10, 160, 50), 2)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((800 * (3 / 4)) - 110, (800 / 2) - 10, 160, 50), 2)
    return


def drawChoseDifficulty():
    text1 = font.render('Please choose the difficulty you want', True, (0, 0, 0))
    text2 = font.render('Easy', True, (0, 0, 0))
    text3 = font.render('Hard', True, (0, 0, 0))
    screen.blit(text1, ((800 / 4) - 100, 800 / 4))
    screen.blit(text2, ((800 / 3) - 100, 800 / 2))
    screen.blit(text3, ((800 * (2 / 3)) - 100, 800 / 2))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((800 / 3) - 110, (800 / 2) - 10, 100, 50), 2)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((800 * (2 / 3)) - 110, (800 / 2) - 10, 100, 50), 2)
    return


def drawO(position):
    # offset = (800 * (1 / 3)) / 4
    offset = 100
    screen.blit(image2, (position[0] - offset, position[1] - offset))
    """pygame.draw.circle(screen, (0, 0, 0), position, 80)
    pygame.draw.circle(screen, (255, 255, 255), position, 70)
"""


def drawX(position):
    # offset = (800 * (1 / 3)) / 4
    offset = 100
    screen.blit(image1, (position[0] - offset, position[1] - offset))
    """pygame.draw.lines(screen, (0, 0, 0), True,
                      [(position[0] - offset, position[1] - offset), (position[0] + offset, position[1] + offset)], 10)
    pygame.draw.lines(screen, (0, 0, 0), True,
                      [(position[0] + offset, position[1] - offset), (position[0] - offset, position[1] + offset)], 10)
"""


def validPosition(board, position):
    if 800 * (1 / 3) > position[1]:  # if the y axis is in the top row
        if 800 * (1 / 3) > position[0]:
            if board[0][0] == 'X' or board[0][0] == 'O':
                return False
        elif position[0] > 800 * (2 / 3):
            if board[0][2] == 'X' or board[0][2] == 'O':
                return False
        else:
            if board[0][1] == 'X' or board[0][1] == 'O':
                return False
    elif 800 * (1 / 3) < position[1] < 800 * (2 / 3):  # if the y axis is in the middle row
        if 800 * (1 / 3) > position[0]:
            if board[1][0] == 'X' or board[1][0] == 'O':
                return False
        elif position[0] > 800 * (2 / 3):
            if board[1][2] == 'X' or board[1][2] == 'O':
                return False
        else:
            if board[1][1] == 'X' or board[1][1] == 'O':
                return False
    else:  # if the y axis is in the bottom row
        if 800 * (1 / 3) > position[0]:
            if board[2][0] == 'X' or board[2][0] == 'O':
                return False
        elif position[0] > 800 * (2 / 3):
            if board[2][2] == 'X' or board[2][2] == 'O':
                return False
        else:
            if board[2][1] == 'X' or board[2][1] == 'O':
                return False
    return True


def placeMarker(board, position, turn):
    player = tictactoe.getPlayer(turn)
    if 800 * (1 / 3) > position[1]:  # if the y axis is in the top row
        if 800 * (1 / 3) > position[0]:
            board[0][0] = player
        elif position[0] > 800 * (2 / 3):
            board[0][2] = player
        else:
            board[0][1] = player
    elif 800 * (1 / 3) < position[1] < 800 * (2 / 3):  # if the y axis is in the middle row
        if 800 * (1 / 3) > position[0]:
            board[1][0] = player
        elif position[0] > 800 * (2 / 3):
            board[1][2] = player
        else:
            board[1][1] = player
    else:  # if the yaxis is in the bottom row
        if 800 * (1 / 3) > position[0]:
            board[2][0] = player
        elif position[0] > 800 * (2 / 3):
            board[2][2] = player
        else:
            board[2][1] = player


def drawBoard(board):
    # Draws the lines of the board
    pygame.draw.lines(screen, (0, 0, 0), True, [(800 * (1 / 3), 0), (800 * (1 / 3), 800)], 5)
    pygame.draw.lines(screen, (0, 0, 0), True, [(800 * (2 / 3), 0), (800 * (2 / 3), 800)], 5)
    pygame.draw.lines(screen, (0, 0, 0), True, [(0, 800 * (1 / 3)), (800, 800 * (1 / 3))], 5)
    pygame.draw.lines(screen, (0, 0, 0), True, [(0, 800 * (2 / 3)), (800, 800 * (2 / 3))], 5)

    # variables defined to make it easier to draw x's and o's in the middle of the square
    middleOfSquare = (800 * (1 / 3)) / 2
    offset = (800 * (1 / 3))

    # checks every spot in the board for an X or O and draws it if its there
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'X':
                drawX((middleOfSquare + offset * j, middleOfSquare + offset * i))
            elif board[i][j] == 'O':
                drawO((middleOfSquare + offset * j, middleOfSquare + offset * i))


# Game Loop

while True:
    winner = tictactoe.checkWinner(board)
    if numPlayers == 0 and 9 > turn and winner == False and playGame:
        clock.tick(2)
        if difficulty == 'easy':
            move = AI.easyAI(availableMovesBoard)
            board = tictactoe.makeMove(turn, move, board, availableMovesBoard)
            turn += 1
        elif difficulty == 'hard':
            move = AI.hardAI(availableMovesBoard, turn)
            board = tictactoe.makeMove(turn, move, board, availableMovesBoard)
            turn += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if chosePlayers and choseDifficulty and playGame and choseXorO:
            if playerXorO == 'O':
                if turn % 2 == 0:
                    if difficulty == 'easy':
                        move = AI.easyAI(availableMovesBoard)
                        board = tictactoe.makeMove(turn, move, board, availableMovesBoard)
                        turn += 1
                    elif difficulty == 'hard':
                        move = AI.hardAI(availableMovesBoard, turn)
                        board = tictactoe.makeMove(turn, move, board, availableMovesBoard)
                        turn += 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                if numPlayers == 2:
                    position = pygame.mouse.get_pos()
                    if validPosition(board, position):
                        placeMarker(board, position, turn)
                        turn += 1
                elif numPlayers == 1:
                    position = pygame.mouse.get_pos()
                    if validPosition(board, position):
                        placeMarker(board, position, turn)
                        turn += 1
                    if playerXorO == 'X':
                        if turn == 9 or tictactoe.checkWinner(board) != False:
                            break
                        if difficulty == 'easy':
                            move = AI.easyAI(availableMovesBoard)
                            board = tictactoe.makeMove(turn, move, board, availableMovesBoard)
                            turn += 1
                        elif difficulty == 'hard':
                            move = AI.hardAI(availableMovesBoard, turn)
                            board = tictactoe.makeMove(turn, move, board, availableMovesBoard)
                            turn += 1
        else:
            if not chosePlayers or not choseDifficulty or not choseXorO:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if not chosePlayers:
                        position = pygame.mouse.get_pos()
                        numPlayers = chosenPlayer(position)
                        if numPlayers == 0 or numPlayers == 1 or numPlayers == 2:
                            chosePlayers = True
                            if numPlayers == 2:
                                choseDifficulty = True
                                choseXorO = True
                                playGame = True
                    elif not choseDifficulty:
                        position = pygame.mouse.get_pos()
                        difficulty = chosenDifficulty(position)
                        if difficulty == 'easy' or difficulty == 'hard':
                            choseDifficulty = True
                            if numPlayers == 0:
                                choseXorO = True
                                playGame = True
                    elif not choseXorO:
                        position = pygame.mouse.get_pos()
                        playerXorO = chosenXorO(position)
                        if playerXorO == 'X' or playerXorO == 'O':
                            choseXorO = True
                            playGame = True
    if chosePlayers and choseDifficulty and playGame and choseXorO:
        screen.fill((255, 255, 255))
        drawBoard(board)
        pygame.display.update()
    else:
        screen.fill((255, 255, 255))
        if not choseXorO:  # if the player hasent been chosen
            displayChloe()
            if not choseDifficulty:  # if the difficulty hasn't been chosen
                if not chosePlayers:  # if the number of players hasent been chosen
                    drawChosePlayer()
                    pygame.display.update()
                else:  # if the number of players has been chosen then display the choose difficulty
                    drawChoseDifficulty()
                    pygame.display.update()
            else:  # if difficulty and players have been chosen
                drawChoseXorO()
                pygame.display.update()

    if winner is not False:
        playGame = False
        drawBoard(board)
        displayWinner(winner)
        pygame.display.update()
    if turn >= 9 and winner is False:
        playGame = False
        drawBoard(board)
        displayDraw()
        pygame.display.update()
