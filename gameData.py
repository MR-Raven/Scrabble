from Classes import *

class Scoring:
    def __init__(self):
        scoreAI = 0
        scorePlayer = 0

    def updateScore(self, word):
        from gameData import turnPriority, priority
        if priority == "AI":
            self.scoreAI += word.getScore()
            priority= "Player"
        elif priority == "Player":
            self.scorePlayer += word.getScore()
            priority = "AI"


def turnPriority(self):
    from random import randint
    x = randint(0, 1)
    if x == 0:
        return "Player"
    else:
        return "AI"


gameBag = Bag()
gameBoard = Board(15, 15)
allWords = []
priority = turnPriority() # Priority is a string ("AI" or "Player")

