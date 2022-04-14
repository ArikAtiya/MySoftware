user_name_input = input("enter your name")
user_gender = input("write your gender: 'male' or 'female'")
if user_gender == "male":
    print("hello mr:" + user_name_input)
else:
    print("hello ms:" + user_name_input)


my_list = ["first_item", 3, True, "last_item"]
for i in range(len(my_list)):
    print("the value in: " + str(i) + " is " + str(my_list[i]))