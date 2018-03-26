from hashing import *
from Classes import *

def setBonuses():
    bonuses = {}
    for x in range(0, 15):
        for y in range(0, 15):
            point = Coordinate(x, y)
            bonuses[point] = "00"

    for x in range(0, 15, 7):  ### Setting triple word score cells
        for y in range(0, 15, 7):
            bonuses[Coordinate(x, y)] = "3W"

    for x in range(1, 15, 4):   ### Setting triple letter score cells
        for y in range(1, 15, 4):
            bonuses[Coordinate(x, y)] = "3L"

    bonuses[Coordinate(7, 7)] = "2W"  ### Setting double word score cells
    for x in range(1, 5):
        bonuses[Coordinate(x, x)] = "2W"
        bonuses[Coordinate(x, 14 - x)] = "2W"
        bonuses[Coordinate(14 - x, x)] = "2W"
        bonuses[Coordinate(14 - x, 14 - x)] = "2W"

    doubleLetters = {(0, 3), (2, 6), (3, 7), (6, 6), (7, 3), (6, 2), (3, 0)}   ### Setting double letter score cells
    for cell in doubleLetters:
        x = cell[0]
        y = cell[1]
        bonuses[Coordinate(x, y)] = "2L"
        bonuses[Coordinate(x, 14 - y)] = "2L"
        bonuses[Coordinate(14 - x, y)] = "2L"
        bonuses[Coordinate(14 - x, 14 - y)] = "2L"
    return bonuses

typeData = ["Basic", "Big", "Large", "Medium", "Small"]
forbidden = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ",", ".", "/", "-", "&", "'"]
###
hashesAI = dict()
for typeAI in typeData:
    hashesAI[typeAI] = hashTabling(typeAI)
#print(hashesAI) Working though

bonuses = setBonuses()
scores = {' ': 0, 'a': 1, 'b': 2, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2,
              'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1,
              'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4,
              'x': 8, 'y': 4, 'z': 10}


