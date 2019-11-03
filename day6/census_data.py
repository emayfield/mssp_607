import requests
import pandas as pd
from intro_requests import lookup_state

# Now we can open the floodgates! We can look up the different parameters we're 
# interested in at the following website, and get arbitrary data.

# We can now write a reusable clean function for looking up state-level data from the Census.
#
# This function takes two parameters as input:
# variable_code: Lookup string from the Census. Definitions are here:
#                https://api.census.gov/data/2018/acs/acs1/variables.html
# my_key: Authentication key from the census. Get yours here:
#         https://api.census.gov/data/key_signup.html
#
# This function returns a Pandas dataframe with the state-level data for the variable you provided.
def query_survey(variable_code, my_key):
    # This endpoint will always look up statistics from the 2018 Community Survey
    endpoint = "https://api.census.gov/data/2018/acs/acs1"
    
    # This matches the parameters we used earlier, but uses the variable code from the query.
    parameters = {
        "get":variable_code,
        "for":"state:*",
        "key":my_key
    }
    detailed_data = requests.get(endpoint, params=parameters)
    response_df = None
    if detailed_data.status_code == 200:
        response_df = pd.read_json(detailed_data.content)
        # The response that the government gives us is just a big long array, and we need
        # to tell Pandas that the first row is actually headers for the columns.
        response_df.columns = response_df.iloc[0]
        response_df = response_df[1:].reset_index()
    return response_df

if __name__ == "__main__":
    geocodes = pd.read_csv("geocodes.csv", dtype=str)
    my_key = open("day6/key.txt").read()
    
    total_variable = "B01003_001E"
    # Start with target population. Here are a couple:
    # B01001_002E Male
    #
    # Here's one that we'll try later, but with missing data:
    # B03001_003E Hispanic or Latino identifying
    target_variable = "B01001_002E"


    population_df = query_survey(total_variable, my_key)
    target_df = query_survey(target_variable, my_key)

    # We previously merged one column at a time using .join(). If we want to merge together
    # two entire dataframes, it is often easier to use .merge() instead.
    merged_df = population_df.merge(target_df, on="state")

    # Here we can give names to the variables we're interested in.
    merged_df["population"] = pd.to_numeric(merged_df[total_variable])
    merged_df["target"] = pd.to_numeric(merged_df[target_variable])
    merged_df["state_name"] = merged_df.state.apply(lambda x: lookup_state(geocodes, x))
    merged_df["target_pct"] = merged_df.target / merged_df.population

    # We can look in the terminal to find out what our variables look like.
    for state in merged_df.state.unique():
        state_name = lookup_state(geocodes, state)
        target_percent = 100*merged_df.loc[merged_df.state == state].iloc[0]["target_pct"]
        print(f"{state_name} has {target_percent:.2f}% identified target population")

    # And finally we can export our results to a new file.
    with open("state_values.csv", "w") as out_file:
        output = merged_df.loc[:, ["state_name", "target_pct"]].to_csv()
        out_file.write(output)

