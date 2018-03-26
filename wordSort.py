from hashing import hashFunc
from config import *

def forbiddenCheck(curWord):
    flag = True
    for i in range(len(curWord)):
        if len(curWord) <= 3 or curWord[i] in forbidden or (curWord[i] == curWord[i].upper() and curWord[i] != '\n'):
            flag = False
            break
    for i in range(2, len(curWord)):
        if curWord[i] == curWord[i - 1] == curWord[i - 2]:
            flag = False
            break
    return flag

def sorting(wordDataUnsorted, type):
    firstWordsPath = "/home/pavlik/Pavlik/python/Scrabble/dicts/wordsSorted"  # The first path is for Pavlik, the second one is for Pavel
    secondWordsPath = "/home/pavel/MyDocs/Programming/Python/Scrabble/dicts/wordsSorted"
    firstHashesPath = "/home/pavlik/Pavlik/python/Scrabble/hashes/hashes"
    secondHashesPath = "/home/pavel/MyDocs/Programming/Python/Scrabble/hashes/hashes"
    pathSorted = firstWordsPath + type + ".txt"
    wordDataSorted = open(pathSorted, "w")
    pathHashes = firstHashesPath + type + ".txt"
    hashesData = open(pathHashes, "w")
    curWord = wordDataUnsorted.readline()

    differentHashes = set() ### Collisions counter
    usedWords = set()
    while curWord:
        if forbiddenCheck(curWord) and curWord not in usedWords:
            usedWords.add(curWord)
            wordDataSorted.write(curWord)
            differentHashes.add(hashFunc(curWord))
            hashesData.write(str(hashFunc(curWord.rstrip())) + '\n')
        curWord = wordDataUnsorted.readline()
    print(len(usedWords), len(differentHashes))

    wordDataSorted.close()

# Full-sized Sort + Hashingas
for type in typeData:
    firstUnsortedPath = "/home/pavlik/Pavlik/python/Scrabble/dicts/wordsUnsorted"  # The first path is for Pavlik, the second one is for Pavel
    secondUnsortedPath = "/home/pavel/MyDocs/Programming/Python/Scrabble/dicts/wordsUnsorted"
    path = firstUnsortedPath + type + ".txt"
    # CHANGE PATH IN MY COLLEAGUES COMPUTER
    wordDataUnsorted = open(path, "r")
    sorting(wordDataUnsorted, type)
    wordDataUnsorted.close()
