import string

def read_in_file(filename):
    wordList = []
    with open(filename) as myFile:
        for line in myFile:
            for word in line.split():
                wordList.append(word)
    return wordList

def Make_Upper_List(inputList):
    UpperList = []
    for word in inputList:
        UpperList.append(word.upper())
    for word in UpperList:
        if len(word) <= 3:
            print(word)
            UpperList.remove(word)
    return UpperList

def createMaxWordsList(inputList):
    keyCount = {}
    for word in inputList:
        if word in keyCount:
            keyCount[word] += keyCount[word] + 1
        else:
            keyCount[word] = 1
        return keyCount

def MainProgram():
    try:
        #fileName = input("provide file name to en")
        fileName = "test.txt"
        WordsList = read_in_file(fileName)
    except:
        print('bad input')
        MainProgram()
    
    UpperList = Make_Upper_List(WordsList)

    WordCountList = createMaxWordsList(UpperList)

    maxKey = max(WordCountList, key = WordCountList.get)

    print(maxKey)
    print(WordCountList[maxKey])
    
MainProgram()