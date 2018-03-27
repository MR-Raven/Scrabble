from Classes import *

def testNeighborsNum(board):
    print(myBoard.board[7][10].neighborsNum(board))

myBoard = Board(15, 15)
myBag = Bag()
word1 = WordOnBoardConstructor("apple", 7, 7, 'h')
word2 = WordOnBoardConstructor("like", 7, 10, 'v')
word1.isLinked = True
word2.isLinked = True
myBoard.addWord(word1)
myBoard.addWord(word2)
myBoard.printBoard()
testNeighborsNum(myBoard)

