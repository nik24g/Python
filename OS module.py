import os

# returns current working directory
print(os.getcwd())

# it changes working directory
# os.chdir("C:\\Users")
# print(os.getcwd())

# it used for making new directory(folder)
# os.mkdir("Nitin")


# it removes directory which should be empty
# os.rmdir("Nitin")

# it makes directory inside directory
# os.makedirs("this/that")

# it is used for rename
# os.rename("word.txt", "word01.txt")

# it returns environment variable
print(os.environ.get("path"))

# it used for joinging path
print(os.path.join("C:/", "harry.text"))

# it returns boolean if address or path exists
print(os.path.exists("C:\\Users\\Nitin\\Desktop"))

# it returns True for file and False for directory(folder)
print(os.path.isfile("pandas"))

# it returns True for directory(folder) and False for file
print(os.path.isdir("pandas"))
