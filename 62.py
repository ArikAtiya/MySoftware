def get_age():
    age = float(input("enter your age: "))
    if age < 0:
        raise ValueError("age can't be negative")
    else:
        print(age)


try:
    get_age()
except ValueError as excp:
    print(excp.args[0])

