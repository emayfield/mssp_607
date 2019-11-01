# This code is almost identical to what we used in class two weeks ago.
# It uses no libraries, just built-in python.
def build_states(states_filename):
    file_rows = []
    with open(states_filename) as states_file:
        for row in states_file.readlines():
            row_text = row.strip()
            file_rows.append(row_text)

    states = []
    row_num = 0
    for state_string in file_rows:
        if row_num > 0:
            # Start with string that looks like "XXXXXX,000000"
            # .split() replaces this string with a list: ["XXXXXX", "00000"]
            split_string = state_string.split(",")
            state_name = split_string[0]
            state_population = int(split_string[1])
            state_dictionary = {
                "name": state_name,
                "population": state_population
            }
            states.append(state_dictionary)
        row_num += 1

    print(f"We created {len(states)} dictionaries.")
    return states


# This alternate implementation of the same code uses the CSV library,
# which is built in to Python. You can add libraries with the import statement.
# Then, you can call functions defined in that library
import csv

def build_states_csv(states_filename):
    states = {}
    with open(states_filename) as states_file:

        # The csv library contains a function named reader() which does a lot of our work
        # for us, without having to go to the trouble of splitting on commas, etc.
        states_reader = csv.reader(states_file)

        # The enumerate function in a for loop lets us keep track of what row we're on, 
        # without having to separately keep track of a row number.
        for i, state in enumerate(states_reader):
            if i > 0:
                # The comma syntax lets us assign multiple values at a time, but the number
                # of values on the left and right sides of the assignment operator (=)
                # must be the same.
                name, population = state

                # The try/except syntax below is also new, and allows us to attempt to do something when
                # we're not sure that all of our data will be perfectly clean or behave the way we want.
                # One common use of this syntax is to test whether strings are integers.
                population_int = 0
                try:
                    population_int = int(population)
                    states[name] = population_int
                except:
                    print(f"Failed to convert population for state {name} to an integer: {population}.")
                
    print(f"We created {len(states)} dictionaries.")
    return states

# This code will only run if we run this file specifically; we can still use this file as an import
# in other places in our code and the lines below will not run.
if __name__ == "__main__":
    build_states("state_sizes.csv")
    build_states_csv("state_sizes.csv")