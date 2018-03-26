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

for i in range(100):
    slovo = Word("abcdefg", "Big")
    print(slovo.subWords(), i)


class Cell:
    def __init__(self, x, y):
        from config import bonuses
        self.x = x
        self.y = y
        self.letter = '-'
        self.bonus = bonuses[(x, y)]
        self.isEmpty = True

class Bag:
    bag = {' ': 2, 'a': 9, 'b': 2, 'c': 2, 'd': 4, 'e': 12, 'f': 2, 'g': 3,
           'h': 2, 'i': 9, 'j': 1, 'k': 1, 'l': 4, 'm': 2, 'n': 6, 'o': 8,
           'p': 2, 'q': 1, 'r': 6, 's': 4, 't': 6, 'u': 4, 'v': 2, 'w': 2,
           'x': 1, 'y': 2, 'z': 1}

    lettersNum = 100

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
        for x in range(boardHeight):
            for y in range(boardLength):
                self.board[x].append(Cell(x, y))

    def addWord(self, word, xBegin, xEnd, yBegin, yEnd):
        if xBegin == xEnd:
            counter = 0
            for letter in word:
                self.board[xBegin][yBegin + counter].letter = letter
                counter += 1

        elif yBegin == yEnd:
            counter = 0
            for letter in word:
                self.board[xBegin + counter][yBegin].letter = letter
                counter += 1

    def printBoard(self):
        for x in range(self.height):
            for y in range(self.length):
                print(self.board[x][y].letter, end=" ")
            print()



myBoard = Board(10, 10)
myBoard.addWord("hello", 0, 5, 0, 0)
myBoard.addWord("little", 3, 3, 0, 6)
myBoard.printBoard()
