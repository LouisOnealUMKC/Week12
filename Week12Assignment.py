import string

fileName = "test.txt"


def read_in_file(filename):
    wordList = []
    
    with open(fileName) as myFile:
        for line in myFile:
            for word in line.split():
                wordList.append(word)
    return wordList

def Make_Upper_List(inputList):
    UpperList = []
    for word in inputList:
        UpperList.append(word.upper())
    return UpperList

for word in UpperList:
    if len(word) <= 3:
        print(word)
        UpperList.remove(word)

print(UpperList)

def createMaxWordsList(inputList):
    keyCount = {}
    for word in inputList:
        if word in keyCount:
            keyCount[word] += keyCount[word] + 1
        else:
            keyCount[word] = 1
        return keyCount

WordsDict = createMaxWordsList(UpperList)
maxKey = max(WordsDict, key = WordsDict.get
print(maxKey)
print(WordsDict[maxKey])

def MainProgram():
    try:
        fileName = input("provide file name to en")
        WordsList = read_in_file(fileName)
    except:
        print('bad input')
        MainProgram()
    
    UpperList = Make_Upper_List(WordsList)

    WordCountList = createMaxWordsList(UpperList)
    
MainProgram()