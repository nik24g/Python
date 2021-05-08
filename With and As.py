file = open("love.txt", "rt")
print(file.read())
file.close()

# It is new syntax of open a file and close a file in file handling
with open("love.txt", "rt") as file:
    print(file.read())

with open("info.txt", "at") as file:
    file.write("Nitin")
