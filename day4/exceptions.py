
# This function shows what happens if we want to do multiple tests
# within an exception. 
def exceptions_test(string_to_test):
    value = 0
    try:
        string_converted = int(string_to_test)
        value = string_converted
    except Exception as e:
        print(e)
        if len(string_to_test) > 0:
            print("Not an integer")
        else:
            print("Blank string")
    print(value)
    return value

print(__name__)
if __name__ == "__main__":
    string1 = "5666000"
    string2 = "elijah mayfield"
    string3 = ""
    exceptions_test(string1)
    exceptions_test(string2)
    exceptions_test(string3)

