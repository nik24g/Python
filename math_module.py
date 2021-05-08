import math as m
lst = [6, 9, 55, 8, 51, 62, 74, 36, 59, 23, 87, 94, 96, 92, 97, 75, 72]
print(max(lst))
print(min(3, 9, 6, 5))

# sort is used for arranging the list in increasing order
# if argument in sort is reverse=True then it will arranging in descending order
lst.sort()
# lst.sort(reverse=True)
print(lst)

# sqrt method is used for calculating square root
a = m.sqrt(121)
print(a)

# abs returns absolute value(positive)
b = abs(-62.96)
print(b)

c = m.fabs(-62.96)
print(c)

# constants
print(m.pi)
print(m.e)
print(m.tau)

# sin,tan,cos angles
print(m.sin(360))
print(m.cos(45))
print(m.tan(90))

# factorial returns factorial value
print(m.factorial(1000))

# radian and degree are units of angles
print(m.radians(90))
print(m.degrees(1.5707963267948966))

# pow is for power
print(pow(6, 3))

# ceil return nearest integer
print(m.ceil(1.1))
