from hashing import *

typeData = ["Basic", "Big", "Large", "Medium", "Small"]
forbidden = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ",", ".", "/", "-", "&", "'"]
###
hashesAI = dict()
for typeAI in typeData:
    hashesAI[typeAI] = hashTabling(typeAI)
#print(hashesAI) Working though
