from hashing import *

def setBonuses():
    bonuses = [[] for n in range(15)]
    for str in range(0, 15):
        for col in range(0, 15):
            bonuses[str].append("00")

    for str in range(0, 15, 7):  ### Setting triple word score cells
        for col in range(0, 15, 7):
            bonuses[str][col] = "3W"

    for str in range(1, 15, 4):   ### Setting triple letter score cells
        for col in range(1, 15, 4):
            bonuses[str][col] = "3L"

    bonuses[7][7] = "2W"  ### Setting double word score cells
    for str in range(1, 5):
        bonuses[str][str] = "2W"
        bonuses[str][14-str] = "2W"
        bonuses[14-str][str] = "2W"
        bonuses[14 - str][14 - str] = "2W"

    doubleLetters = {(0, 3), (2, 6), (3, 7), (6, 6), (7, 3), (6, 2), (3, 0)}   ### Setting double letter score cells
    for cell in doubleLetters:
        str = cell[0]
        col = cell[1]
        bonuses[str][col] = "2L"
        bonuses[str][14 - col] = "2L"
        bonuses[14 - str][col] = "2L"
        bonuses[14 - str][14 - col] = "2L"
    return bonuses



typeData = ["Basic", "Big", "Large", "Medium", "Small"]
forbidden = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ",", ".", "/", "-", "&", "'"]

hashesAI = dict()
for typeAI in typeData:
    hashesAI[typeAI] = hashTabling(typeAI)
bonuses = setBonuses()
scores = {' ': 0, 'a': 1, 'b': 2, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2,
              'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1,
              'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4,
              'x': 8, 'y': 4, 'z': 10}



