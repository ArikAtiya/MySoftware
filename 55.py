my_file = open("read_my_contents.txt")
lines = my_file.readlines()
print(lines)
for line in lines:
    print(line, end='')