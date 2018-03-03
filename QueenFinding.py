import sys
import itertools

# Position 8 queens in chess board!

# Define the board with 64 positions
line = list(range(0,80))
board = [x for x in line if x % 10 < 8]
g_queens_all = []
g_queens = []
# print board

# isFound = False

def printPos(queens):
    # map the position to chess pos i.e. B5, etc
    line = list(range(0,80))
    board = [x for x in line if x % 10 < 8]

    board_with_queens = ["-" if x not in queens else "Q" for x in board]
    board_with_queens_m = [board_with_queens[i:i+8] for i in range(0,64,8)]

    for l in board_with_queens_m:
        print l

def __FindOccupied(board, pos):

    # Find occupied places
    board_occupied = [x for x in board if x / 10 == pos / 10 or \
                                          x % 10 == pos % 10 or \
                                          abs(x - pos) % 9 == 0 or \
                                          abs(x - pos) % 11 == 0]

    board_free = [x for x in board if x not in board_occupied]

    # print "board_occupied: " + str(board_occupied)
    # print "board_free: " + str(board_free)

    return (board_occupied, board_free)


def FindPos(board, round):
    # This function should:
    #   Find a position in the given board that the queenPos can survive
    global g_queens
    # global isFound

    indexes = range(0, len(board))
    # print "indexes length: " + str(len(indexes))

    ##############
    # Main logic
    #
    # loop all the remaining positions. For each one:
    # - remove all the covered/attacked positions from board
    # - if rest board is not empty, enter next call
    # - if rest board is empty, failed since not 8 queens found. isFound = False
    #   and return. Most importantly, remove last added queen from g_queens. It's
    #   because last added queen killed the try.
    #
    # NOTE: We should not stop traversing on the same root of the tree but
    #   instead just go back one level.
    ##############

    for i in indexes:

        # update position in the list and start traverse
        queenPos = board.pop(0)

        if len(g_queens) > 0 and queenPos == g_queens[-1]:
            print "yes! queenPos: " + str(queenPos)
            raw_input()

        g_queens.append(queenPos)

        ##############
        # Exit critieria for stopping the recursive call:
        #
        # Every time when we jump in one deeper level, we see if 8 queens are found (round 7).
        # If so we succeed and stop for current call
        #
        # NOTE: We should not stop traversing on the same root of the tree but
        #   instead just go back one level.
        ##############

        if round == 7:
            # we should have just one item in the list?
            if len(board) > 1:
                print "we have " + str(len(board)) + " left in board!"

            # isFound = True
            g_queens_all.append(sorted(g_queens))

            # print "g_queens" + str(g_queens)

            # raw_input()
            # recover the queens
            g_queens = g_queens[:-1]

            # print "queens:" + str(g_queens)
            # printPos(g_queens)
            # raw_input()
            return

        # print "Round: " + str(round) + " trying position: queenPos " + str(queenPos)
        # print "current board: " + str(board)

        board_occupied, board_free = __FindOccupied(board, queenPos)

        # print "FindPos before: round " + str(round) + " i " + str(i) + " board: " + str(board)

        if board_free:
            # now we haven't got 8 queens, continue traversing
            FindPos(board_free, round + 1)

        g_queens = g_queens[:-1]
        board.append(queenPos)

        # print "FindPos after: round " + str(round) + " i " + str(i) + " board: " + str(board) + " queenPos: " + str(queenPos)

FindPos(board, 0)

print str(len(g_queens_all)) + " solutions are found!"

g_queens_uni = list(g_queens_all for g_queens_all,_ in itertools.groupby(g_queens_all))

print str(len(g_queens_uni)) + " unique solutions are found!"
# print "g_queens_uni " + str(g_queens_uni)

#printPos(queenPos)
