def print_upper_words(list_of_words):
    ''' this function takes a list of words, converts them to uppercase, and prints each word'''
    for word in list_of_words:
        print(word.upper())

def print_some_upper_words(list_of_words):
    ''' this function takes a list of words, converts them to uppercase, and only prints out the words that start with e or E. '''
    for word in list_of_words:
        if word.startswith('e') or word.startswith('E'):
            print(word.upper())

def print_words_with_start_letter(list_of_words, letter_at_start):
    ''' this function takes a list of words, converts them to uppercase, and only prints out the words that start with e or E. '''
    for word in list_of_words:
        for start_letter in letter_at_start:
            if word.startswith(f'{start_letter}') or word.startswith(f'{start_letter.upper()}'):
                print(word.upper())



print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])
print_some_upper_words(["hello", "ERNIE", "hey", "goodbye", "elizabeth", "yo", "yes"])
print_words_with_start_letter(["hello", "ERNIE", "hey", "goodbye", "elizabeth", "yo", "yes"], ['h', 'g'])