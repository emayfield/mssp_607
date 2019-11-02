from intro_yelp import fetch_yelp
import re
import pandas as pd

# This function takes as input a single review text.
# It checks for indicators of an "American" restaurant with a regular expression
def is_american_restaurant(review):
    american_menu_string = "(burger|fries)"
    american_menu_pattern = re.compile(american_menu_string)
    menu_mentions = re.findall(american_menu_pattern, review)
    matches_exist = len(menu_mentions) > 0
    return matches_exist
    
# This function is slightly moore sophisticated and instead has a set of different
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
        pattern = re.compile(cuisine)
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
    return "Unknown"


if __name__ == "__main__":
    takeout_filename = "PA_takeout_reviews.json"
    takeout = fetch_yelp(takeout_filename)
    takeout["is_american"] = takeout.loc[:, "text"].apply(is_american_restaurant)
    takeout["sentiment"] = takeout.loc[:, "text"].apply(review_sentiment)
    sentiment_groups = takeout.groupby("sentiment").mean()
    print(sentiment_groups.head)

    takeout["cuisine"] = takeout.loc[:, "text"].apply(cuisine_type)
    cuisine_groups = takeout.groupby("cuisine").count().iloc[:, :1]
    print(cuisine_groups.head)