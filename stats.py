def _sort_on(items):
    return items["num"]

def countWordsInString(string):
    wordList = string.split()
    return len(wordList)

def createDictWithEachCaracterCounted(string):
    inputString = string.lower()
    charDict = {}
    for char in inputString:
        if char.isalpha() == True:
            if char in charDict:
                charDict[char] += 1
            else:
                charDict[char] = 1
    
    return charDict

def dictToSortedListByValue(inputDict):
    #print(inputDict)
    outputList = []
    for element in inputDict:
        dict = {"char": element, "num": inputDict[element]}
        outputList.append(dict)
        #print(dict)
    
    outputList.sort(key=_sort_on, reverse=True)
    #print(outputList)
    return outputList