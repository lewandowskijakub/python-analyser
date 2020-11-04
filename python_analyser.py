import re

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
    counter = 0
    with open(filename, "r") as file_to_analyse:
        for line in file_to_analyse.readlines():
            if line[0] != "#":
                counter += 1
    return counter

print(count_code_lines("to_analyse.py"))
'''
count_words version I
simple - with split() - not good enough
def count_words(filename):
    # this function returns number of words in file (#,:,etc, ==, +, etc) are not words
    counter = 0
    with open(filename, "r") as file_to_analyse:
        for line in file_to_analyse.readlines():
            lines_to_analyse = line.split()
            for word in lines_to_analyse:
                if word.isalpha():
                    counter += 1
    
    return counter

'''

'''
count_words version II 
with import re.split() - ok
'''

def count_words(filename):
    # this function returns number of words in file (#,:,etc, ==, +, etc) are not words
    counter = 0
    with open(filename, "r") as file_to_analyse:
        for line in file_to_analyse.readlines():
            lines_to_analyse = re.split(r'\W+',line)
            for word in lines_to_analyse:
                if word.isalpha():
                    # print(word)
                    counter += 1
    
    return counter


print(count_words("to_analyse.py"))

def count_word(filename, word):
    # this function returns number of occurence of word in the file
    counter = 0
    with open(filename, "r") as file_to_analyse:
        for line in file_to_analyse.readlines():
            lines_to_analyse = re.split(r'\W+',line)
            for word_in_file in lines_to_analyse:
                if word.lower() == word_in_file.lower():
                    counter += 1

    return counter

print(count_word("to_analyse.py", "Class"))

def count_comment_words(filename):
    # this function returns number of words in all comments
    with open(filename, "r") as file_to_analyse:
        with open("hash_analyse","w") as file_to_write:
            for line in file_to_analyse.readlines():
                data_to_write = line
                if line[0] == "#":
                    with open("hash_analyse","a") as file_to_write:
                        file_to_write.write(data_to_write)
    
    return count_words("hash_analyse")

print(count_comment_words("to_analyse.py"))



def count_syntax(filename, syntax_word):
    # this function should handle following syntax words: if, else, elif, for, while, return, class, def, try, except
    # remember that "if" can occure in comments and commented lines of code f.e #while True: 
    # should not be counted. This function should return the number of syntax_word occurence in the file.
    pass