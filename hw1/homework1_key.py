# This function takes one object as input:
#   populations_file: A filename where the file contains a spreadsheet with
#                     exactly two columns: name in column 0, population in column 1
# 
# This function returns a dictionary as output:
#   states: Each key in this dictionary is a state name.
#           The value is the population for that state, as found in the data file. 
# 
def build_state_populations_dictionary(populations_file):
    states = {}
    with open(populations_file) as states_file:
        states_input = states_file.readlines()
        header_row = []
        i = 0
        for row in states_input:
            if i == 0:
                header_row = row.split(",")
            else:
                state_row = row.split(",")
                state_name = state_row[0].strip()
                state_population = int(state_row[1].strip())
                states[state_name] = state_population
            i += 1
    return states
    
# This function takes one object as input:
#   districts_filename: A filename where the file contains a spreadsheet with
#                       any number of columns.
#
# This header column is then followed by any number of rows. The function
# attempts to convert the values to integers, or defaults to strings if it cannot.
#
# This function returns a list as output:
#   districts_list: Each entry in this list is a dictionary representing
#                   a single school district from our input file. Each dictionary
#                   contains keys corresponding to the columns in the input file. 
#                   That means you can retrieve, for instance, the 
#                   total revenue of the first school district in the list:
# 
#                           districts_list[0]["revenue"]
# 
def build_districts_list(districts_filename):
    districts_list = []
    with open(districts_filename) as districts_file:
        districts_input = districts_file.readlines()
        row_number = 0
        header_row = []
        for row in districts_input:
            if row_number == 0:
                header_row = row.strip().split(",")
            else:
                district_row = row.split(",")
                district_facts = {}
                for column_number in range(len(district_row)):
                    column_name = header_row[column_number]
                    cell_value = district_row[column_number]
                    try:
                        cell_value = int(cell_value)
                    except ValueError:
                        pass
                    district_facts[column_name] = cell_value
                districts_list.append(district_facts)
            row_number += 1
    return districts_list

# This function takes as input a list of school districts, and prints 
# an answer to the question: what percentage of those districts receive 
# over $10 million in local revenue? Units are in thousands.
#
# The answer in this dataset is 30.30%, or 5087 districts.
#
# This function does not return any value.
def q1_ten_million(districts_list):
    ten_million_districts = 0
    for district in districts_list:
        local_revenue = district["local_revenue"]
        if local_revenue > 10000:
            ten_million_districts += 1
    percentage = 100*ten_million_districts / len(districts_list)
    print(f"Q1: {ten_million_districts} districts, {percentage}%, with at least ten million in local funding.")

# This function takes as input a list of school districts, and prints
# the shortest name among all districts with at least $1 billion budgets,
# along with the state where the district is located.
#
# The answer in this dataset is DADE, which is actually the Miami-Dade countywide district.
# It is located in Florida.
# 
# This function does not return any value.
def q2_shortest_billion_name(districts_list):
    shortest_name_length = 9999 # Placeholder value - all school district names are shorter than this.
    shortest_name = None
    shortest_state = None
    for district in districts_list:
        expenses = district["expenses"]
        if expenses > 1000000:
            name = district["name"]
            length = len(name)
            if length < shortest_name_length:
                shortest_name_length = length
                shortest_name = name
                shortest_state = district["state"]
    print(f"Q2: Shortest name is {shortest_name} (length {shortest_name_length}) in state {shortest_state}")

# This function takes as input a list of school districts, and prints a count of
# how many of those districts have greater budgets than Hawaii does statewide.
# 
# The answer in this case is 8.
#
# This function does not return any value.
def q3_larger_than_hawaii(districts_list):
    hawaii_budget = None
    for district in districts_list:
        if district["state"] == "Hawaii":
            hawaii_budget = district["expenses"]
    larger_than_hawaii = 0
    if hawaii_budget:
        for district in districts_list:
            if district["state"] != "Hawaii" and district["expenses"] > hawaii_budget:
                larger_than_hawaii += 1
    print(f"Q3: {larger_than_hawaii} districts with larger budgets than Hawaii.")

# This function takes as input a list of school districts, and prints the name of the 
# school district in Pennslyvania with the largest budget deficit in 2014, along with the
# size of that deficit.
#
# The answer is PENN HILLS SD (with a deficit of just under $33 million)
#
# This function does not return any value.
def q4_biggest_pennsylvania_deficit(districts_list):
    largest_deficit = 0
    largest_deficit_name = None
    for district in districts_list:
        if district["state"] == "Pennsylvania":
            expenses = district["expenses"]
            revenue = district["revenue"]
            deficit = expenses - revenue
            if deficit > largest_deficit:
                largest_deficit_name = district["name"]
                largest_deficit = deficit
    print(f"Q4: Largest budget deficit in Pennsylvania is {largest_deficit}, name is {largest_deficit_name}")

# This function takes as input a list of districts and a list of statewide populations,
# and calculates the per-capita spending of the six states in New England, then prints
# the name of the state in that region with the highest spending.
#
# The answer is Conecticut, with per-capita spending of $2.91, though Vermont is lower by less
# than $0.01 per capita, if we look at the data directly.
#
# This function does not return any value.
def q5_new_england_highest_per_capita(districts_list, state_populations):
    per_capita_highest = 0
    highest_state_name = None
    new_england = ["Maine", "Vermont", "New Hampshire", "Rhode Island", "Connecticut", "Massachusetts"]
    for state in new_england:
        state_total = 0
        population = state_populations[state]
        for district in districts_list:
            if district["state"] == state:
                state_revenue = district["state_revenue"]
                local_revenue = district["local_revenue"]
                state_total += (state_revenue + local_revenue)
        state_per_capita = state_total / population
        if state_per_capita > per_capita_highest:
            per_capita_highest = state_per_capita
            highest_state_name = state
    print(f"Q5: Most per-capita spending was {highest_state_name} with per capita spending of {per_capita_highest}.")

# This function takes as input a list of districts and a list of statewide populations,
# then calculates and prints which state has the smallest mean district size, by population count.
#
# The answer is Vermont, with only 1,955 residents per school district (though this number turns out
# to be slightly inaccurate as some of the districts are administrative-only).
#
# This function does not return any value.
def q6_smallest_mean_district_size(districts_list, state_populations):
    state_counts = {}
    for district_facts in districts_list:
        state = district_facts["state"]
        if state in state_counts:
            state_counts[state] = state_counts[state] + 1
        else:
            state_counts[state] = 1
    smallest_mean = 9999999 # Placeholder value - all school district mean sizes are less than this.
    state_with_smallest_mean = None
    for state in state_counts:
        pop = state_populations[state]
        mean = pop / state_counts[state]
        if mean < smallest_mean:
            state_with_smallest_mean = state
            smallest_mean = mean
    print(f"Q6: Smallest mean is {round(smallest_mean)} in {state_with_smallest_mean}")
           
state_populations = build_state_populations_dictionary("state_sizes.csv")
districts_list = build_districts_list("district_statistics.csv")

q1_ten_million(districts_list)
q2_shortest_billion_name(districts_list)
q3_larger_than_hawaii(districts_list)
q4_biggest_pennsylvania_deficit(districts_list)
q5_new_england_highest_per_capita(districts_list, state_populations)
q6_smallest_mean_district_size(districts_list, state_populations)