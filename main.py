def main():
    book = "books/frankenstein.txt"
    contents = get_book(book)
    num_words = get_wordcount(contents)
    letters = letter_count(contents)
    print(letters)

def get_book(book):
    with open(book) as f:
      return f.read()

def get_wordcount(contents):
    wordcount = contents.split()
    return len(wordcount)

def letter_count(contents):
    lowercase = contents.lower()
    lower_list =list(lowercase)
    letter_dict = {}
    for i in lower_list:
        if i in letter_dict:
            letter_dict[i] += 1
        elif i.isalpha():
            letter_dict[i] = 1
    return letter_dict




main()