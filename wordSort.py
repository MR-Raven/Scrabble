from hashing import hashFunc

def sorting(wordDataUnsorted, type):
    pathSorted = "/home/pavlik/Pavlik/python/Scrabble/dicts/wordsSorted" + type + ".txt"
    wordDataSorted = open(pathSorted, "w")
    pathHashes = "/home/pavlik/Pavlik/python/Scrabble/hashes/hashes" + type + ".txt"
    hashesData = open(pathHashes, "w")

    forbidden = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ",", ".", "/", "-", "&", "'"]
    flag = True
    curWord = wordDataUnsorted.readline()
    sz1 = 0
    st = set()
    while curWord:
        flag = True
        for i in range(len(curWord)):
            if len(curWord) <= 3 or curWord[i] in forbidden or (curWord[i] == curWord[i].upper() and curWord[i] != '\n'):
                flag = False
                break
        for i in range(2, len(curWord)):
            if curWord[i] == curWord[i - 1] == curWord[i - 2]:
                flag = False
                break
        if flag:
            wordDataSorted.write(curWord)
            st.add(hashFunc(curWord))
            sz1 += 1
            hashesData.write(str(hashFunc(curWord)) + '\n')
        curWord = wordDataUnsorted.readline()
    print(sz1, len(st))

    wordDataSorted.close()

typeData = ["Basic", "Big", "Huge", "Large", "Medium", "Small"]

for type in typeData:
    path = "/home/pavlik/Pavlik/python/Scrabble/dicts/wordsUnsorted" + type + ".txt"
    wordDataUnsorted = open(path, "r")
    sorting(wordDataUnsorted, type)
    wordDataUnsorted.close()
