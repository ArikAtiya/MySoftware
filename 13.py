from utils import my_print as my_print_utils
from utils import square
my_print_utils(7)


my_number = input("enter a number")
print(square(int(my_number)))

#Write a function that takes a number and return the word corresponding to that number
def get_numeric (number):
    numbers = ["zero", "one", "two", "three", "four"]
    numbers.append("five")
    if number < len(numbers):
        return numbers[number]
    else:
        return "not supported"



input_from_user = int(input("please enter a number: "))
if 0 < input_from_user < 5:
    print(get_numeric(input_from_user))
else:
    print("the number is not between '0' to '5'")


