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

# This function is slightly more sophisticated and instead has a set of different
# types of food that might be mentioned in a review. It attempts to match each pattern
# and returns the name of the cuisine type mentioned most often in a review.
def cuisine_type(review):
    patterns = {
        "american":"(burger|fries)",
        "italian":"(pizza|pasta)",
        "mexican":"(taco|burrito|quesadilla)"
    }
    max_cuisine = "unknown"
    max_cuisine_count = 0
    for cuisine in patterns:
        pattern = re.compile(patterns[cuisine])
        mentions = re.findall(pattern, review)
        count_mentions = len(mentions)
        if count_mentions > max_cuisine_count:
            max_cuisine_count = count_mentions
            max_cuisine = cuisine
    return max_cuisine

# This function should define a way to test whether a given review text is
# positive or negative, using the tools from regular expressionso that we've
# learned up until this point.
def review_sentiment(review):
    positive_words = "(good|great|amazing|delicious|fabulous)"
    negative_words = "(bad|terrible|disgusting|gross|rude)"

    # With the not prefix, we got a breakdown of:
    # 871 negative reviews
    # 12,807 positive reviews
    #
    # What does this filter out? 594 false positives and 200 false negatives
    not_prefix = "[^(not)]\s"
    positive_pattern = re.compile(f"{not_prefix}{positive_words}")
    negative_pattern = re.compile(f"{not_prefix}{negative_words}")

    positive_mentions = re.findall(positive_pattern, review)
    negative_mentions = re.findall(negative_pattern, review)

    if len(positive_mentions) > len(negative_mentions):
        return "Positive"
    elif len(negative_mentions) > len(positive_mentions):
        return "Negative"
    else:
        return "Unknown"

