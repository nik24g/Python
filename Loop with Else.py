lst = ['Banana', 'Milk', 'Oats', 'Honey']

for a in lst:
    print(a)
    pass
# else will execute when for loop is end naturally
# if it will end by break statement then else will not execute
else:
    print("List is complete")

for a in lst:
    if a == "Banana":
        break
    # if a == "Sugar":
    #     break

else:
    print("Item not found")

# else will execute when while loop is end naturally
# if it will end by break statement then else will not execute
i = 0
while i < 5:
    # if i == 3:
    #     break
    print(i)
    i += 1

else:
    print("While loop is complete")