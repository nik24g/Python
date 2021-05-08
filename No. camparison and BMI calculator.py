a = 1
b = 2
if a < b:
    print("A is less than B")
print("Not sured if A is less than B")
print("_______________________________________________________")
c = 6
d = 4
if c < d:
    print("C is less than d")
else:
    print("C is not less than D")
    print("I don't think C is less than D")
print("out side the if block")
print("________________________________________________________")
e = 8
f = 7
if e < f:
    print("E is less than F")
else:
    if e == f:
        print("E is equal to F")
    else:
        print("E is greater than F")
print("________________________________________________________")
g = 19
h = 9
if g < h:
    print("G is less than H")
elif g == h:
    print("G is equal to H")
elif g > h + 9:
    print("G is greater than H by more than 9")
else:
    print("G is greater than H")
print("________________________________________________________")
print("                B.M.I. CALCULATOR")
print("                -----------------")
name = "Sahil"
weight_kg = 50
height_m = 1.2
bmi = weight_kg / (height_m ** 2)
print("bmi: ")
print(bmi)
if bmi < 25:
    print(name)
    print("is not overweigth")
else:
    print(name)
    print("is overweight")
print("________________________________________________________")

power = 3**3
print(power)

