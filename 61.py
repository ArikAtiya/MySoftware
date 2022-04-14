try:
    first_number = int(input("enter first number: "))
    second_number = int(input("enter second number: "))
    result = first_number / second_number
    print(result)
except ZeroDivisionError as excp:
    print("could not divide by zero")
except ValueError as excp:
    print("one of the variables is not a number")

print("finished")
