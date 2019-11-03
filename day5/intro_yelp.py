import re
import pandas as pd
from pandas.io.json import json_normalize  

# This method is used to convert a large JSON file into a Pandas dataframe.
def fetch_yelp(takeout_file):
    yelp = None
    with open(takeout_file) as in_file:
        raw = pd.read_json(in_file)
        reviews = raw["reviews"]
        yelp = json_normalize(reviews)
        print(yelp.shape)
        print(yelp.columns)
    return yelp

# This method takes as input a whole list of reviews.
# For each review, it prints out which words the user used that were followed
# by an exclamation point.
def find_enthusiasm(reviews):
    pattern = "(\w+)!(!)+"
    exclamations = re.compile(pattern)
    for review in reviews.loc[:, "text"]:
        matches = re.findall(exclamations, review)
        if len(matches) > 0:
            print("-------")
            print(review)
            print("-------")
            print(f"This user was excited about {len(matches)} things: ")
            for match in matches:
                print(f"   {match[0]}")


# This method takes as input a single review text. It calculates 
# how many total times a user ended a sentence in an exclamation point.
# We will use it on a dataframe with the .apply() function.
def measure_enthusiasm(single_review):
    pattern = "(!)+"
    exclamations = re.compile(pattern)
    matches = re.findall(exclamations, single_review)
    return len(matches)

if __name__ == "__main__":
    takeout_filename = "PA_takeout_reviews.json"
    takeout = fetch_yelp(takeout_filename)
    find_enthusiasm(takeout)
    takeout["enthusiasm"] = takeout.text.apply(measure_enthusiasm)
    print(takeout.enthusiasm)
    enthusiasm_max = takeout.iloc[takeout.enthusiasm.idxmax()]
    print(enthusiasm_max.text)