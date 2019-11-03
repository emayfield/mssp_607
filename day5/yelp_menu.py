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

    # 1071 negative
    # 13,401 positive
#    positive_pattern = re.compile(positive_words)
#    negative_pattern = re.compile(negative_words)


    positive_mentions = re.findall(positive_pattern, review)
    negative_mentions = re.findall(negative_pattern, review)

    if len(positive_mentions) > len(negative_mentions):
        return "Positive"
    elif len(negative_mentions) > len(positive_mentions):
        return "Negative"
    else:
        return "Unknown"



if __name__ == "__main__":
    takeout_filename = "PA_takeout_reviews.json"
    takeout = fetch_yelp(takeout_filename)
    takeout["sentiment"] = takeout.loc[:, "text"].apply(review_sentiment)
    sentiment_groups = takeout.groupby("sentiment").size()
    print(sentiment_groups.head)

    takeout["cuisine"] = takeout.loc[:, "text"].apply(cuisine_type)
    cuisine_groups = takeout.groupby("cuisine").size()
    print(cuisine_groups)
