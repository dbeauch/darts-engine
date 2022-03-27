player1 = "Kieran"
player2 = "Ethan"
players = [player1, player2]

boardState1 = [0, 0, 0, 3, 0, 0, 0, 0]
boardState2 = [0, 0, 0, 0, 0, 0, 0, 0]
states = [boardState1, boardState2]

turn = 0
subTurn = 0

boardHistory1 = []
boardHistory2 = []
boardHistories = [boardHistory1, boardHistory2]


def updateBoard(value):
    thrower = turn % 2
    if thrower == 0:
        boardHistory1.append(boardState1)
    else:
        boardHistory2.append(boardState2)
    if value == "15":
        if (states[thrower][0] == 3) and (states[1 if thrower == 0 else 0][0] != 3):
            states[thrower][7] += 15
            return states[thrower]
        elif (states[thrower][0] == 3) and (states[1 if thrower == 0 else 0][0] == 3):
            return states[thrower]
        states[thrower][0] += 1
    elif value == "16":
        if (states[thrower][1] == 3) and (states[1 if thrower == 0 else 0][1] != 3):
            states[thrower][7] += 16
            return states[thrower]
        elif (states[thrower][1] == 3) and (states[1 if thrower == 0 else 0][1] == 3):
            return states[thrower]
        states[thrower][1] += 1
    elif value == "17":
        if (states[thrower][2] == 3) and (states[1 if thrower == 0 else 0][2] != 3):
            states[thrower][7] += 17
            return states[thrower]
        elif (states[thrower][2] == 3) and (states[1 if thrower == 0 else 0][2] == 3):
            return states[thrower]
        states[thrower][2] += 1
    elif value == "18":
        if (states[thrower][3] == 3) and (states[1 if thrower == 0 else 0][3] != 3):
            states[thrower][7] += 18
            return states[thrower]
        elif (states[thrower][3] == 3) and (states[1 if thrower == 0 else 0][3] == 3):
            return states[thrower]
        states[thrower][3] += 1
    elif value == "19":
        if (states[thrower][4] == 3) and (states[1 if thrower == 0 else 0][4] != 3):
            states[thrower][7] += 19
            return states[thrower]
        elif (states[thrower][4] == 3) and (states[1 if thrower == 0 else 0][4] == 3):
            return states[thrower]
        states[thrower][4] += 1
    elif value == "20":
        if (states[thrower][5] == 3) and (states[1 if thrower == 0 else 0][5] != 3):
            states[thrower][7] += 20
            return states[thrower]
        elif (states[thrower][5] == 3) and (states[1 if thrower == 0 else 0][5] == 3):
            return states[thrower]
        states[thrower][5] += 1
    elif value == "25":
        if (states[thrower][6] == 3) and (states[1 if thrower == 0 else 0][6] != 3):
            states[thrower][7] += 25
            return states[thrower]
        elif (states[thrower][6] == 3) and (states[1 if thrower == 0 else 0][6] == 3):
            return states[thrower]
        states[thrower][6] += 1
    return 0


def throw(x):
    score = x  # From gui
    space = -1
    for i in range(len(score)):
        if score[i] == ' ':
            space = i
    value = score
    multiplier = 1
    if space != -1:
        value = score[:space]
        multiplier = int(score[space + 1:])
    for i in range(multiplier):
        updateBoard(value)
    printBoard()


def undo():  # Watch out, this is permanent
    p = turn % 2
    states[p] = boardHistories[p][-2]
    boardHistories[p] = boardHistories[p][start:-1]


def printBoard():
    p = turn % 2
    print(players[p] + "'s scores:")
    print("15:", states[p][0])
    print("16:", states[p][1])
    print("17:", states[p][2])
    print("18:", states[p][3])
    print("19:", states[p][4])
    print("20:", states[p][5])
    print("Bullseye:", states[p][6])
    print("Score:", states[p][7])


def twoPlayers():
    global subTurn
    global turn
    while (boardState1[0:7] != [3, 3, 3, 3, 3, 3, 3]) and (boardState2[0:7] != [3, 3, 3, 3, 3, 3, 3]):
        throw()
        subTurn += 1
        if subTurn % 3 == 0:
            subTurn -= 3
            turn += 1
    if boardState1[0:7] == [3, 3, 3, 3, 3, 3, 3]:
        while boardState2[0:7] != [3, 3, 3, 3, 3, 3, 3]:
            if boardState1[7] >= boardState2[7]:
                print(player1 + " wins!")
                return
            else:
                throw()
                subTurn += 1
                if subTurn % 3 == 0:
                    subTurn -= 3
                    turn += 1
        print(player2 + " wins!")
    else:
        while boardState1[0:7] != [3, 3, 3, 3, 3, 3, 3]:
            if boardState2[7] >= boardState1[7]:
                print(player2 + " wins!")
                return
            else:
                throw()
                subTurn += 1
                if subTurn % 3 == 0:
                    subTurn -= 3
                    turn += 1
        print(player1 + " wins!")


def onePlayer():
    global subTurn
    global turn
    while (boardState1[0:7] != [3, 3, 3, 3, 3, 3, 3]) and (boardState2[0:7] != [3, 3, 3, 3, 3, 3, 3]):
        if turn % 2 == 0:
            throw()
            subTurn += 1
            if subTurn % 3 == 0:
                subTurn -= 3
                turn += 1
        else:
            AIthrow()
            subTurn += 1
            if subTurn % 3 == 0:
                subTurn -= 3
                turn += 1
    if boardState1[0:7] == [3, 3, 3, 3, 3, 3, 3]:
        while boardState2[0:7] != [3, 3, 3, 3, 3, 3, 3]:
            if boardState1[7] >= boardState2[7]:
                print(player1 + " wins!")
                return
            else:
                if turn % 2 == 0:
                    throw()
                    subTurn += 1
                    if subTurn % 3 == 0:
                        subTurn -= 3
                        turn += 1
                else:
                    AIthrow()
                    subTurn += 1
                    if subTurn % 3 == 0:
                        subTurn -= 3
                        turn += 1
        print("The computer wins!")
    else:
        while boardState1[0:7] != [3, 3, 3, 3, 3, 3, 3]:
            if boardState2[7] >= boardState1[7]:
                print("The computer wins!")
                return
            else:
                if turn % 2 == 0:
                    throw()
                    subTurn += 1
                    if subTurn % 3 == 0:
                        subTurn -= 3
                        turn += 1
                else:
                    AIthrow()
                    subTurn += 1
                    if subTurn % 3 == 0:
                        subTurn -= 3
                        turn += 1
        print(player1 + " wins!")
