# Exercise 2 - Faulty Calculator
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result
print('                                         calculator')
print('                                         ----------')

a = input("Please enter the operation ")

b = float(input("please enter 1st number "))
c = float(input("please enter 2nd number "))

if a == '+':
    if b == 56 and c == 9:
        print("77")
    else:
        print(b+c)
elif a == '-':
    sub = b-c
    print(sub)
elif a == "*":
    if b == 45 and c == 3:
        print("555")
    else:
        multi = b*c
        print(multi)
elif a == "/":
    if b == 56 and c == 6:
        print("4")
    else:
        div = b/c
        print(div)
else:
    print("please enter the valid operation")
