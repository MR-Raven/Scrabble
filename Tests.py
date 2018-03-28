from Classes import *
print(hashFunc("appl"))
myBoard = Board(15, 15)
myBag = Bag()
word1 = WordOnBoardConstructor("appl", 0, 0, 'h')
word2 = WordOnBoardConstructor("like", 0, 3, 'v')
word1.isLinked = True
word2.isLinked = True
cell1 = Cell(0, 4, 'e')
word1.addLetter(cell1, True)
myBoard.addWord(word1)
myBoard.printBoard()
""" TEST NeighborsNum

def testNeighborsNum(row, col):
    print(myBoard.board[row][col].letter, myBoard.board[row][col].neighborsNum(myBoard), sep="-")
word1 = WordOnBoardConstructor("apple", 0, 0, 'h')
word2 = WordOnBoardConstructor("like", 0, 3, 'v')
word1.isLinked = True
word2.isLinked = True
myBoard.addWord(word1)
myBoard.addWord(word2)
myBoard.printBoard()
testNeighborsNum(0, 0)
testNeighborsNum(0, 3)
testNeighborsNum(0, 2)
"""


