from stats import countWordsInString, createDictWithEachCaracterCounted, dictToSortedListByValue

def get_book_text(filePath):
    returnValue = ""
    with open(filePath, encoding="utf-8") as f:
        returnValue = f.read()
    
    return returnValue

def main():
    bookpath = "books/frankenstein.txt"
    numOfWords = countWordsInString(get_book_text(bookpath))
    charDict = createDictWithEachCaracterCounted(get_book_text(bookpath))
    sortedDictList = dictToSortedListByValue(charDict)
    
    print(f"============ BOOKBOT ============\n")
    print(f"Analyzing book found at {bookpath}...")
    print(f"----------- Word Count ----------\n")
    print(f"Found {numOfWords} total words.\n")
    print(f"--------- Character Count -------\n")

    for item in sortedDictList:
        print(f"{item['char']}: {item['num']}\n")

    print("============= END ===============")

main()