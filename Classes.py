from hashing import hashFunc
from itertools import permutations
from config import *

# NESSESARY?
class Alphabet:
    alphabetSize = 26
    letters = [chr(ord('a') + i) for i in range(26)]


class WordAI: ### !!! STRING IS STORING WITHOUT \n SYMBOL (use .rstrip()), HASH'S ALSO COUNTING THIS WAY HERE AND IN SORTING !!!
    def __init__(self, string): # Is local copy of type really nessesary?
        self.string = string.rstrip()
        self.dictType = dictAI
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

    def allPossibleWords(self, playBoard):
        emptyData = [[[0, 0] for i in range(playBoard.length)] for j in range(playBoard.height)]
        for i in range(playBoard.height):
            curEmpty = 0
            for j in range(playBoard.length - 1, -1, -1):
                curEmpty += playBoard.board[i][j].isEmpty
                emptyData[i][j][0] = curEmpty
        for i in range(playBoard.length):
            curEmpty = 0
            for j in range(playBoard.height - 1, -1, -1):
                curEmpty += playBoard.board[j][i].isEmpty
                emptyData[j][i][1] = curEmpty
        ### Horizontal
        wordsAndCoordsH = set()
        wordsOnlyH = set()
        for i in range(playBoard.height):
            for j in range(playBoard.length - 1, -1, -1):
                maxLetters = min(len(self.string), emptyData[i][j][0]) # Hand size irl ()
                print(maxLetters)
                for curLen in range(1, maxLetters + 1):
                    currentEmptiness = 0
                    temp = 0
                    stakedLetters = []
                    prevData = []
                    for k in range(j - 1, -1, -1):
                        if playBoard.board[i][k].isEmpty:
                            break
                        else:
                            prevData.insert(0, playBoard.board[i][k].letter)
                    for k in range(len(prevData)):
                        stakedLetters.append((k, prevData[k]))
                    while currentEmptiness != maxLetters:
                        if playBoard.board[i][j + temp].isEmpty:
                            currentEmptiness += 1
                        else:
                            stakedLetters.append((temp + len(prevData), playBoard.board[i][j + temp].letter))
                        temp += 1
                    for k in range(j + temp, playBoard.length):
                        if playBoard.board[i][k].isEmpty:
                            break
                        else:
                            stakedLetters.append((temp + k + len(prevData), playBoard.board[i][k].letter))

                    subWordsData = set()
                    for psiWord in permutations(self.string, curLen):
                        curString = ""
                        psiWord = list(psiWord)
                        for inserts in range(len(stakedLetters)):
                            psiWord.insert(stakedLetters[inserts][0], stakedLetters[inserts][1])
                        for letter in psiWord:
                            curString += letter
                        curWord = WordAI(curString)  # Here in the arguments was self.datatype, I deleted it, because I moved all dictTypes to config
                        if curWord.isWord():
                            subWordsData.add(curWord.string)  # STRING JUST TO TEST
                    for elem in subWordsData:
                        wordsAndCoordsH.add((elem, (i, j)))
                        wordsOnlyH.add(elem)
        print('H')
        print(wordsOnlyH)

        ### Vertical (comments like previous)
        wordsAndCoordsV = set()
        wordsOnlyV = set()
        for j in range(playBoard.length):
            for i in range(playBoard.height - 1, -1, -1):
                maxLetters = min(len(self.string), emptyData[i][j][1]) # Hand size irl ()
                for curLen in range(1, maxLetters + 1):
                    currentEmptiness = 0
                    temp = 0
                    stakedLetters = []
                    prevData = []
                    for k in range(i - 1, -1, -1):
                        if playBoard.board[k][j].isEmpty:
                            break
                        else:
                            prevData.insert(0, playBoard.board[k][j].letter)
                    for k in range(len(prevData)):
                        stakedLetters.append((k, prevData[k]))
                    while currentEmptiness != maxLetters:
                        if playBoard.board[i + temp][j].isEmpty:
                            currentEmptiness += 1
                        else:
                            stakedLetters.append((temp + len(prevData), playBoard.board[i + temp][j].letter))
                        temp += 1
                    for k in range(i + temp, playBoard.height):
                        if playBoard.board[i][k].isEmpty:
                            break
                        else:
                            stakedLetters.append((temp + k + len(prevData), playBoard.board[k][j].letter))

                    subWordsData = set()
                    for psiWord in permutations(self.string, curLen):
                        curString = ""
                        psiWord = list(psiWord)
                        for inserts in range(len(stakedLetters)):
                            psiWord.insert(stakedLetters[inserts][0], stakedLetters[inserts][1])
                        for letter in psiWord:
                            curString += letter
                        curWord = WordAI(curString)
                        if curWord.isWord():
                            subWordsData.add(curWord.string)
                    for elem in subWordsData:
                        wordsAndCoordsV.add((elem, (i, j)))
                        wordsOnlyV.add(elem)
        print('V')
        print(wordsOnlyV)

class Cell:
    def __init__(self, row, col, letter='-'):
        self.row = row
        self.col = col
        self.letter = letter
        if letter == '-':
            self.isEmpty = True
        else:
            self.isEmpty = False

    def setLetter(self, letter):
        self.letter = letter
        self.isEmpty = False

    def generateWord(self, board, orientation): # Returns a word, that contains this cell
        if orientation == "Horizontal":             # Orientation is a string ("Horizontal" or "Vertical")
            leftCol = self.col
            while leftCol >= 0 and board.board[self.row][leftCol] != '-':
                leftCol -= 1
            leftCol += 1
            rightCol = self.col
            while rightCol < board.length and board.board[self.row][rightCol] != '-':
                rightCol += 1
            cells = []
            for column in range(leftCol, rightCol):
                cells.append(board.board[self.row][column])
        else:
            bottomRow = self.row
            while bottomRow >= 0 and board.board[bottomRow][self.col] != '-':
                bottomRow -= 1
            bottomRow += 1
            topRow = self.row
            while topRow < board.height and board.board[topRow][self.col] != '-':
                topRow += 1
            cells = []
            for row in range(bottomRow, topRow):
                cells.append(board.board[row][self.col])
        return WordOnBoard(cells)

    def neighborsNum(self, board):
        boardCopy = [[] for row in range(board.height + 2)]
        for row in range(board.height + 2):
            for col in range(board.length + 2):
                if row == 0 or row == board.height + 1 or col == 0 or col == board.height + 1:
                    boardCopy[row].append(0)
                else:
                    if board.board[row-1][col-1].letter == '-':
                        boardCopy[row].append(0)
                    else:
                        boardCopy[row].append(1)

        answer = boardCopy[self.row][self.col + 1] + boardCopy[self.row + 1][self.col]
        answer += boardCopy[self.row + 1][self.col + 2] + boardCopy[self.row + 2][self.col + 1]
        return answer


class WordOnBoard:
    def __init__(self, cells):  # Cells is a list of Cell objects
        string = ""
        for el in cells:
            string += el.letter
        self.string = string.rstrip()
        self.dictType = dictPlayer    # Will we need this Class for AI words, if yes, it is necessary to change the type
        self.hash = hashFunc(self.string)
        self.cells = cells
        self.Tests = False           # !!!! IF YOU NEED TO TEST SET THIS FIELD AS TRUE !!!!!!!!

    def isValidWord(self, board):
        if self.isWord():
            if self.isConnected():
                if (self.isLinked(board) or self.Tests):
                    if self.areFormedWordsValid(board):
                        firstCell = self.cells[0]
                        lastCell = self.cells[len(self.string) - 1]
                        if self.getOrientation() == "Vertical":  # Word is vertical
                            if firstCell.row - 1 >= 0:
                                if board.board[firstCell.row - 1][firstCell.col].letter != '-':
                                    return False
                            if lastCell.row + 1 < board.height:
                                if board.board[lastCell.row + 1][lastCell.col].letter != '-':
                                    return False
                        else:  # Word is horizontal
                            if firstCell.col - 1 >= 0:
                                if board.board[firstCell.row][firstCell.col - 1].letter != '-':
                                    return False
                            if lastCell.row + 1 < board.length:
                                if board.board[lastCell.row][lastCell.col + 1].letter != '-':
                                    return False
                        return True
                    print("Mistake! Your word: '", self.string, "'. All new formed words should be valid", sep="")
                    return False
                print("Mistake! Your word: '", self.string, "' should be linked with previous words", sep="")
                return False
            print("Mistake! Your word: '", self.string, "' is not connected", sep="")
            return False
        print("Mistake! Your word: '", self.string, "' is not in the dictionary", sep="")
        return False
    
    def isWord(self): # Checks whether the word is in dictionary
        return self.hash in hashesPlayer[self.dictType].keys() and self.string in hashesPlayer[self.dictType][self.hash]
    
    def isLinked(self, board):  # Checks whether there are neighbors from old Cells
        firstCell = self.cells[0]
        lastCell = self.cells[len(self.string) - 1]
        if firstCell.neighborsNum(board) > 1 or lastCell.neighborsNum(board) > 1:
            return True
        for i in range(1, len(self.string) - 1):
            if self.cells[i].neighborsNum(board) > 2:
                return True
        return False
        
    def isConnected(self):  # Checks whether cells is a solid strip of letters
        if len(self.string) > 1:
            firstCell = self.cells[0]
            secondCell = self.cells[1]
            rowDif = firstCell.row - secondCell.row
            colDif = firstCell.col - secondCell.col
            if abs(rowDif) + abs(colDif) > 1:
                return False
            for i in range(1, len(self.cells) - 1):
                currentCell = self.cells[i]
                nextCell = self.cells[i + 1]
                if currentCell.row - nextCell.row != rowDif or currentCell.col - nextCell.col != colDif:
                    return False
        return True

    def areFormedWordsValid(self, board):  # Checks whether all new formed words are valid
        if self.getOrientation() == "Horizontal":
            for cell in self.cells:
                if not cell.generatedWord(board, "Vertical").isWord():
                    return False
            return self.cells[0].generateWord(board, "Horizontal").isWord()
        else:
            for cell in self.cells:
                if not cell.generatedWord(board, "Horizontal").isWord():
                    return False
            return self.cells[0].generateWord(board, "Vertical").isWord()

    def addLetter(self, cell):
        self.string += cell.letter
        self.hash = hashFunc(self.string)
        self.cells.append(cell)
        if not self.isConnected():  # Should I throw an Exception here?
            print("Mistake! You can't add the letter '", cell.letter, "', a word should be connected", sep="")
            self.string = self.string[: -1]
            self.hash = hashFunc(self.string)
            self.cells.pop()

    def getOrientation(self):
        firstCell = self.cells[0]
        lastCell = self.cells[len(self.string) - 1]
        rowDif = firstCell.row - lastCell.row
        colDif = firstCell.col - lastCell.col
        if rowDif == 0:
            return "Horizontal"
        else:
            return "Vertical"

    def getScore(self, board):
        score = 0
        wordMultiplier = 1
        for cell in self.cells:
            lettterMultiplier = 1
            if board.bonuses[cell.row][cell.col] == "3W":
                wordMultiplier *= 3
                board.bonuses[cell.row][cell.col] = "00"
            elif board.bonuses[cell.row][cell.col] == "2W":
                wordMultiplier *= 2
                board.bonuses[cell.row][cell.col] = "00"
            elif board.bonuses[cell.row][cell.col] == "3L":
                lettterMultiplier = 3
                board.bonuses[cell.row][cell.col] = "00"
            elif board.bonuses[cell.row][cell.col] == "2L":
                lettterMultiplier = 2
                board.bonuses[cell.row][cell.col] = "00"
                score += lettterMultiplier * scores[cell.letter]
        score *= wordMultiplier
        return score

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
        else: # Should I throw an Exception here?
            print("Mistake! It is impossible to take the letter '", letter, "'", sep="")
            pass

    def randomLetter(self):
        from random import randint
        letterNum = randint(0, self.lettersNum - 1)
        counter = 0
        for el in self.bag:
            if counter <= letterNum:
                prevLetter = el
                counter += self.bag[el]
            else:
                break
        self.removeLetter(prevLetter)
        return prevLetter

class Board:
    def __init__(self, boardLength, boardHeight):
        self.board = [[] for x in range(boardHeight)]
        self.bonuses = bonuses
        self.length = boardLength
        self.height = boardHeight
        for row in range(boardHeight):
            for col in range(boardLength):
                self.board[row].append(Cell(row, col))

    def addWord(self, word):
        if word.isValidWord(self):
            rowBegin = word.cells[0].row
            rowEnd = word.cells[len(word.cells) - 1].row
            colBegin = word.cells[0].col
            colEnd = word.cells[len(word.cells) - 1].col
            if rowBegin == rowEnd:  # "Horizontal orientation"
                counter = 0
                for letter in word.string:
                    self.board[rowBegin][colBegin + counter].setLetter(letter)
                    counter += 1

            elif colBegin == colEnd:  # Vertical orientation
                counter = 0
                for letter in word.string:
                    self.board[rowBegin + counter][colBegin].setLetter(letter)
                    counter += 1
        else:  # Should i throw an exception here?
            print("Mistake! Word '", word.string, "' is Invalid", sep="")
            pass

    def printBoard(self):
        for row in range(self.height):
            for col in range(self.length):
                print(self.board[row][col].letter, end=" ")
            print()


def WordOnBoardConstructor(word, rowBegin, colBegin, orientation):  #Word is a string, rowBegin and colBegin are numbers, orientation is a char ('h' or 'v')
    wordCells = []
    if orientation == 'h':
        rowEnd = rowBegin
        colEnd = colBegin + len(word) - 1
        for i in range(colBegin, colEnd + 1):
            currentLetter = word[i-colBegin]
            wordCells.append(Cell(rowBegin, i))
            wordCells[i-colBegin].setLetter(currentLetter)

    elif orientation == 'v':
        colEnd = colBegin
        rowEnd = rowBegin + len(word) - 1
        for i in range(rowBegin, rowEnd + 1):
            currentLetter = word[i-rowBegin]
            wordCells.append(Cell(i, colBegin))
            wordCells[i-rowBegin].setLetter(currentLetter)

    word = WordOnBoard(wordCells)
    return word


myBoard = Board(15, 15)
word = WordOnBoardConstructor("nose", 6, 6, 'v')
myBoard.addWord(word)
myBoard.printBoard()