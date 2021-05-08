import random

a = random.randint(0, 10)  # random.randint() gives you random integer
print(a)

b = random.random() * 10  # random.random() gives you random number
print(b)

lst = ['Nitin', 'Love', 'Shayna']
ns = random.choice(lst)  # random.choice() gives you random value from list, tuples or dictionary
print(ns)
