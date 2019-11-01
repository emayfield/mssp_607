
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
           
def q6_pandas(districts_df, states_df):
    print("Pandas: Not implemented yet")
    pass


import pandas as pd

from build_districts import build_districts_list_csv
from build_states import build_states_csv


if __name__ == "__main__":
    filename = "district_statistics.csv"
    districts_df = pd.read_csv(filename)
    districts_list = build_districts_list_csv(filename)

    states_filename = "state_sizes.csv"
    states_df = pd.read_csv(states_filename)
    state_populations = build_states_csv(states_filename)

    q6_smallest_mean_district_size(districts_list, state_populations)
    q6_pandas(districts_df, states_df)
