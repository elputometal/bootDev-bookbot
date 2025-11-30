def __sort_on(items):
    return items["num"]

def countWordsInString(string):
    wordList = string.split()
    return len(wordList)

def createDictWithEachCaracterCounted(string):
    inputString = string.lower()
    charDict = {}
    for char in inputString:
        if char in charDict:
            charDict[char] += 1
        else:
            charDict[char] = 1
    
    return charDict

def sortDictByKey(inputDict):
    outputList = []
    for element in inputDict:
        outputList.append({
            "char": element,
            "num": inputDict[element]
        })
    return outputList.sort(key=__sort_on)