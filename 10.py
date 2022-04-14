#a = input("enter your name: ")
#result = 30 + int(a)
#print("%s" % (a))

a = input("enter your age: ")
b = "in 30 years you will be"
result = 30 + int(a)
#print(f"in 30 years you will be: {result}")
print(" %s %s" % (b, result))

c = int(input("enter first number"))
d = int(input("enter second number"))
def check_lower (c, d):
    if c < 5:
        print("the first number is lower than 5")
    if d < 10:
        print("the second number is lower than 10")
check_lower(4, 6)