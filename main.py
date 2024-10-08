def main():
    bookPath = "books/frankenstein.txt"
    contents = getBookText(bookPath)
    count = getWordCount(contents)
    print(count)
    
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
    
main()