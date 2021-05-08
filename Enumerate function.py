list1 = ["Banana", "Oats", "Honey", "Milk"]
a = 1
for item in list1:
    if a % 2 == 0:
        print(item)
    a += 1

for index, item in enumerate(list1):
    if index % 2 != 0:
        print(f"Buy {item}")

# enumerate gives index number and item as tuples
for n in enumerate(list1):
    print(n)

for index, item in enumerate(list1):
    print(f"{index}-{item}")


list1 = ("Banana", "Oats", "Honey", "Milk")
print(list(enumerate(list1)))

for index, item in enumerate(list1):
    print(f"{index}, {item}")

