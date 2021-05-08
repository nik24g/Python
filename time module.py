import time
# import datetime

initial = time.time()
# this function is used to get total ticks with the help of ticks we can calculate programme execution time
print(initial)

list1 = ["Nitin", "Shayna", "Nik", "Kimmi"]

for a in list1:
    print(a)
print(f"For loop ran in {time.time() - initial} seconds")

print("\nwhile loop start")
initial2 = time.time()
a = 0
while a < 4:
    print(list1[a])
    a = a + 1
print(f"While loop ran in {time.time() - initial2} seconds")
print(time.time())

time.sleep(3)  # this function is used to delay the programme
localtime = time.asctime(time.localtime(time.time()))  # this function is used to get local time
print(localtime)


# hour = int(datetime.datetime.now().hour)
# print(hour)