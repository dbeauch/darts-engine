from crick_bot import *

boardState1 = [0, 0, 0, 0, 0, 0, 0, 0]
boardState2 = [0, 0, 0, 0, 0, 0, 0, 0]
states = [boardState1, boardState2]

turn = 0
subTurn = 0

boardHistory1 = []
boardHistory2 = []
boardHistories = [boardHistory1, boardHistory2]


def updateBoard(value):
    thrower = turn % 2
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


def throw(score):
    global boardState1
    global boardState2
    thrower = turn % 2
    space = -1
    for i in range(len(score)):
        if score[i] == ' ':
            space = i
    value = score
    multiplier = 1
    if space != -1:
        value = score[:space]
        multiplier = int(score[space + 1:])
    if thrower == 0:
        boardHistory1.append(boardState1)
    else:
        boardHistory2.append(boardState2)
    for i in range(multiplier):
        updateBoard(value)
    printBoard()


def undo():  # Watch out, this is permanent
    global subTurn
    p = turn % 2
    states[p] = boardHistories[p][-2]
    boardHistories[p] = boardHistories[p][start:-1]
    subTurn -= 1


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


# Runs a game where player1 goes first for three throws followed by player2 for three throws until one party wins
def twoPlayers():
    global subTurn
    global turn
    global boardState1
    global boardState2
    while (boardState1[0:7] != [3, 3, 3, 3, 3, 3, 3]) and (boardState2[0:7] != [3, 3, 3, 3, 3, 3, 3]):
        throw(input("What number? "))
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
                throw(input("What number? "))
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
                throw(input("What number? "))
                subTurn += 1
                if subTurn % 3 == 0:
                    subTurn -= 3
                    turn += 1
        print(player1 + " wins!")


# Runs a game where the player goes first for three throws followed by the computer for three throws until one party wins
def onePlayer(difficulty):
    global subTurn
    global turn
    global boardState1
    global boardState2
    while (boardState1[0:7] != [3, 3, 3, 3, 3, 3, 3]) and (boardState2[0:7] != [3, 3, 3, 3, 3, 3, 3]):
        if turn % 2 == 0:
            throw(input("What number? "))
            subTurn += 1
            if subTurn % 3 == 0:
                subTurn -= 3
                turn += 1
        else:
            throw(shoot(boardState1, boardState2, difficulty))
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
                    throw(input("What number? "))
                    subTurn += 1
                    if subTurn % 3 == 0:
                        subTurn -= 3
                        turn += 1
                else:
                    throw(shoot(boardState1, boardState2, difficulty))
                    subTurn += 1
                    if subTurn % 3 == 0:
                        subTurn -= 3
                        turn += 1
        print("The computer wins!")
    else:
        while boardState1[0:7] != [3, 3, 3, 3, 3, 3, 3]:
            if boardState2[7] >= boardState1[7]:
                print("The computer wins!")
                print("Printing computer's shots:")
                return
            else:
                if turn % 2 == 0:
                    throw(input("What number? "))
                    subTurn += 1
                    if subTurn % 3 == 0:
                        subTurn -= 3
                        turn += 1
                else:
                    throw(shoot(boardState1, boardState2, difficulty))
                    subTurn += 1
                    if subTurn % 3 == 0:
                        subTurn -= 3
                        turn += 1
        print(player1 + " wins!")


thetheta = np.linspace(0, 2 * np.pi, 100)
radius0 = 225.5
radius1 = 170
radius2 = 162
radius3 = 107
radius4 = 99
radius5 = 16
radius6 = 6.35

a = radius0 * np.cos(thetheta)
b = radius0 * np.sin(thetheta)
c = radius1 * np.cos(thetheta)
d = radius1 * np.sin(thetheta)
e = radius2 * np.cos(thetheta)
f = radius2 * np.sin(thetheta)
g = radius3 * np.cos(thetheta)
h = radius3 * np.sin(thetheta)
i = radius4 * np.cos(thetheta)
j = radius4 * np.sin(thetheta)
k = radius5 * np.cos(thetheta)
l = radius5 * np.sin(thetheta)
m = radius6 * np.cos(thetheta)
n = radius6 * np.sin(thetheta)

figure, axes = plt.subplots(1)

axes.plot(a, b, color='black')
axes.plot(c, d, color='black')
axes.plot(e, f, color='black', linewidth=0.75)
axes.plot(g, h, color='black', linewidth=0.75)
axes.plot(i, j, color='black', linewidth=0.75)
axes.plot(k, l, color='black', linewidth=0.75)
axes.plot(m, n, color='black', linewidth=0.75)

axes.set_aspect(1)

x1 = np.linspace(-169, 169, 100)
y1 = -0.15838 * x1
plt.plot(x1, y1, 'k-', linewidth=0.5)

x2 = np.linspace(-167, 167, 100)
y2 = x2 * 0.15838
plt.plot(x2, y2, 'k-', linewidth=0.5)

x3 = np.linspace(-150, 150, 100)
y3 = x3 * 0.509525
plt.plot(x3, y3, 'k-', linewidth=0.5)

x4 = np.linspace(-120, 120, 100)
y4 = x4
plt.plot(x4, y4, 'k-', linewidth=0.5)

x5 = np.linspace(-78, 78, 100)
y5 = 1.96261 * x5
plt.plot(x5, y5, 'k-', linewidth=0.5)

x6 = np.linspace(-27, 27, 100)
y6 = 6.31375 * x6
plt.plot(x6, y6, 'k-', linewidth=0.5)

x7 = np.linspace(-27, 27, 100)
y7 = -6.31375 * x7
plt.plot(x7, y7, 'k-', linewidth=0.5)

x8 = np.linspace(-78, 78, 100)
y8 = -1.96261 * x8
plt.plot(x8, y8, 'k-', linewidth=0.5)

x9 = np.linspace(-120, 120, 100)
y9 = -1 * x9
plt.plot(x9, y9, 'k-', linewidth=0.5)

x10 = np.linspace(-150, 150, 100)
y10 = -0.509525 * x10
plt.plot(x10, y10, 'k-', linewidth=0.5)

plt.axis('off')

numPlayers = input("Number of players: ")
player1 = input("Player 1 name: ")
if numPlayers != "1":
    player2 = input("Player 2 name: ")
    players = [player1, player2]
    twoPlayers()
else:
    player2 = "Computer"
    difficulty = int(input("Enter difficulty (1-100): "))
    while not(0 < difficulty <= 100):
        difficulty = int(input("Enter difficulty (1-100): "))
    players = [player1, player2]
    onePlayer(difficulty)

plt.show()
