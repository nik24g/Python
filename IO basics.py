# File IO Basics
"""
"r" - open file for reading -- default
"w" - Open a file for writing
"x" - add Creates file if not exists
"a" - Add more content to a file (add content at the end of the file)
"t" - text mode -- default
"b" - binary mode
"+" - read and write
"""

# open() function open file
# open() function takes two arguments 1st is for file name and 2nd is for mode of file
# read() method is used for reading full file
file = open("love.txt", "rt")
# content = file.read()
# print(f"1- {content}")
content = file.read()
print(f"2- {content}")
file.close()  # close() function is used for closing file. If open a file it is good habit to close a file

# readline is used to read file's one line
# if we want file's second line then use again readline method
file = open("love.txt", "rt")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

# for loop in file is used to print file lines by line by line
file = open("love.txt", "rt")
for a in file:
    print(a)
file.close()

# readlines method is returns list of lines that is written in file
file = open("love.txt")
print(file.readlines())
file.close()