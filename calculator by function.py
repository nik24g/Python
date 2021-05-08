def add(x, y):
    """This function is used for add two numbers"""
    return x + y


def sub(x, y):
    return x - y


def multi(x, y):
    return x * y


def div(x, y):
    return x / y


print("\t\tCalculator")
operator = input("Please give operator sign ")
if operator == "+":
    a = add(int(input("Enter 1st number")), int(input("Enter 2nd number")))
    print(a)
elif operator == "-":
    s = sub(int(input("Enter 1st number")), int(input("Enter 2nd number")))
    print(s)
elif operator == "*":
    m = multi(int(input("Enter 1st number")), int(input("Enter 2nd number")))
    print(m)
elif operator == "/":
    d = div(int(input("Enter 1st number")), int(input("Enter 2nd number")))
    print(d)
else:
    print("Please enter valid operator")

