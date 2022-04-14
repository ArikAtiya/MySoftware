def show_names():
    my_file2 = open("/home/arik/Desktop/name.txt")
    for name in my_file2.readlines():
        print(name + "\n", end='')
    my_file2.close()



show_names()