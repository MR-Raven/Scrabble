from Classes import *



class Scoring:
    def __init__(self):
        self.scoreAI = 0
        self.scorePlayer = 0
        self.priority = self.turnPriority()

    def updateScore(self, board, newWord):
        if self.priority == "AI":
            if newWord.getOrientation() == "Horizontal":
                for cell in newWord.cells:
                    currentWord = cell.generateWord(board, "Vertical")
                    self.scoreAI += currentWord.getScore()
            else:
                for cell in newWord.cells:
                    currentWord = cell.generateWord(board, "Horizontal")
                    self.scoreAI += currentWord.getScore()
            self.scoreAI += newWord.getScore()
            self.priority = "Player"

        elif self.priority == "Player":
            if newWord.getOrientation() == "Horizontal":
                for cell in newWord.cells:
                    currentWord = cell.generateWord(board, "Vertical")
                    self.scorePlayer += currentWord.getScore()
            else:
                for cell in newWord.cells:
                    currentWord = cell.generateWord(board, "Horizontal")
                    self.scorePlayer += currentWord.getScore()
            self.scorePlayer += newWord.getScore()
            self.priority = "AI"

    def turnPriority(self):
        from random import randint
        x = randint(0, 1)
        if x == 0:
            return "Player"
        else:
            return "AI"


gameBag = Bag()
gameBoard = Board(15, 15)
gameScore = Scoring()

