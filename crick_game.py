player1 = input("Enter player 1: ")
player2 = input("Enter player 2: ")

boardState1 = [2, 3, 3, 3, 3, 3, 3, 0]
boardState2 = [3, 3, 3, 3, 3, 3, 2, 0]
turn = 0


def updateBoard(throw):
    if turn % 2 == 0:
        if throw == "15":
            if (boardState1[0] == 3) & (boardState2[0] != 3):
                boardState1[7] += 15
                return boardState1
            elif (boardState1[0] == 3) & (boardState2[0] == 3):
                return boardState1
            boardState1[0] += 1
        elif throw == "16":
            if (boardState1[1] == 3) & (boardState2[1] != 3):
                boardState1[7] += 16
                return boardState1
            elif (boardState1[1] == 3) & (boardState2[1] == 3):
                return boardState1
            boardState1[1] += 1
        elif throw == "17":
            if (boardState1[2] == 3) & (boardState2[2] != 3):
                boardState1[7] += 17
                return boardState1
            elif (boardState1[2] == 3) & (boardState2[2] == 3):
                return boardState1
            boardState1[2] += 1
        elif throw == "18":
            if (boardState1[3] == 3) & (boardState2[3] != 3):
                boardState1[7] += 18
                return boardState1
            elif (boardState1[3] == 3) & (boardState2[3] == 3):
                return boardState1
            boardState1[3] += 1
        elif throw == "19":
            if (boardState1[4] == 3) & (boardState2[4] != 3):
                boardState1[7] += 19
                return boardState1
            elif (boardState1[4] == 3) & (boardState2[4] == 3):
                return boardState1
            boardState1[4] += 1
        elif throw == "20":
            if (boardState1[5] == 3) & (boardState2[5] != 3):
                boardState1[7] += 20
                return boardState1
            elif (boardState1[5] == 3) & (boardState2[5] == 3):
                return boardState1
            boardState1[5] += 1
        elif throw == "25":
            if (boardState1[6] == 3) & (boardState2[6] != 3):
                boardState1[7] += 25
                return boardState1
            elif (boardState1[6] == 3) & (boardState2[6] == 3):
                return boardState1
            boardState1[6] += 1
        else:
            return boardState1
    else:
        if throw == "15":
            if (boardState2[0] == 3) & (boardState1[0] != 3):
                boardState2[7] += 15
                return boardState2
            elif (boardState2[0] == 3) & (boardState1[0] == 3):
                return boardState2
            boardState2[0] += 1
        elif throw == "16":
            if (boardState2[1] == 3) & (boardState1[1] != 3):
                boardState2[7] += 16
                return boardState2
            elif (boardState2[1] == 3) & (boardState1[1] == 3):
                return boardState2
            boardState2[1] += 1
        elif throw == "17":
            if (boardState2[2] == 3) & (boardState1[2] != 3):
                boardState2[7] += 17
                return boardState2
            elif (boardState2[2] == 3) & (boardState1[2] == 3):
                return boardState2
            boardState2[2] += 1
        elif throw == "18":
            if (boardState2[3] == 3) & (boardState1[3] != 3):
                boardState2[7] += 18
                return boardState2
            elif (boardState2[3] == 3) & (boardState1[3] == 3):
                return boardState2
            boardState2[3] += 1
        elif throw == "19":
            if (boardState2[4] == 3) & (boardState1[4] != 3):
                boardState2[7] += 19
                return boardState2
            elif (boardState2[4] == 3) & (boardState1[4] == 3):
                return boardState2
            boardState2[4] += 1
        elif throw == "20":
            if (boardState2[5] == 3) & (boardState1[5] != 3):
                boardState2[7] += 20
                return boardState2
            elif (boardState2[5] == 3) & (boardState1[5] == 3):
                return boardState2
            boardState2[5] += 1
        elif throw == "25":
            if (boardState2[6] == 3) & (boardState1[6] != 3):
                boardState2[7] += 25
                return boardState2
            elif (boardState2[6] == 3) & (boardState1[6] == 3):
                return boardState2
            boardState2[6] += 1
        else:
            return boardState2
    return 0


def throws():
    for i in range (0, 3):
        throw = input("Throw Value: ")
        updateBoard(throw)


def printBoard():
    if turn % 2 == 0:
        print(player1 + ":")
        print("15:", boardState1[0])
        print("16:", boardState1[1])
        print("17:", boardState1[2])
        print("18:", boardState1[3])
        print("19:", boardState1[4])
        print("20:", boardState1[5])
        print("Bullseye:", boardState1[6])
        print("Score:", boardState1[7])
    else:
        print(player2 + ":")
        print("15:", boardState2[0])
        print("16:", boardState2[1])
        print("17:", boardState2[2])
        print("18:", boardState2[3])
        print("19:", boardState2[4])
        print("20:", boardState2[5])
        print("Bullseye:", boardState2[6])
        print("Score:", boardState2[7])


def playGame():
    while (boardState1[0:7] != [3, 3, 3, 3, 3, 3, 3]) & (boardState2[0:7] != [3, 3, 3, 3, 3, 3, 3]):
        throws()
        printBoard()
        global turn
        turn += 1
    if boardState1[0:7] == [3, 3, 3, 3, 3, 3, 3]:
        while boardState2[0:7] != [3, 3, 3, 3, 3, 3, 3]:
            if boardState1[7] >= boardState2[7]:
                print(player1 + " wins!")
                break
            else:
                throws()
                printBoard()
                turn += 1
        print(player2 + " wins!")
    else:
        while boardState1[0:7] != [3, 3, 3, 3, 3, 3, 3]:
            if boardState2[7] >= boardState1[7]:
                print(player2 + " wins!")
                return
            else:
                throws()
                printBoard()
                turn += 1
        print(player1 + " wins!")



playGame()