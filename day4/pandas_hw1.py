
from build_districts import build_districts_list_csv
from build_states import build_states_csv
from intro_pandas import build_states_pandas


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

def q2_pandas(df):
    # Initial test to get the subset of districts we're interested in.
    billions = df.loc[df.expenses > 1000000]

    # This is funky syntax that is the equivalent of saying that we want to apply the len() function
    # to every value within the column df["name"]. The resulting new column is then assigned
    # to the key "name_length".
    billions["name_length"] = df["name"].apply(len)

    # .idxmin() gives us the row number with the lowest value for the name_length column.
    min_row_number = billions.name_length.idxmin()
    
    # We can then pass that row number back and find the whole row that contained that minimum,
    # and then print out the name of the district and name of the state.
    minimum_row = billions.iloc[billions.index == min_row_number]
    print(minimum_row.loc[:, ['name', 'state']])


def larger_than_hawaii_hw1(districts_list):
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

def larger_than_hawaii_pandas(df):
    hawaii = df.loc[df.state=="Hawaii"]
    hawaii_expenses = hawaii.iloc[0].expenses
    larger = df.loc[df.expenses > hawaii_expenses]
    print(f"Q3: {len(larger)} districts with larger budgets than Hawaii.")

def new_england_hw1(districts_list, state_populations):
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

def new_england_pandas(districts_df, states_df):
    new_england = ["Maine", "Vermont", "New Hampshire", "Rhode Island", "Connecticut", "Massachusetts"]

    # In addition to having simple boolean operators like >, <, and ==, Pandas has some other methods built-in for you.
    # One of them, .isin(), will find all the rows where the specified column matches any of the values in a list.
    ne_districts_df = districts_df.loc[districts_df.state.isin(new_england)]
    
    # The .groupby() object method on a dataframe gives us an intermediate representation - it's not yet a new data structure,
    # nor is it a dataframe anymore, but is instead a work-in-progress waiting for your next analysis, which will convert it
    # from the original set of rows (thousands of districts) to one row per group label (one per state, in this case).
    ne_by_state = ne_districts_df.groupby('state')

    # This line tells the intermediate object how you want to combine the rows that appear for each group. In this case, we 
    # just want the sum of all the values for state and local revenue. Note that in this particular case, the result is only
    # one column wide, so Pandas returns a Series object, not a DataFrame.
    ne_sums = ne_by_state.state_revenue.sum() + ne_by_state.local_revenue.sum()  
    # The series object, by default, doesn't have a name yet, so we can give it a label. This is equivalent to a new column, now.
    ne_sums = ne_sums.rename("nonfederal_revenue")

    # Next, we need to merge the second file data (population) together with this one. 
    # Let's find all of the state populations that are relevant for the subset of states we're analyzing.
    # We'll reuse the .isin() syntax here.
    ne_populations = states_df.loc[states_df.state.isin(new_england)]

    # This line, now, calls the .join() method on the dataframe, which lets us add in a new column (ne_sums).
    # But this new column might not be in exactly the same order to begin with, so we pass in a new parameter, on,
    # to give Pandas instructions on how to match row to row.
    ne_combined = ne_populations.join(ne_sums, on='state')

    # Within a dataframe, we can use dictionary notation to add in a new column that is calculated based on 
    # data that's already in the rows.
    ne_combined["per_capita"] = ne_combined.nonfederal_revenue / ne_combined.population

    # The .idxmax() function here returns the index value of the row with the highest per-capita value,
    # based on our previous calculation.
    # We could also just call .max() if we only wanted the value and did not need the full row.
    max_row_number = ne_combined.per_capita.idxmax()

    # Now we can find the single row in the dataframe matching that index.
    max_state = ne_combined.iloc[ne_combined.index == max_row_number]

    print(max_state.loc[:, ["state", "per_capita"]])

import pandas as pd

if __name__ == "__main__":
    filename = "district_statistics.csv"
    districts_df = pd.read_csv(filename)
    districts_list = build_districts_list_csv(filename)

    larger_than_hawaii_hw1(districts_list)
    larger_than_hawaii_pandas(districts_df)

    states_filename = "state_sizes.csv"
    states_df = pd.read_csv(states_filename)
    states_list = build_states_csv(states_filename)

    new_england_hw1(districts_list, states_list)
    new_england_pandas(districts_df, states_df)