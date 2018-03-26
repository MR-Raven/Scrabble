from hashing import hashFunc
from itertools import permutations

# NESSESARY?
class Alphabet:
    alphabetSize = 26
    letters = [chr(ord('a') + i) for i in range(26)]


class Word: ### !!! STRING IS STORING WITHOUT \n SYMBOL (use .rstrip()), HASH'S ALSO COUNTING THIS WAY HERE AND IN SORTING !!!
    def __init__(self, string, type): # Is local copy of type really nessesary?
        self.string = string.rstrip()
        self.dictType = type
        self.hash = hashFunc(self.string)
    def isWord(self):
        from config import hashesAI
        return self.hash in hashesAI[self.dictType].keys() and self.string in hashesAI[self.dictType][self.hash]
    def allPermutations(self):
        permutationsData = set()
        for psiWord in permutations(self.string, len(self.string)):
            curString = ""
            for letter in psiWord:
                curString += letter
            curWord = Word(curString, self.dictType)
            if curWord.isWord():
                permutationsData.add(curWord.string) # STRING JUST TO TEST
        return permutationsData
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

# Test
slovo = Word("zakharov", "Big")
print(slovo.subWords())

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Cell:
    def __init__(self, coord, letter, bonus):
        from config import bonuses
        self.x = coord.x
        self.y = coord.y
        self.letter = letter
        self.bonus = bonuses(coord)
