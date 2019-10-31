# This function takes one parameter as input: 
#     names_list: A list of strings.
# 
# The function looks for the longest string in the list, prints it,
# then saves the result to a local file.
# 
# This function does not return any values.
def find_longest_name(names_list):
    record = 0
    for name in names_list:
        temporary = len(name)
        
        # Look for the longest name of all 50 states.
        if temporary > record:
            longest_row = name
            record = temporary

        result_string = longest_row
        print(f"The new longest row is {longest_row}, length {record}")

    with open("longest_row_result.txt", "w") as result_file:
        result_file.write(result_string)

# This function takes two parameters as input: 
#    names_list: A list of strings
#    letter_to_check: a string of length 1.
# 
# The function then counts the number of strings in the list that have the
# letter to check as their first character, and prints the sum.
#
# This function does not return any values.
def find_names_starting_with(names_list, letter_to_check):
    number_starting_with = 0
    for name in names_list:
        if name[0] == letter_to_check:
            number_starting_with += 1
    print(f"The number of names starting with {letter_to_check} is {number_starting_with}")

# We can use lists to loop through multiple data files.
files_to_process = ["state_names.txt", "animal_names.txt"]

# This code loops through each file in our list. For each, it saves all the contents to 
# a list, then calls two functions (find_longest_name and find_names_starting_with)
# on the contents of that list.
for this_file in files_to_process:
    names_list = []
    with open(this_file) as single_file_to_process:
        for row in single_file_to_process.readlines():
            names_list.append(row.strip())
    print(len(names_list))
    find_longest_name(names_list)
    find_names_starting_with(names_list, "Z")
