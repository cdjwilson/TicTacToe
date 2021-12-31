"""Ai player for tic-tac-toe"""
import random
import tictactoe
from numba import jit

def easyAI(availableMovesBoard):
    # Take the moves that are available
    availableMovesForAI = []

    # Go through the given board and add all the availble moves into a list
    for i in range(len(availableMovesBoard)):
        for j in range(len(availableMovesBoard[i])):
            if availableMovesBoard[i][j] != 'X' and availableMovesBoard[i][j] != 'O':
                availableMovesForAI.append(availableMovesBoard[i][j])

    # pick a random number from 0 to the length of the list and return the move for that index
    randomPick = random.randint(0, len(availableMovesForAI) - 1)
    return availableMovesForAI[randomPick]

def bestMove(availableMovesBoard, turn, ai):
    player = tictactoe.getPlayer(turn)
    bestValue = -1000
    bestMove = (-1, -1)
    for i in range(len(availableMovesBoard)):
        for j in range(len(availableMovesBoard[i])):
            if availableMovesBoard[i][j] != 'X' and availableMovesBoard[i][j] != 'O':
                move = availableMovesBoard[i][j]
                availableMovesBoard[i][j] = player
                moveValue = minimax(availableMovesBoard, False, turn + 1, ai)
                availableMovesBoard[i][j] = move
                if moveValue > bestValue:
                    bestMove = (i, j)
                    bestValue = moveValue
    return bestMove

def minimax(availableMovesBoard, maximizingPlayer, turn, ai):
    player = tictactoe.getPlayer(turn)
    winner = tictactoe.checkWinner(availableMovesBoard)
    if winner != False:
        if winner == ai: return 10 - turn
        return -10
    if 9 == turn:
        return 0

    if (maximizingPlayer):
        bestValue = -1000
        for i in range(len(availableMovesBoard)):
            for j in range(len(availableMovesBoard[i])):
                if availableMovesBoard[i][j] != 'X' and availableMovesBoard[i][j] != 'O':
                    move = availableMovesBoard[i][j]
                    availableMovesBoard[i][j] = player
                    bestValue = max(bestValue, minimax(availableMovesBoard, False, turn + 1, ai))
                    availableMovesBoard[i][j] = move
        return bestValue
    else:
        bestValue = 1000
        for i in range(len(availableMovesBoard)):
            for j in range(len(availableMovesBoard[i])):
                if availableMovesBoard[i][j] != 'X' and availableMovesBoard[i][j] != 'O':
                    move = availableMovesBoard[i][j]
                    availableMovesBoard[i][j] = player
                    bestValue = min(bestValue, minimax(availableMovesBoard, True, turn + 1, ai))
                    availableMovesBoard[i][j] = move
        return bestValue


def hardAI(availableMovesBoard, turn):
    ai = tictactoe.getPlayer(turn)
    bestMoveForAi = bestMove(availableMovesBoard, turn, ai)
    return availableMovesBoard[bestMoveForAi[0]][bestMoveForAi[1]]
