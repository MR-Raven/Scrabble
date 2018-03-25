from config import *

def hashFunc(word):
    hashCode = 0
    module = 1000000007
    power = 1
    for letter in range(len(word) - 1, -1, -1):
        hashCode += (ord(word[letter]) - ord('a') + 1) * power
        hashCode %= module
        power *= 26
    return hashCode

def hashTabling(type):
    pathSorted = "/home/pavlik/Pavlik/python/Scrabble/dicts/wordsSorted" + type + ".txt"
    wordData = open(pathSorted, "r")
    pathHashes = "/home/pavlik/Pavlik/python/Scrabble/hashes/hashes" + type + ".txt"
    hashData = open(pathHashes, "r")
    # CHANGE PATH IN MY COLLEAGUES COMPUTER
    hashTable = dict()

    curWord = wordData.readline()
    while curWord:
        curHash = int(hashData.readline())
        if curHash not in hashTable.keys():
            hashTable[curHash] = set()
            hashTable[curHash].add(curWord[:-1])
        else:
            hashTable[curHash].add(curWord[:-1])
        curWord = wordData.readline()

    return hashTable

hashesNative = dict()
typeNative = "Huge"

hashesAI = dict()
typeAI = input()
while typeAI not in typeData:
    print("No such level, try again")
    typeAI = input()
hashesNative = hashTabling(typeNative)
hashesAI = hashTabling(typeAI)
print(hashesAI)
