def main():
    book = "books/frankenstein.txt"
    contents = get_book(book)
    num_words = get_wordcount(contents)
    letters = letter_count(contents)
    report = f"--- Begin report of {book} --- \n{num_words} words found in the document \n\n\n{sort_on(letters)}"
    print(report)

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

def sort_on(letters):
    letters_list = list(letters.items())
    letters_list.sort(key=lambda x:x[1],reverse=True)
    report_str = str()
    for i in letters_list:
        report_str = report_str + (f"The '{i[0]}' character was found {i[1]} times \n")
    return report_str + "--- End report---"




main()