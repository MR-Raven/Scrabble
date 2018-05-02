from hashing import hashFunc
from itertools import permutations
from config import *

class WordAI:  ### !!! STRING IS STORING WITHOUT \n SYMBOL (use .rstrip()), HASH'S ALSO COUNTING THIS WAY HERE AND IN SORTING !!!
    def __init__(self, string):  # Is local copy of type really nessesary?
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
                curWord = WordAI(curString, self.dictType)
                if curWord.isWord():
                    subWordsData.add(curWord.string)  # STRING JUST TO TEST
        return subWordsData

    def isLinked(self, board, cellsData):  # Checks whether there are neighbors from old Cells
        for i in range(0, len(self.string)):
            if cellsData[i].neighborsNum(board) > 0:
                return True
        return False

    def allPossibleWords(self, playBoard):
        emptyData = playBoard.boardEmptiness()
        ### Horizontal
        wordsAndCoordsH = set()
        for i in range(playBoard.height):
            for j in range(playBoard.length - 1, -1, -1):
                maxLetters = min(len(self.string), emptyData[i][j][0])  # Hand size irl ()
                for curLen in range(1, maxLetters + 1):
                    ### Stable letters companation
                    currentEmptiness = 0
                    temp = 0
                    stakedLetters = []
                    prevData = []
                    for k in range(j - 1, -1, -1):
                        if playBoard.board[i][k].isEmpty():
                            break
                        else:
                            prevData.insert(0, playBoard.board[i][k].letter)
                    for k in range(len(prevData)):
                        stakedLetters.append((k, prevData[k]))
                    while currentEmptiness != maxLetters:
                        if playBoard.board[i][j + temp].isEmpty():
                            currentEmptiness += 1
                        else:
                            stakedLetters.append((temp + len(prevData), playBoard.board[i][j + temp].letter))
                        temp += 1
                    postDataSize = 0
                    for k in range(j + temp, playBoard.length):
                        if playBoard.board[i][k].isEmpty():
                            break
                        else:
                            stakedLetters.append((temp + k + len(prevData), playBoard.board[i][k].letter))
                            postDataSize += 1
                    ### Subwords search
                    subWordsData = set()
                    for psiWord in permutations(self.string, curLen):
                        curString = ""
                        psiWord = list(psiWord)
                        for inserts in range(len(stakedLetters)):
                            psiWord.insert(stakedLetters[inserts][0], stakedLetters[inserts][1])
                        for letter in psiWord:
                            curString += letter
                        curWord = WordAI(curString)  # Here in the arguments was self.datatype, I deleted it, because I moved all dictTypes to config
                        cellData = []
                        for curPos in range(len(curWord.string)):
                            cellData.append(Cell(i, curPos + j, curWord.string[curPos]))
                        ### New words formation check
                        newWordsFlag = True
                        for curLetter in range(j - len(prevData), j + len(curWord.string) - len(prevData)):
                            newFormedWord = curWord.string[curLetter - j + len(prevData)]
                            xMin = i - 1
                            while xMin >= 0 and not playBoard.board[xMin][curLetter].isEmpty():
                                newFormedWord = playBoard.board[xMin][curLetter].letter + newFormedWord
                                xMin -= 1
                            xMax = i + 1
                            while xMax < playBoard.height and not playBoard.board[xMax][curLetter].isEmpty():
                                newFormedWord += playBoard.board[xMax][curLetter].letter
                                xMax += 1
                            if not WordAI(newFormedWord).isWord() and len(newFormedWord) >= 2:
                                newWordsFlag = False
                        if curWord.isWord() and curWord.isLinked(playBoard, cellData) and newWordsFlag:
                            subWordsData.add(curWord.string)  # STRING JUST TO TEST
                        if not curWord.isLinked(playBoard, cellData):
                            break
                    for elem in subWordsData:
                        wordsAndCoordsH.add((elem, (i, j - len(prevData) + postDataSize)))
        print('H')
        print(wordsAndCoordsH)

        ### Vertical (comments like previous)
        wordsAndCoordsV = set()
        for j in range(playBoard.length):
            for i in range(playBoard.height - 1, -1, -1):
                maxLetters = min(len(self.string), emptyData[i][j][1])  # Hand size irl ()
                for curLen in range(2, maxLetters + 1):
                    ### Stable letters companation
                    currentEmptiness = 0
                    temp = 0
                    stakedLetters = []
                    prevData = []
                    if i == 5 and j == 5 and maxLetters == 3:
                        print()

                    for k in range(i - 1, -1, -1):
                        if playBoard.board[k][j].isEmpty():
                            break
                        else:
                            prevData.insert(0, playBoard.board[k][j].letter)
                    for k in range(len(prevData)):
                        stakedLetters.append((k, prevData[k]))
                    while currentEmptiness != maxLetters:
                        if playBoard.board[i + temp][j].isEmpty():
                            currentEmptiness += 1
                        else:
                            stakedLetters.append((temp + len(prevData), playBoard.board[i + temp][j].letter))
                        temp += 1
                    postDataSize = 0
                    for k in range(i + temp, playBoard.height):
                        if playBoard.board[k][j].isEmpty():
                            break
                        else:
                            stakedLetters.append((temp + k + len(prevData), playBoard.board[k][j].letter))
                            postDataSize += 1
                    ### Subwords search
                    subWordsData = set()
                    for psiWord in permutations(self.string, curLen):
                        curString = ""
                        psiWord = list(psiWord)
                        for inserts in range(len(stakedLetters)):
                            psiWord.insert(stakedLetters[inserts][0], stakedLetters[inserts][1])
                        for letter in psiWord:
                            curString += letter
                        curWord = WordAI(curString)
                        ### Cells and valid linking
                        cellData = []
                        for curPos in range(len(curWord.string)):
                            cellData.append(Cell(i + curPos, j, curWord.string[curPos]))
                        ### New words formation check
                        newWordsFlag = True
                        for curLetter in range(i - len(prevData), i + len(curWord.string) - len(prevData)):
                            newFormedWord = curWord.string[curLetter - i + len(prevData)]
                            xMin = j - 1
                            while xMin >= 0 and not playBoard.board[curLetter][xMin].isEmpty():
                                newFormedWord = playBoard.board[curLetter][xMin].letter + newFormedWord
                                xMin -= 1
                            xMax = j + 1
                            while xMax < playBoard.length and not playBoard.board[curLetter][xMax].isEmpty():
                                newFormedWord += playBoard.board[curLetter][xMax].letter
                                xMax += 1
                            if not WordAI(newFormedWord).isWord() and len(newFormedWord) >= 2:
                                newWordsFlag = False
                        if curWord.isWord() and curWord.isLinked(playBoard, cellData) and newWordsFlag:
                            subWordsData.add(curWord.string)
                        if not curWord.isLinked(playBoard, cellData):
                            break
                    for elem in subWordsData:
                        wordsAndCoordsV.add((elem, (i - len(prevData) + postDataSize, j)))
        print('V')
        print(wordsAndCoordsV)


class Cell:
    def __init__(self, row, col, letter='-'):
        self.row = row
        self.col = col
        self.letter = letter
        self.isNew = True

    def generateWord(self, board, orientation):  # Returns a word, that contains this cell, it may be just one cell
        if orientation == "Horizontal":  # Orientation is a string ("Horizontal" or "Vertical")
            leftCol = self.col
            while leftCol >= 0 and not board.board[self.row][leftCol].isEmpty():
                leftCol -= 1
            leftCol += 1
            rightCol = self.col
            while rightCol < board.length and not board.board[self.row][rightCol].isEmpty():
                rightCol += 1
            cells = []
            for column in range(leftCol, rightCol + 1):
                cells.append(board.board[self.row][column])
        else:
            bottomRow = self.row
            while bottomRow >= 0 and not board.board[bottomRow][self.col].isEmpty():
                bottomRow -= 1
            bottomRow += 1
            topRow = self.row
            while topRow < board.height and not board.board[topRow][self.col].isEmpty():
                topRow += 1
            cells = []
            for row in range(bottomRow, topRow + 1):
                cells.append(board.board[row][self.col])
        return WordOnBoard(cells)

    def isEmpty(self):
        return self.letter == '-'

    def neighborsNum(self, board):   # It is better to optimize it
        boardCopy = [[] for row in range(board.height + 2)]
        for row in range(board.height + 2):
            for col in range(board.length + 2):
                if row == 0 or row == board.height + 1 or col == 0 or col == board.height + 1:
                    boardCopy[row].append(0)
                else:
                    if board.board[row - 1][col - 1].isEmpty():
                        boardCopy[row].append(0)
                    else:
                        boardCopy[row].append(1)

        answer = boardCopy[self.row][self.col + 1] + boardCopy[self.row + 1][self.col]
        answer += boardCopy[self.row + 1][self.col + 2] + boardCopy[self.row + 2][self.col + 1]
        return answer


class WordOnBoard:
    def __init__(self, cells=None):  # Cells is a list of Cell objects
        if cells == None:
            self.cells = []
        else:
            self.cells = cells
        string = ""
        for el in self.cells:
            if not el.isEmpty():
                string += el.letter
        self.string = string.rstrip()
        self.dictType = dictPlayer  # Will we need this Class for AI words, if yes, it is necessary to change the type
        self.hash = hashFunc(self.string)

    def isValidWord(self, board, turn):
        if self.isWord():
            if self.isConnected():
                if self.isLinked(board) or self.firstTurnCheck(board, turn) or isTested:
                    if self.areFormedWordsValid(board):
                        firstCell = self.cells[0]
                        lastCell = self.cells[len(self.string) - 1]
                        if self.getOrientation() == "Vertical":  # Word is vertical
                            if firstCell.row - 1 >= 0:
                                if not board.board[firstCell.row - 1][firstCell.col].isEmpty():
                                    print("Mistake! On the top of your word there shouldn't be other letters")
                                    return False
                            if lastCell.row + 1 < board.height:
                                if not board.board[lastCell.row + 1][lastCell.col].isEmpty():
                                    print("Mistake! On the bottom of your word there shouldn't be other letters")
                                    return False
                        else:  # Word is horizontal
                            if firstCell.col - 1 >= 0:
                                if not board.board[firstCell.row][firstCell.col - 1].isEmpty():
                                    print("Mistake! On the left of your word there shouldn't be other letters")
                                    return False
                            if lastCell.col + 1 < board.length:
                                if not board.board[lastCell.row][lastCell.col + 1].isEmpty():
                                    print("Mistake! On the right of your word there shouldn't be other letters")
                                    return False
                        for cell in self.cells:  # Checking that the word has at least one new letter
                            if cell.isNew:
                                return True
                        print("Mistake! Your word: '", self.string, "' should have at least one new letter!", sep="")
                        return False
                    print("Mistake! Your word: '", self.string, "'. All new formed words should be valid", sep="")
                    return False
                if turn.isFirstTurn:
                    print("Mistake! You word: '", self.string, "' should have a letter on the center square!", sep="")
                else:
                    print("Mistake! Your word: '", self.string, "' should be linked with previous words", sep="")
                return False
            print("Mistake! Your word: '", self.string, "' is not connected", sep="")
            return False
        print("Mistake! Your word: '", self.string, "' is not in the dictionary", sep="")
        return False

    def isWord(self):  # Checks whether the word is in the dictionary
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
                if not cell.generateWord(board, "Vertical").isWord() and len(
                        cell.generateWord(board, "Vertical").string) > 1:
                    return False
            return self.isWord()     # In fact there is no need to check it
        else:
            for cell in self.cells:
                if not cell.generateWord(board, "Horizontal").isWord() and len(
                        cell.generateWord(board, "Horizontal").string) > 1:
                    return False
            return self.isWord()   # In fact there is no need to check it

    def firstTurnCheck(self, board, turn):
        if turn.isFirstTurn == True:
            for cell in self.cells:
                if cell.row == 7 and cell.col == 7:
                    return True
        return False

    def addLetter(self, cell, board):  # It is necessary to update rack here
        if self.isConnected():
            self.string += cell.letter
            self.hash = hashFunc(self.string)
            self.cells.append(cell)
            board.addCell(cell)
        else:  # Should I throw an Exception here? Surely you should
            print("Mistake! You can't add the letter '", cell.letter, "', a word should be connected", sep="")

    def deleteLastLetter(self, board):  # It is necessary to update rack here
        if len(self.string) > 0:
            board.deleteCell(self.cells[-1])
            self.string = self.string[:-1]
            self.hash = hashFunc(self.string)
            self.cells.pop()
        else:
            print("Mistake! The word is empty, you can't delete any letter!")

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
        if self.isWord():  # In fact it is enough to check that len(self.string) > 1
            wordMultiplier = 1
            for cell in self.cells:
                lettterMultiplier = 1
                if board.bonuses[cell.row][cell.col] == "3W":
                    wordMultiplier *= 3
                elif board.bonuses[cell.row][cell.col] == "2W":
                    wordMultiplier *= 2
                elif board.bonuses[cell.row][cell.col] == "3L":
                    lettterMultiplier = 3
                elif board.bonuses[cell.row][cell.col] == "2L":
                    lettterMultiplier = 2
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
        else:  # Should I throw an Exception here?
            print("Mistake! It is impossible to take the letter '", letter, "'", sep="")

    def getRandomLetter(self):
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

    def addWord(self, word, score, rack, turn): # word is a WordOnBoard object, score is a Score object, rack is a Rack object
        if word.isValidWord(self, turn):
            score.updateScore(self, word, rack, turn)
            self.updateBoard(word)
            rack.drawNewTiles(self, turn)
            turn.finishTurn()
        else:
            while len(word.string) > 0:
                word.deleteLastLetter(self)

    def updateBoard(self, newWord):
        for cell in newWord.cells:         # Update bonuses
            self.bonuses[cell.row][cell.col] = "00"

        for cell in newWord.cells:
            self.board[cell.row][cell.col].isNew = False

    def addCell(self, cell):
        if self.board[cell.row][cell.col].isEmpty() or self.board[cell.row][cell.col].letter == cell.letter:
            self.board[cell.row][cell.col].letter = cell.letter
        else:
            print("Mistake! This cell is not empty!")

    def deleteCell(self, cell):
        if self.board[cell.row][cell.col].isNew:
            self.board[cell.row][cell.col].letter = '-'
        else:
            print("Mistake! This cell wasn't added during this turn, you can't delete it")

    def printBoard(self):
        for row in range(self.height):
            for col in range(self.length):
                print(self.board[row][col].letter, end=" ")
            print()
        print()

    def boardEmptiness(self):
        emptyData = [[[0, 0] for i in range(self.length)] for j in range(self.height)]
        for i in range(self.height):
            curEmpty = 0
            for j in range(self.length - 1, -1, -1):
                curEmpty += self.board[i][j].isEmpty()
                emptyData[i][j][0] = curEmpty
        for i in range(self.length):
            curEmpty = 0
            for j in range(self.height - 1, -1, -1):
                curEmpty += self.board[j][i].isEmpty()
                emptyData[j][i][1] = curEmpty
        return emptyData


class Scoring:
    def __init__(self):
        self.scoreAI = 0
        self.scorePlayer = 0

    def updateScore(self, board, newWord, rack, turn):  # board is a Board object, newword is WordOnBoard object, rack is an object of the class Rack
        if turn.priority == "AI":
            if newWord.getOrientation() == "Horizontal":
                for cell in newWord.cells:
                    if board.board[cell.row][cell.col].isNew:
                        currentWord = cell.generateWord(board, "Vertical")
                        self.scoreAI += currentWord.getScore(board)
            else:
                for cell in newWord.cells:
                    if board.board[cell.row][cell.col].isNew:
                        currentWord = cell.generateWord(board, "Horizontal")
                        self.scoreAI += currentWord.getScore(board)
            self.scoreAI += newWord.getScore(board)
            if len(rack.rackAI) == 0:  # Bingo bonus
                self.scoreAI += 50

        elif turn.priority == "Player":
            if newWord.getOrientation() == "Horizontal":
                for cell in newWord.cells:
                    if board.board[cell.row][cell.col].isNew:
                        currentWord = cell.generateWord(board, "Vertical")
                        self.scorePlayer += currentWord.getScore(board)
            else:
                for cell in newWord.cells:
                    if board.board[cell.row][cell.col].isNew:
                        currentWord = cell.generateWord(board, "Horizontal")
                        self.scorePlayer += currentWord.getScore(board)
            self.scorePlayer += newWord.getScore(board)
            if len(rack.rackPlayer) == 0:  # Bingo bonus
                self.scorePlayer += 50
        else:
            print("Mistake! There is no such name '", turn.priority, "' for priority parameter", sep="")

    def gameEndRecalculation(self, rack):  # rack is a Rack object
        for letter in rack.rackAI:
            self.scoreAI -= scores[letter]
        for letter in rack.rackPlayer:
            self.scorePlayer -= scores[letter]
        if len(myRack.rackAI) == 0:
            for letter in rack.rackPlayer:
                self.scoreAI += scores[letter]
        elif len(myRack.rackPlayer) == 0:
            for letter in rack.rackAI:
                self.scorePlayer += scores[letter]

    def getWinner(self):
        playerScoreCopy = self.scorePlayer
        aiScoreCopy = self.scoreAI
        self.gameEndRecalculation()
        if self.scorePlayer > self.scoreAI:
            return "Player"
        elif self.scoreAI > self.scorePlayer:
            return "AI"
        else:
            if playerScoreCopy < aiScoreCopy:
                return "AI"
            elif aiScoreCopy < playerScoreCopy:
                return "Player"
            return "Draw"

class Rack:
    def __init__(self, bag):  # bag is a Bag object
        self.rackPlayer = []
        self.rackAI = []
        for i in range(7):
            self.addLetter(bag.getRandomLetter(), "AI")
            self.addLetter(bag.getRandomLetter(), "Player")

    def removeLetter(self, letter, priority):  # priority is a string ("Player" or "AI")
        if priority == "Player":
            if letter in self.rackPlayer:
                for i in range(len(self.rackPlayer)):
                    if self.rackPlayer[i] == letter:
                        del self.rackPlayer[i]
                        break
            else:
                print("Mistake! There is no letter '", letter, "' in player's rack", sep="")
        elif priority == "AI":
            if letter in self.rackAI:
                for i in range(len(self.rackAI)):
                    if self.rackAI[i] == letter:
                        del self.rackAI[i]
                        break
            else:
                print("Mistake! There is no letter '", letter, "' in AI's rack", sep="")
        else:
            print("Mistake! There is no such name '", priority, "' for priority parameter", sep="")

    def addLetter(self, letter, priority):  # Maybe it is better to sort self.letters
        if priority == "Player":
            if len(self.rackPlayer) < 7:
                self.rackPlayer.append(letter)
            else:
                print("Mistake! It's impossible to add a letter '", letter, "' to player's rack, because it's already full")
        elif priority == "AI":
            if len(self.rackAI) < 7:
                self.rackAI.append(letter)
            else:
                print("Mistake! It's impossible to add a letter '", letter, "' to AI's rack, because it's already full")

    def drawNewTiles(self, bag, turn):  # bag is a Bag object, score is a Scoring object
        if turn.priority == "Player":
            while len(self.rackPlayer) < 7 and len(bag.bag) > 0:
                self.rackPlayer.append(bag.getRandomLetter())
        elif turn.priority == "AI":
            while len(self.rackAI) < 7 and len(bag.bag) > 0:
                self.rackAI.append(bag.getRandomLetter())
        else:
            print("Mistake! There is no such name '", turn.priority, "' for priority parameter", sep="")

class Turn:
    def __init__(self):
        self.priority = self.turnPriority()
        self.isFirstTurn = True;

    def finishTurn(self):
        if self.isFirstTurn:
            self.isFirstTurn = False
        if self.priority == "AI":
            self.priority = "Player"
            # if self.isGameFinished():
        elif self.priority == "Player":
            self.priority = "AI"
            # if self.isGameFinished():
        else:
            print("Mistake! There is no such name '", self.priority, "' for priority parameter", sep="")

    def turnPriority(self):
        from random import randint
        x = randint(0, 1)
        if x == 0:
            return "Player"
        else:
            return "AI"

    def isGameFinished(self, rack, bag):  # Afterwards add an option to check whether any words can be made
        if bag.lettersNum == 0 and (len(rack.rackPlayer) == 0 or len(rack.rackAI) == 0):
            return True
        return False


def WordOnBoardConstructor(word, rowBegin, colBegin, orientation):  # Word is a string, rowBegin and colBegin are numbers, orientation is a char ('h' or 'v')
    wordNew = WordOnBoard()
    global myBoard, myScore, myRack, myBag
    if orientation == 'h':
        rowEnd = rowBegin
        colEnd = colBegin + len(word) - 1
        for i in range(colBegin, colEnd + 1):
            currentLetter = word[i - colBegin]
            wordNew.addLetter(Cell(rowBegin, i, currentLetter), myBoard)

    elif orientation == 'v':
        colEnd = colBegin
        rowEnd = rowBegin + len(word) - 1
        for i in range(rowBegin, rowEnd + 1):
            currentLetter = word[i - rowBegin]
            wordNew.addLetter(Cell(i, colBegin, currentLetter), myBoard)
    myBoard.addWord(wordNew, myScore, myRack, myTurn)


def printStatus():
    global myBoard, myScore, myRack, myBag
    print("PLAYER:")
    print("Score:", myScore.scorePlayer)
    print("Rack:", myRack.rackPlayer)
    print()
    print("AI:")
    print("Score:", myScore.scoreAI)
    print("Rack:", myRack.rackAI)
    print("")
    print("Board:")
    myBoard.printBoard()
    print()
    print("Bag:")
    print(myBag.bag)
    print()
    print()
    print()




myBoard = Board(15, 15)
myScore = Scoring()
myBag = Bag()
myRack = Rack(myBag)
myTurn = Turn()

WordOnBoardConstructor("mother", 4, 4, 'h')
WordOnBoardConstructor("meadow", 4, 4, 'v')
WordOnBoardConstructor("racket", 4, 9, 'v')
WordOnBoardConstructor("attack", 9, 8, 'h')

myBoard.printBoard()
slovo = WordAI("topless")
slovo.allPossibleWords(myBoard)
'''
word1 = WordOnBoard()
word1.addLetter(Cell(6, 7, 'p'), myBoard)
word1.addLetter(Cell(7, 7, 'i'), myBoard)
word1.addLetter(Cell(8, 7, 'e'), myBoard)
myBoard.addWord(word1, myScore, myRack, myTurn)
printStatus()
word2 = WordOnBoard()
word2.addLetter(Cell(8, 7, 'e'), myBoard)
word2.addLetter(Cell(8, 8, 'y'), myBoard)
word2.addLetter(Cell(8, 9, 'e'), myBoard)
myBoard.addWord(word2, myScore, myRack, myTurn)
printStatus()
word3 = WordOnBoard()
word3.addLetter(Cell(0, 0, 'h'), myBoard)
word3.addLetter(Cell(1, 0, 'e'), myBoard)
word3.addLetter(Cell(2, 0, 'l'), myBoard)
word3.addLetter(Cell(3, 0, 'l'), myBoard)
word3.addLetter(Cell(4, 0, 'o'), myBoard)
myBoard.addWord(word3, myScore, myRack, myTurn)
printStatus()
word4 = WordOnBoard()
word4.addLetter(Cell(8, 8, 'y'), myBoard)
word4.addLetter(Cell(9, 8, 'e'), myBoard)
word4.addLetter(Cell(10, 8, 's'), myBoard)
myBoard.addWord(word4, myScore, myRack, myTurn)
printStatus()

'''