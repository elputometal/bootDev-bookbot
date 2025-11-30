from stats import countWordsInString, createDictWithEachCaracterCounted

def get_book_text(filePath):
    returnValue = ""
    with open(filePath, encoding="utf-8") as f:
        returnValue = f.read()
    
    return returnValue

def main():
    numOfWords = countWordsInString(get_book_text("books/frankenstein.txt"))
    charDict = createDictWithEachCaracterCounted(get_book_text("books/frankenstein.txt"))
    print(f"Found {numOfWords} total words. Character counts below: \n")
    print(charDict)

main()