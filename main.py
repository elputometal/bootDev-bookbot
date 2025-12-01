from stats import countWordsInString, createDictWithEachCaracterCounted, dictToSortedListByValue
import sys

def get_book_text(filePath):
    returnValue = ""
    with open(filePath, encoding="utf-8") as f:
        returnValue = f.read()
    
    return returnValue

def main():
    bookpath = "books/frankenstein.txt"
    if len(sys.argv) > 1:
        bookpath = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
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