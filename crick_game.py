player = input("Enter a player: ")

boardState = [0, 0, 0, 0, 0, 0, 0]


def updateBoard(throw):
    if throw == "15":
        boardState[0] += 1
    elif throw == "16":
        boardState[1] += 1
    elif throw == "17":
        boardState[2] += 1
    elif throw == "18":
        boardState[3] += 1
    elif throw == "19":
        boardState[4] += 1
    elif throw == "20":
        boardState[5] += 1
    elif throw == "25":
        boardState[6] += 1
    else:
        return boardState
    return boardState


def throw():
    throw = input("Throw Value: ")
    updateBoard(throw)


def printBoard():
    print("15:", boardState[0])
    print("16:", boardState[1])
    print("17:", boardState[2])
    print("18:", boardState[3])
    print("19:", boardState[4])
    print("20:", boardState[5])
    print("Bullseye:", boardState[6])


def playGame():
    while boardState != "3333333":
        throw()
        printBoard()
    print("You win!")


playGame()
