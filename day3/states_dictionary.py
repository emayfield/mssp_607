
# This function takes as input a list.
# Each item in the list is a string, with the following format:
#   XXXXXXXX,0000000
# Where the first part of the string is a state name.
# The second part is an integer representing the population of that state.
#
# This function returns a new list, where instead of a string for each state,
# we have a dictionary with the following keys:
# {
#  "name": XXXXX
#  "population": 0000
# }
def build_states_dictionaries(states_raw_list):
    states = []
    for state_string in states_raw_list:
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
        print(f"We found a row for the state {state_name}. It has population {state_population}.")

    print(f"We created {len(states)} dictionaries.")
    return states

# This function takes as input a list of states, each of which is a dictionary with two keys: "name" and "population"
# The code answers the following question: What is the sum of the populations of the first five states in the list?
# When the list is sorted, this produces the sum of the largest five states.
# The result is printed to the terminal.
def sum_of_top_five(states):
    sum_so_far = 0
    for this_state in states[0:5]:
        this_state_population = this_state["population"]
        sum_so_far += this_state_population
    print(f"The sum of the top five states' populations is {sum_so_far}")

# This function takes as input a list of states, each of which is a dictionary with two keys: "name" and "population"
# The code counts how many states have over ten million people in their population.
# The result is printed to the terminal.
def states_over_ten_million(states):
    states_over_ten_million_count = 0
    states_names_over_ten_million = []
    for state in states:
        state_population = state["population"]
        if state_population > 10000000:
            states_over_ten_million_count += 1

            states_names_over_ten_million.append(state["name"])

    for qualifying_state in states_names_over_ten_million:
        print(qualifying_state)

# Now that we've defined our functions, the code below runs when we run this program.

# First, we load the contents of the state sizes CSV and save each row to a list.
state_rows = []
with open("state_sizes.csv") as states_file:
    for row in states_file.readlines():
        row_text = row.strip()
        state_rows.append(row_text)
# This is just a test to see if the contents were loaded properly.
print(state_rows[0])

# Next, we convert the rows of the input file to a dictionary that we can use in future code.
states = build_states_dictionaries(state_rows)
first_state_name = states[4]["name"]
print(f"The fifth state in our dictionary is {first_state_name}")


# With the dictionary that we can built, we can call any number of functions that evaluate its contents.
sum_of_top_five(states)
states_over_ten_million(states)
