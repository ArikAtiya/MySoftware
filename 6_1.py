a = 7
b = 5

if a < b:
    print("a is lower than b")
elif a == b:
    print("a equals b")
else:
    print("a is bigger than b")


a = 1
b = "iteration number is:"
while a < 6:
    print(" %s %s:" % (b, a))
    #print(" %s %s" % (b, result))
    a = a + 1
else:
    print("done")