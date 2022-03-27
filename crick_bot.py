#import crick_game
import math
import random
board_radius = 6.75
test_boardState1 = [3, 3, 3, 3, 3, 3, 2, 15]
test_boardState2 = [2, 2, 3, 3, 3, 3, 2, 15]


# def hit(pos):
#     test_boardState1[pos] += 1
#     return test_boardState1


#def miss():
#    return test_boardState1


# def convertToX(rx, ty):
#     return rx*math.cos(ty)
#
#
# def convertToY(rx, ty):
#     return rx*math.sin(ty)
#
#
# def convertToR(rx, ty):
#     return math.sqrt(math.pow(rx, 2) + math.pow(ty, 2))
#
#
# def convertToTheta(rx, ty):
#     result = math.atan(ty / rx)
#     if result < 0.0:
#         result += 2*math.pi
#     return result
#
#
# class Coord:
#     radius = 0.0
#     theta = 0.0
#     radial = True
#     x = 0.0
#     y = 0.0
#
#     def _init_(self, radial, rx, ty):
#         if (radial):
#             self.radius = rx
#             self.theta = ty
#             self.x = convertToX(rx, ty)
#             self.y = convertToY(rx, ty)
#         else:
#             self.x = rx
#             self.y = ty
#             self.radius = convertToR(rx, ty)
#             self.theta = convertToTheta(rx, ty)


def getValue(target):
    if target == 6:
        return 25
    else:
        return target + 15


def findTarget1(boardState1, boardState2):
    target = 5
    for index in range(len(boardState1)-2, -1, -1):
        if boardState1[index] < 3:
            target = index
            break
    return getValue(target)


def findTarget2(boardState1, boardState2):
    target = 6
    for index in range(len(boardState1) - 1, -1, -1):
        if boardState1[index] < 3:
            target = index
            break
    return getValue(target)

def findTarget3(boardState1, boardState2):
    target = 3
    return target

def easy_calculateShot(target):
    if target <= 20:
        if random.random() <= 0.15:
            return target
        else:
            return 0
    else:
        if random.random() <= 0.05:
            return target
        else:
            return 0

def medium_calculateShot(target):
    if target <= 20:
        if random.random() <= 0.25:
            return target
        else:
            return 0
    else:
        if random.random() <= 0.10:
            return target
        else:
            return 0

def hard_calculateShot(target):
    if target <= 20:
        if random.random() <= 0.99:
            return target
        else:
            return 0
    else:
        if random.random() <= 0.15:
            return target
        else:
            return 0

print(findTarget1(test_boardState1, test_boardState2))

