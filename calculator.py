print('                                         calculator')
print('                                        -----------')

a = input("Please enter the operation ")
b = input("please enter 1st number ")
c = input("please enter 2nd number ")

if a == '+':
    print(float(b)+float(c))
elif a == '-':
    print(float(b) - float(c))
elif a == "*":
    print(float(b) * float(c))
elif a == "/":
    print(float(b) / float(c))
else:
    print("please enter the valid operation")
input()