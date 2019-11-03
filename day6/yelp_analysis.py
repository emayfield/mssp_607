from yelp_functions import fetch_yelp, review_sentiment, cuisine_type

# This function takes as input a dataframe of Yelp reviews and a column name.
# For each possible value in that column, it prints to the terminal the average
# star counts for reviews that contain the specified value in that column.
#
# This function does not return any values.
def print_mean_stars_by_column(df, col):
    group_means = df.groupby(col).mean()
    print("Group average star counts:") 
    for group in group_means.index.unique():
        mean_stars = group_means.loc[group, "stars"]
        print(f"   {group}: {mean_stars:.2f}")

# This function takes as input a dataframe of Yelp reviews and a column name.
# For each possible value in that column, we generate aggregate statistics
# including size of the subgroup and mean star count of that subgroup.
#
# The resulting statistics are output to a new file, specified by the format
# parameter. Possible formats are: "json" and "csv".
#
# This function does not return any values.
def export_star_statistics(df, col, format):
    subgroup_stars = df.groupby(col)["stars"]
    subgroup_statistics = subgroup_stars.agg(["size", "mean"])

    with open(f"subgroups_{col}.{format}", "w") as out_file:
        if format == "csv":
            out_file.write(subgroup_statistics.to_csv())
        elif format == "json":
            out_file.write(subgroup_statistics.to_json())


if __name__ == "__main__":
    takeout_filename = "PA_takeout_reviews.json"
    takeout = fetch_yelp(takeout_filename)

    # Simple automated definition yesterday in yelp_menu.py based on a pair of 
    # regexes, assigns "Positive", "Negative", or "Unknown"
    takeout["sentiment"] = takeout.loc[:, "text"].apply(review_sentiment)

    # Simple automated definition yesterday in yelp_menu.py based on dictionary 
    # of regexes, assigns "italian", "mexican", "american", or "other"
    takeout["cuisine"] = takeout.loc[:, "text"].apply(cuisine_type)

    # Using the function defined above we can now get review averages for any
    # given column of our dataframe.
    print_mean_stars_by_column(takeout, "sentiment")
    print_mean_stars_by_column(takeout, "cuisine")

    # We could alternatively write a very similar function that exports the data
    # to a file for future use or sharing, instead of printing it to the terminal.
    export_star_statistics(takeout, "sentiment", "csv")
    export_star_statistics(takeout, "sentiment", "json")
    