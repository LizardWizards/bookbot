def main():
    bookPath = "books/frankenstein.txt"
    contents = getBookText(bookPath)
    wordCount = getWordCount(contents)
    charCounts = getCharCounts(contents)

    print(f"{wordCount} words found in the document")
    print("")

    for charCount in charCounts:
        if charCount.isalpha():
            count = charCounts[charCount]
            print(f"The '{charCount}' was found {count} times")
    
def getWordCount(contents):
    count = 0
    words = contents.split()
    for word in words:
        count += 1
    return count

def getBookText(path):
    with open("books/frankenstein.txt") as book:
        contents = book.read()
        book.close()
        return contents
    
def getCharCounts(text):
    counts = {}
    for char in text:
        char = char.lower()
        if not char in counts:
            counts[char] = 1
        else:
            counts[char] += 1
    return counts

main()