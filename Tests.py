from Classes import *
# CELL TESTS
cells = []
for row in range(5):
    cells.append(Cell(row, 0))
cells[0].setLetter('a')
cells[1].setLetter('p')
cells[2].setLetter('p')
cells[3].setLetter('l')
cells[4].setLetter('e')



#WordOnBoard TESTS
firstWord = WordOnBoard(cells, "Large")


#BAG TESTS
myBag = Bag()
myDict = {}
alphabet = ' abcdefghijklmnopqrstuvwxyz'
for letter in alphabet:
    myDict[letter] = 0
for i in range(50):
    myDict[myBag.randomLetter()] += 1

for letter in alphabet:
    print(letter, myDict[letter], sep="-", end=" ")
print()


# BOARD TESTS
myBoard = Board(15, 15)
c1 = Cell(5, 6)
c2 = Cell(5, 7)
c3 = Cell(5, 8)
c4 = Cell(5, 9)
c1.setLetter('n')
c2.setLetter('o')
c3.setLetter('s')
c4.setLetter('e')


a = WordOnBoard([c1, c2, c3, c4], "Small")
myBoard.addWord(a)
myBoard.printBoard()
