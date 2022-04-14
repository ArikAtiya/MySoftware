isTrue = False
a = 2
b = 2.5
strOne = "One"
strThree = "Three"
first_array = []
second_array = [1, 2, 3]

if a < b and strOne != strThree or not isTrue:
    print("a is lower than b")
elif a == b or strOne == "3":
    print("a equals b")
else:
    print("a is not lower than b")

if 0 <= a <= 4:
    print("a between 0 and 4")

if first_array:
    print("first_array has elements")
if len(second_array) > 2:
    print("second_array has more than 2 elements")
c = 5
d = 5
e = [1, 2, 3]
f = [1, 2, 3]
if c == d:
    print("c equals d")
if c is d:
    print("c is d")
if e == f:
    print("e equals f")
if e is f:
    print("e is f")
if type(c) is int:
    print("c is integer")