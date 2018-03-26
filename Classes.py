from hashing import hashFunc
from config import *


# NESSESARY?
class Alphabet:
    alphabetSize = 26
    letters = [chr(ord('a') + i) for i in range(26)]


class Word: ### !!! STRING IS STORING WITHOUT \n SYMBOL (use .rstrip()), HASH'S ALSO COUNTING THIS WAY HERE AND IN SORTING !!!
    def __init__(self, string, type): # Is local copy of type really nessesary?
        self.string = string.rstrip()
        self.dictType = type
        self.hash = hashFunc(self.string)
    def isWord(self):
        return self.hash in hashesAI[self.dictType].keys() and self.string in hashesAI[self.dictType][self.hash]
# Test
slovo = Word("tree", "Big")
print(slovo.hash)


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Cell:
    def __init__(self, coord, letter, bonus):
        self.x = coord.x
        self.y = coord.y
        self.letter = letter
        self.bonus = getBonus(coord)


def setBonuses():
    bonuses = {}
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
        x = cell.first
        y = cell.second
        bonuses[Coordinate(x, y)] = "2L"
        bonuses[Coordinate(x, 14 - y)] = "2L"
        bonuses[Coordinate(14 - x, y)] = "2L"
        bonuses[Coordinate(14 - x, 14 - y)] = "2L"
    return bonuses


def getBonus(coord):
    return setBonuses()[coord]


def getLetterScore(letter):
    scores = {' ': 0, 'A': 1, 'B': 2, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2,
              'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1,
              'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4,
              'X': 8, 'Y': 4, 'Z': 10}
    return scores[letter]
