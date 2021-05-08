# join function is used to join the elements of list or tuple or set or dictionary by string
# join function will only work for strings elements if there is any number in iterable then it will give error

name = ("Nitin", "Shayna","Love")
a = " ".join(name)
print(a)

name1 = ["Nitin", "Shayna"]
b = " love ".join(name1)
print(b)

name2 = {"Nitin", "Shayna"}
c = " love ".join(name2)
print(c)

name3 = {
    "Nitin": "Student",
    "Shayna": "Student"
}
d = " love ".join(name3.values())
print(d)

# sum function returns addition of all elements of integer iterable
lst = list(range(0, 9))
result = sum(lst)
print(result)

tup = tuple(range(0, 9))
result1 = sum(tup)
print(result1)

sett = set(range(0, 9))
result2 = sum(sett)
print(result2)

dic = {1: "value1", 2: "value2", 3: "value3", 4: "value4", 5: "value5", 6: "value6", 7: "value7"}
result3 = sum(dic)
print(result3)
