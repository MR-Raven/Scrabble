from Classes import *
# CELL TESTS
cells = []
for row in range(6):
    cells.append(Cell(row, 0))
    cells[row].letter = 'a'

#WordOnBoard TESTS
firstWord = WordOnBoard(cells, "Large")
# BOARD TESTS
myBoard = Board(10, 10)
myBoard.addWord(firstWord)
myBoard.printBoard()