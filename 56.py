my_file = open("names.txt", "a")
for i in range(100):
    my_file.write("moshe\n")
my_file.close()


def enter_name(name):
    #name = str(input("enter your name: "))
    #name = str(input("enter your name: "))
    my_file2 = open("names2.txt", "a")
    my_file2.write(name + "\n")
    my_file2.close()


def show_names():
    my_file2 = open("names2.txt")
    for name in my_file2.readlines():
        print(name + "\n", end='')
    my_file2.close()


enter_name("david")
enter_name("eli")
enter_name("dan")
show_names()





