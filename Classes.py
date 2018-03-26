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
