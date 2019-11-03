import requests
import json
import pandas as pd
from pandas.io.json import json_normalize 

# This is a convenience function that we write for ourselves to look up the actual name
# of a state, given its geocode, by using the lookup table that the government gives us.
def lookup_state(geocodes, state_number):
    matched_rows = geocodes.loc[geocodes.state == state_number].loc[geocodes.county == "000"]
    matched_state = "Unknown"
    if len(matched_rows) > 0:
        matched_state = matched_rows.name.iloc[0]
    return matched_state

if __name__ == "__main__":
    
    # This API endpoint is the base of the Census Bureau's data API. With no
    # authentication at all, it will return a JSON object that's about 18k lines long.
    # This response gives descriptions of every dataset that census.gov makes available
    # to the public for free.
    #
    # The requests library is not part of the standard library. You will need to install
    # it using conda in your environment before the code will run.
    endpoint = "https://api.census.gov/data"
    response = requests.get(endpoint)

    # Status codes tell us whether our request was successful or not. There are many codes,
    # but the basic breakdown is:
    #
    # 1xx - Your request hasn't completed yet
    # 2xx - Your request was successful and the response contains what you asked for.
    # 3xx - Your request was processed successfully, but you haven't gotten your response yet.
    #       (usually because the data has moved to a different location)
    # 4xx - Your request failed and it's probably because you did something wrong.
    #       (most often 403, meaning your access is unauthorized, or 404, meaning you're trying
    #        to access something that doesn't exist)
    # 5xx - Your request failed, but it's probably because there was an error on the server.
    #       (you probably didn't do anything wrong)
    print(response.status_code)

    # The basic content of an HTTP request is returned as a JSON object. This request will be
    # 17k lines long and contain everything in the Census bureau's datasets.
    #
    # We can use the json library, which is part of the Python standard library, to convert
    # the string into dictionaries and lists that we can use in our code.
    print(response.content)
    response_json = json.loads(response.content)
    
    # Using Postman for looking at the json object directly, we can see that "dataset" is the 
    # key that we're going to be most interested in.
    datasets_list = response_json["dataset"]
    print(f"The Census bureau makes {len(datasets_list)} datasets available through an API.")

    # To get your own key, register your own email at the following site:
    #
    # https://api.census.gov/data/key_signup.html
    #
    # Getting a key usually doesn't take more than a minute or two.
    #
    # IMPORTANT: Any information like this that you put into source control
    # is going to be available for everyone to see. You never want to put private
    # information in a place where other users are going to see it.
    # To save information to a file that you do *not* want in your git repository,
    # you can use the "hidden" file .gitignore and list the filename there.
    my_key = open("day6/key.txt").read()
    print(my_key)

    # We start with a base URL that points to the API that will respond to our requests.
    # In this case, we have the 
    endpoint = "https://api.census.gov/data/2018/acs/acs1"

    # Helpfully, the government gives us some examples of specific requests at:
    #
    # https://api.census.gov/data/2018/acs/acs1/examples.html
    # 
    # It gives long confusing URLs like the following:
    # https://api.census.gov/data/2018/acs/acs1?get=B01003_001E&for=state:*&key=YOUR_KEY_GOES_HERE
    #
    # But really, we can split this up into sections based on ? and &. Everything before the ?
    # is the base endpoint that we're sending requests to; everything else is just a dictionary,
    # with each key:value pair separated by ampersands & and using an = sign instead of colons :
    # 
    # So the example above turns into the following dictionary.

    parameters = {
        "get":"B01003_001E",
        "for":"state:*",
        "key":my_key
    }

    # And really, we're going to want to move that example variable out into a separate variable
    # so that we can edit it more easily in the future.
    target_variable = "B01003_001E"
    parameters = {
        "get":target_variable,
        "for":"state:*",
        "key":my_key
    }

    # Now we're ready to send a specific request for a particular set of data!
    detailed_data = requests.get(endpoint, params=parameters)
    
    response_df = None
    if detailed_data.status_code == 200:
        response_df = pd.read_json(detailed_data.content)
        # The response that the government gives us is just a big long array, and we need
        # to tell Pandas that the first row is actually headers for the columns.
        # 
        # By default, Pandas is just creating a bunch of columns with blank names.
        response_df.columns = response_df.iloc[0]
        response_df = response_df[1:].reset_index()

        print(response_df)

    # Well, that's not very helpful, because we don't actually know what the state codes mean.
    # Helpfully, the government gives a glossary, which I've included as a download in geocodes.csv
    #
    # Note that pandas by default will try and transform all of our careful codes into integers, 
    # which is precisely what we don't want, so we need to include a parameter stopping the conversion.
    geocodes = pd.read_csv("geocodes.csv", dtype=str)

    # Sometimes the method you want to apply to a dataframe has more than one parameter, and you
    # want the rest of the parameters to remain the same. For this, we can use lambda functions.
    response_df["state_name"] = response_df.state.apply(lambda x: lookup_state(geocodes, x))


    # Now we finally have all the tools we need for actually making use of the Census API.
    # We can look up the variable codes that the Census uses here:
    #
    # https://api.census.gov/data/2018/acs/acs1/variables.html
    print(response_df.columns)
    response_df["population"] = response_df[target_variable]
    
    # We are now able to see the result of our query by printing it out to the command line.
    print(response_df.loc[:, ["state_name", "population"]])
        
