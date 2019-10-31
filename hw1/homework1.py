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


def q1_ten_million(districts_list):
    pass

def q2_shortest_billion_name(districts_list):
    pass

def q3_larger_than_hawaii(districts_list):
    pass


def q4_biggest_pennsylvania_deficit(districts_list):
    pass

def q5_new_england_highest_per_capita(districts_list, state_populations):
    pass

def q6_smallest_mean_district_size(districts_list, state_populations):
    pass

state_populations = build_state_populations_dictionary("state_sizes.csv")
districts_list = build_districts_list("district_statistics.csv")

q1_ten_million(districts_list)
q2_shortest_billion_name(districts_list)
q3_larger_than_hawaii(districts_list)
q4_biggest_pennsylvania_deficit(districts_list)
q5_new_england_highest_per_capita(districts_list, state_populations)
q6_smallest_mean_district_size(districts_list, state_populations)