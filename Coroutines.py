import time
# coroutines are initialize a function for first time after that it will run half
# for initializing coroutine, we will make a instance(object) of coroutine and use next function on it
# for sending value to yield statement, we will use send method
# when we have done with coroutine we will close it by using close method


def searcher():
    # task consuming time 5 seconds
    book = "This is book on python and programming with easy concepts and is good"
    time.sleep(5)

    while True:
        text = (yield)
        if text in book:
            print("Your text in the book")
        else:
            print("Text is not in the book")


search = searcher()
print("starting searching")
next(search)
# search.__next__()
print("Next function is used")
input("press for send")
search.send("Shayna")
input("Press any key")
search.send("python")
search.close()

