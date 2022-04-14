my_range = list(range(5))
print(my_range)
my_range2 = list(range(-1, 5))
print(my_range2)
my_range3 = list(range(-1, 5, 2))
print(my_range3)

for i in range(5):
    print(i)

for i2 in range(-9, 5, 3):
    print(i2)

names = ["yekutiel", "ginat", "adi", "eliasaf", "yossi"]
for name in names:
    if name == "eliasaf":
        continue
    print(name)
    if name == "adi":
        print("I've found adi, exiting ...")
        break
else:
    print("loop finished successfully")
if "yekutiel" in names:
    print("yekutiel in names")
for i in range(len(names)):
    print(names[i])
    print(len(names))

a = 0
while a < 5:
    print(a)
    a = a + 1
else:
    print("done")

b = 0
if b < 5:
    print(b)
    b = b + 1
else:
    print("done2")

c = 0
if c == 0:
    pass
else:
    print("a is not 0")
