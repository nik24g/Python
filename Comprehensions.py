# comprehensions
# lst = list()
# for i in range(20):
#     if i % 2 == 1:
#         lst.append(i)
# print(lst)

# list comprehensions
lst = [i for i in range(20) if i % 2 == 1]
print(lst)

# dictionary comprehensions
# dic = {1: "item1", 2: "item2", 3:"item3"}
dic1 = {i: f"item{i}" for i in range(20)}
print(dic1)

# reverse dictionary using comprehensions
dic2 = {value: key for key, value in dic1.items()}
print(dic2)

# set comprehensions
lst = [1, 3,  6, 8, 22, 2, 6, 3, 5, 8, 10]
sett = {i for i in lst if i % 2 == 1}
print(sett)

# generator making
tup = (i for i in range(20) if i % 2 == 1)
print(tup.__next__())
print(tup.__next__())
print(tup.__next__())
for i in tup:
    print(i)
