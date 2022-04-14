def my_print(output):
    if output > 5:
        print(output)
    else:
        print("output is smaller or equal 5")


def square(number):
    return number * number


dog_prefix = "Dog bark sound like: "
def bark():
    print(dog_prefix + "Whoof Whoof")


def makesound(sound):
    sound()


makesound(bark)
