file = open("info.txt", "wt")  # when we open a file in write mode it will overwrite the content
print(file.write("Hello "))  # write method is used to write a content in a file
file.close()
# note-- write mode and write method both are different

file = open("info.txt", "a")  # if file open in a append mode it add content to the end of the file
print(file.tell())
a = file.write("Shayna")  # write method returns no. of total characters that we have written
# print(file.read())
print(a)
file.close()


file = open("info.txt", "r+")  # + mode is used to read and write
file.write("is anyone there?")
print(file.tell())
# file.seek(1)
# print(file.read())
print(file.readline())
print(file.tell())
print(file.readline())
file.seek(0)
print(file.readline())
file.close()
