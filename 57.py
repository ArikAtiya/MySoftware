def enter_name():
    name = str(input("enter your name: "))
    my_file = open("names.txt", "a")
    my_file.write(name + "/")
    my_file.close()


def show_names():
    my_file = open("names.txt")
    for name in my_file.readlines():
        print(name + "/")


#with open("names.txt") as