from hashing import hashFunc
from config import *

def forbiddenCheck(curWord):
    flag = True
    forbidden = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ",", ".", "/", "-", "&", "'"]
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
    pathSorted = "/home/pavlik/Pavlik/python/Scrabble/dicts/wordsSorted" + type + ".txt"
    # CHANGE PATH IN MY COLLEAGUES COMPUTER
    wordDataSorted = open(pathSorted, "w")
    pathHashes = "/home/pavlik/Pavlik/python/Scrabble/hashes/hashes" + type + ".txt"
    # CHANGE PATH IN MY COLLEAGUES COMPUTER
    hashesData = open(pathHashes, "w")
    curWord = wordDataUnsorted.readline()

    differentHashes = set() ### Collisions counter
    usedWords = set()
    while curWord:
        if forbiddenCheck(curWord) and curWord not in usedWords:
            usedWords.add(curWord)
            wordDataSorted.write(curWord)
            differentHashes.add(hashFunc(curWord))
            hashesData.write(str(hashFunc(curWord)) + '\n')
        curWord = wordDataUnsorted.readline()
    print(len(usedWords), len(differentHashes))

    wordDataSorted.close()

# Full-sized Sort + Hashingas
for type in typeData:
    path = "/home/pavlik/Pavlik/python/Scrabble/dicts/wordsUnsorted" + type + ".txt"
    # CHANGE PATH IN MY COLLEAGUES COMPUTER
    wordDataUnsorted = open(path, "r")
    sorting(wordDataUnsorted, type)
    wordDataUnsorted.close()
