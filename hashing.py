def hashFunc(word):
    hashCode = 0
    module = 1000000007
    power = 1
    for letter in range(len(word) - 1, -1, -1):
        hashCode += (ord(word[letter]) - ord('a') + 1) * power
        hashCode %= module
        power *= 26
    return hashCode
