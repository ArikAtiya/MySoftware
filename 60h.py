from PIL import Image
# 1, 2
try:
    a = 1 / 0
    result = a
    print(a)
except ZeroDivisionError as excp:
    print("could not divide by zero")

print("finished")

# 3 - Yes
try:
    x = 1
finally:
    print("finally")


# 4 - Devide by Zero, Value error
# 5 - It is not a specific exception. It will catch any exception.
# 6 except IOError - input/output error, for example when you want to use a parameter from a file which is not available
# 6 except ZeroDivisionError - devide by zero error


# 7, 8
def create_file():
    my_file = open("words.txt", "a+")
    my_file.write("arik\n")
    my_file.close()


# 9
def read_file():
    my_file = open("words.txt")
    for name in my_file:
        print(name + "\n")

# 10
def add_hebrew():
    my_file = open("words.txt", "a+", encoding='utf-8')
    my_file.write("אריק")
    my_file.close()


create_file()
add_hebrew()
read_file()


# 11
img = Image.new('RGB', (60, 30), color='red')
img.save('pil_red.png')
