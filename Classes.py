from hashing import hashFunc
from itertools import permutations

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

    def allPermutations(self):
        permutationsData = set()
        for psiWord in permutations(self.string, len(self.string)):
            curString = ""
            for letter in psiWord:
                curString += letter
            curWord = Word(curString, self.dictType)
            if curWord.isWord():
                permutationsData.add(curWord.string) # STRING JUST TO TEST
        return permutationsData

    def subWords(self):
        subWordsData = set()
        for length in range(len(self.string)):
            for psiWord in permutations(self.string, length):
                curString = ""
                for letter in psiWord:
                    curString += letter
                curWord = Word(curString, self.dictType)
                if curWord.isWord():
                    subWordsData.add(curWord.string) # STRING JUST TO TEST
        return subWordsData


class BoardWord:
    def __init__(self, cells, type):
        self.string = ''.join(cells).rstrip()
        self.dictType = type
        self.hash = hashFunc(self.string)
        self.cells = cells

    def isWord(self):
        from config import hashesAI
        return self.hash in hashesAI[self.dictType].keys() and self.string in hashesAI[self.dictType][self.hash]


class Cell:
    def __init__(self, row, col):
        from config import bonuses
        self.row = row
        self.col = col
        self.letter = ''
        self.bonus = bonuses[str][col]
        self.isEmpty = True


class Bag:
    def __init__(self):
        self.bag = {' ': 2, 'a': 9, 'b': 2, 'c': 2, 'd': 4, 'e': 12, 'f': 2, 'g': 3,
           'h': 2, 'i': 9, 'j': 1, 'k': 1, 'l': 4, 'm': 2, 'n': 6, 'o': 8,
           'p': 2, 'q': 1, 'r': 6, 's': 4, 't': 6, 'u': 4, 'v': 2, 'w': 2,
           'x': 1, 'y': 2, 'z': 1}

        self.lettersNum = 100

    def removeLetter(self, letter):
        if self.bag[letter] > 0:
            self.bag[letter] -= 1
            self.lettersNum -= 1
            return True
        else:
            return False


class Board:
    def __init__(self, boardLength, boardHeight):
        self.board = [[] for x in range(boardHeight)]
        self.length = boardLength
        self.height = boardHeight
        for row in range(boardHeight):
            for col in range(boardLength):
                self.board[row].append(Cell(row, col))

    def addWord(self, word):
        if word.isWord():
            rowBegin = word.cells[0].row
            rowEnd = word.cells[len(word.cells) - 1].row
            colBegin = word.cells[0].col
            colEnd = word.cells[len(word.cells) - 1].col
            if rowBegin == rowEnd:  # "Horizontal orientation"
                counter = 0
                for letter in word:
                    self.board[rowBegin][colBegin + counter].letter = letter

            elif colBegin == colEnd:  # Vertical orientation
                counter = 0
                for letter in word:
                    self.board[rowBegin + counter][colBegin].letter = letter

    def printBoard(self):
        for row in range(self.height):
            for col in range(self.length):
                print(self.board[row][col].letter, end=" ")
            print()



myBoard = Board(10, 10)
myBoard.printBoard()
