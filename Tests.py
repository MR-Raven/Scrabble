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


#BAG TESTS
myBag = Bag()
myDict = {}
alphabet = ' abcdefghijklmnopqrstuvwxyz'
for letter in alphabet:
    myDict[letter] = 0
for i in range(10000):
    myDict[myBag.randomLetter()] += 1

for letter in alphabet:
    print(letter, round(myDict[letter]/100), sep="-", end=" ")
print()


# BOARD TESTS
myBoard = Board(15, 15)
c1 = Cell(5, 6)
c2 = Cell(5, 7)
c3 = Cell(5, 8)
c4 = Cell(5, 9)
c1.letter = 'n'
c2.letter = 'o'
c3.letter = 's'
c4.letter = 'e'


a = WordOnBoard([c1, c2, c3, c4], "Small")
myBoard.addWord(a)
myBoard.printBoard()
