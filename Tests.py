from Classes import *
# CELL TESTS
cells = []
for row in range(5):
    cells.append(Cell(row, 0))
cells[0].letter = 'a'
cells[1].letter = 'p'
cells[2].letter = 'p'
cells[3].letter = 'l'
cells[4].letter = 'e'



#WordOnBoard TESTS
firstWord = WordOnBoard(cells, "Large")



# BOARD TESTS
myBoard = Board(10, 10)
myBoard.addWord(firstWord)
myBoard.printBoard()
