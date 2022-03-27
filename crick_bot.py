import math
import random
import numpy as np
from matplotlib import pyplot as plt

radius = 170
test_boardState1 = [3, 3, 3, 3, 3, 3, 2, 15]
test_boardState2 = [2, 2, 3, 3, 3, 3, 3, 15]


class Coord:
    radius = 0.0
    theta = 0.0
    radial = True
    x = 0.0
    y = 0.0

    def __init__(self, radial, rx, ty):
        if radial:
            self.radius = rx
            self.theta = ty
            self.x = convertToX(self)
            self.y = convertToY(self)
        else:
            self.x = rx
            self.y = ty
            self.radius = convertToR(self)
            self.theta = convertToTheta(self)


def convertToX(coord):
    return coord.radius * math.cos(coord.theta)


def convertToY(coord):
    return coord.radius * math.sin(coord.theta)


def convertToR(coord):
    return abs(math.sqrt(math.pow(coord.x, 2) + math.pow(coord.y, 2)))


def convertToTheta(coord):
    result = math.atan2(coord.y, coord.x)
    if result < 0.0:
        result += 2 * math.pi
    # if coord.y < 0 and coord.x < 0:
    #    result += math.pi
    # if result > 2 * math.pi:
    #    result -= 2 * math.pi
    return result


# Plot board BEN PUT IT HERE

# counter = 10
# while counter > 0:
#     plt.plot(random.vonmisesvariate((math.pi)/2, 6), random.vonmisesvariate(math.pi, 1), 'rx')
#     counter -= 1


def getValue(target):
    if target == 6:
        return 25
    else:
        return target + 15


# default to highest possible scoring target


def findTarget1(state1, state2):
    target = 6
    for index in range(len(state1) - 3, -1, -1):
        if state1[index] < 3:
            target = index
            break
    target = 6
    for index in range(len(state2) - 3, -1, -1):
        if state2[index] < 3:
            target = index
            break
    return target


def findTarget2(state1, state2):
    target = 6
    for index in range(len(state2) - 1, -1, -1):
        if state2[index] < 3:
            target = index
            break
    return target


def findTarget3(state1, state2):
    target = 6
    for index in range(len(state2) - 1, -1, -1):
        if state1[index] == 3 and state2[index] < 3:
            target = index
            break
    return target


# def easy_calculateShot(target):
#     target = getValue(target)
#     if target <= 20:
#         if random.random() <= 0.15:
#             return target
#         else:
#             return 0
#     else:
#         if random.random() <= 0.05:
#             return target
#         else:
#             return 0
#
#
# def medium_calculateShot(target):
#     target = getValue(target)
#     if target <= 20:
#         if random.random() <= 0.25:
#             return target
#         else:
#             return 0
#     else:
#         if random.random() <= 0.10:
#             return target
#         else:
#             return 0
#
#
# def hard_calculateShot(target):
#     target = getValue(target)
#     if target <= 20:
#         if random.random() <= 0.99:
#             return target
#         else:
#             return 0
#     else:
#         if random.random() <= 0.15:
#             return target
#         else:
#             return 0


tripRadius = 103
targetList = [Coord(True, tripRadius, 9 * math.pi / 5), Coord(True, tripRadius, 6 * math.pi / 5),
              Coord(True, tripRadius, 8 * math.pi / 5), Coord(True, tripRadius, 3 * math.pi / 10),
              Coord(True, tripRadius, 7 * math.pi / 5), Coord(True, tripRadius, math.pi / 2),
              Coord(True, 0, math.pi / 2)]


def calculateShot(coord):
    result = ""
    hit = False
    #print(coord.radius, " ", coord.theta)
    if coord.radius <= radius:
        if 9 * math.pi / 20 <= coord.theta <= 11 * math.pi / 20:
            result += "20"
            hit = True
        elif 27 * math.pi / 20 <= coord.theta <= 29 * math.pi / 20:
            result += "19"
            hit = True
        elif 5 * math.pi / 20 <= coord.theta <= 7 * math.pi / 20:
            result += "18"
            hit = True
        elif 31 * math.pi / 20 <= coord.theta <= 33 * math.pi / 20:
            result += "17"
            hit = True
        elif 23 * math.pi / 20 <= coord.theta <= 25 * math.pi / 20:
            result += "16"
            hit = True
        elif 35 * math.pi / 20 <= coord.theta <= 37 * math.pi / 20:
            result += "15"
            hit = True

        if radius >= coord.radius >= radius - 8 and hit:
            result += " 2"
        elif 107 >= coord.radius >= 107 - 8 and hit:
            result += " 3"
        elif 16 >= coord.radius:
            if coord.radius <= 6.35:
                return "25 2"
            return "25"
    return result


stdevX = 15
stdevY = 15


def shoot(boardState1, boardState2):
    #print(boardState1, boardState2)
    target = findTarget1(boardState1, boardState2)
    targetCoord = targetList[target]
    newX = random.gauss(targetCoord.x, stdevX)
    newY = random.gauss(targetCoord.y, stdevY)
    plt.plot(newX, newY, "rx")
    newCoord = Coord(False, newX, newY)
    # print(newCoord.x, newCoord.y)
    result = calculateShot(newCoord)
    return result
