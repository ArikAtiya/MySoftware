my_dictionary = {"name": "arik", "age": 48, "hobbies": ["design", "music"]}
my_dictionary2 = {"city": "tlv", "zip": 360, "state": "israel"}

print(my_dictionary.keys())
print(my_dictionary.values())

for key in my_dictionary.keys():
    print(my_dictionary[key])

if 48 in my_dictionary.values():
    print("48 is in the list")


def dictionary_validator(any_dictionary):
    if "name" in list(any_dictionary.keys()):
        if "age" in list(any_dictionary.keys()):
            if "hobbies" in list(any_dictionary.keys()):
                print("name, age, hobbies are in the dictionary")
                return True
            return False
        return False
    return False


dictionary_validator(my_dictionary)
dictionary_validator(my_dictionary2)
