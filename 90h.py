import os


my_file = open("/home/arik/Desktop/name.txt", "a")
my_file.write("Arik\n")
my_file.close()


def show_names():
    my_file2 = open("/home/arik/Desktop/name.txt")
    for name in my_file2.readlines():
        print(name + "\n", end='')
    my_file2.close()


def move_folders():
    os.replace("/home/arik/Desktop/name.txt", "/home/arik/Downloads/name.txt")


show_names()
move_folders()