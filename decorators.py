var = 0
while var == 0 or var == 1:
    def dec(func):
        def iris(a, b, c):
            print(f"I am going to {a}")
            print(func(a, b, c))
            print(f"Now I have done {a}")
        return iris


    @dec
    def evaluate(a, b, c):
        if a == "add" or a == "sum" or a == "+":
            return b + c
        if a == "subtract" or a == "minus" or a == "-":
            return b - c
        if a == "multiply" or a == "multi" or a == "*":
            return b * c
        if a == "divide" or a == "div" or a == "/":
            return b / c
        return "Enter valid operator"


    try:
        operator = input("Please Enter operator: ")
        num1 = int(input("Enter 1st no: "))
        num2 = int(input("Enter 2nd no: "))
        evaluate(operator, num1, num2)
    except Exception as e:
        print(e)
        print("Please try again")
    finally:
        var = int(input("Do you want to calculate again \nif Yes press-1 \nif no press-2\nEnter: "))
