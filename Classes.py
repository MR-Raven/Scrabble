from hashing import hashFunc


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
        from config import hashesAI
        return self.hash in hashesAI[self.dictType].keys() and self.string in hashesAI[self.dictType][self.hash]
# Test
slovo = Word("tree", "Big")
print(slovo.hash)


class Cell:
    def __init__(self, x, y,  bonus):
        from config import bonuses
        self.x = x
        self.y = y
        self.bonus = bonuses[(x, y)]
        self.isEmpty = True


class Bag:
    bag = {' ': 2, 'a': 9, 'b': 2, 'c': 2, 'd': 4, 'e': 12, 'f': 2, 'g': 3,
           'h': 2, 'i': 9, 'j': 1, 'k': 1, 'l': 4, 'm': 2, 'n': 6, 'o': 8,
           'p': 2, 'q': 1, 'r': 6, 's': 4, 't': 6, 'u': 4, 'v': 2, 'w': 2,
           'x': 1, 'y': 2, 'z': 1}

    def deleteLetter(self, letter):
        if self.bag[letter] > 0:
            self.bag[letter] -= 1
            return 1
        else:
            return 0


class Board:
    def __init__(self, boardLength, boardWidth):
        board = []
        for x in range(0, boardLength):
            for y in range(0, boardWidth):
                board.append(Cell(x, y))