import os

a = open("basic.txt", "x")
a.close()

# os.path.exists check file is exists or not is file exists then it returns True if not exists it returns False
# os.remove function is used to delete a file if file is not exists it will give error
if os.path.exists("basic.txt"):
    os.remove("basic.txt")
else:
    print("File is not exists")


# os.rmdir function is used to delete a empty folder
# os.rmdir give error if folder is not empty and if folder is not exists
# os.rmdir("dir")
