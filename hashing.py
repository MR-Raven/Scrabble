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
    pathSorted = "/home/pavlik/Pavlik/python/Scrabble/dicts/wordsSorted" + type + ".txt"
    wordData = open(pathSorted, "r")
    pathHashes = "/home/pavlik/Pavlik/python/Scrabble/hashes/hashes" + type + ".txt"
    hashData = open(pathHashes, "r")
    # CHANGE PATH IN MY COLLEAGUES COMPUTER
    hashTable = dict()

    curWord = wordData.readline()
    while curWord:
        curHash = int(hashData.readline())
        if curWord.rstrip() == "tree":
            print(curWord, curHash)
        if curHash not in hashTable.keys():
            hashTable[curHash] = set()
            hashTable[curHash].add(curWord.rstrip())
        else:
            hashTable[curHash].add(curWord.rstrip())
        curWord = wordData.readline()
    return hashTable
