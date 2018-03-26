def hashFunc(word): # Making something trickier doesn't make sence not mainly but also in case of removing huge dictionary
    hashCode = 0
    module = 1000000007
    power = 1
    for letter in range(len(word) - 1, -1, -1):
        hashCode += (ord(word[letter]) - ord('a') + 1) * power
        hashCode %= module
        power *= 26
    return hashCode

def hashTabling(type):
    firstWordsPath = "/home/pavlik/Pavlik/python/Scrabble/dicts/wordsSorted"     # The first path is for Pavlik, the second one is for Pavel
    secondWordsPath = "/home/pavel/MyDocs/Programming/Python/Scrabble/dicts/wordsSorted"
    firstHashesPath = "/home/pavlik/Pavlik/python/Scrabble/hashes/hashes"
    secondHashesPath = "/home/pavel/MyDocs/Programming/Python/Scrabble/hashes/hashes"
    pathSorted = secondWordsPath + type + ".txt"
    wordData = open(pathSorted, "r")
    pathHashes = secondHashesPath + type + ".txt"
    hashData = open(pathHashes, "r")
    hashTable = dict()

    curWord = wordData.readline()
    while curWord:
        curHash = int(hashData.readline())
        if curHash not in hashTable.keys():
            hashTable[curHash] = set()
            hashTable[curHash].add(curWord.rstrip())
        else:
            hashTable[curHash].add(curWord.rstrip())
        curWord = wordData.readline()
    return hashTable
