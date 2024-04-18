def main():
    book = "books/frankenstein.txt"
    contents = get_book(book)
    num_words = get_wordcount(contents)
    print(num_words)

def get_book(book):
    with open(book) as f:
      return f.read()

def get_wordcount(contents):
    wordcount = contents.split()
    return len(wordcount)

def leter_count(contents):
    lowercase = contents.lower()




main()