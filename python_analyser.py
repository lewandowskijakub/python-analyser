def count_lines(filename):
    with open(filename, "r") as file_to_analyse:
        return len(file_to_analyse.readlines())

print(count_lines("to_analyse.py"))

def is_not_empty_line(line):
    line = line.replace(" ", "")
    line = line.replace("\t", "")
    line = line.replace("\r", "")
    line = line.replace("\n", "")
    return len(line) != 0

def count_not_empty_lines(filename):
    counter = 0
    with open(filename, "r") as file_to_analyse:
        for line in file_to_analyse.readlines():
            if is_not_empty_line(line):
               counter += 1

    return counter 

print(count_not_empty_lines("to_analyse.py"))

def count_comment_lines(filename):
    # this function returns number of comment lines
    # dont forget that comment starts with hash "#" 
    counter = 0
    with open(filename, "r") as file_to_analyse:
        for line in file_to_analyse.readlines():
            if line[0] == "#":
                counter += 1
    
    return counter

print(count_comment_lines("to_analyse.py"))


def count_code_lines(filename):
    # this function returns number of code lines
    pass

def count_words(filename):
    # this function returns number of words in file (#,:,etc, ==, +, etc) are not words
    pass

def count_word(filename, word):
    # this function returns number of occurence of word in the file
    pass

def count_comment_words(filename):
    # this function returns number of words in all comments
    pass


def count_syntax(filename, syntax_word):
    # this function should handle following syntax words: if, else, elif, for, while, return, class, def, try, except
    # remember that "if" can occure in comments and commented lines of code f.e #while True: 
    # should not be counted. This function should return the number of syntax_word occurence in the file.
    pass