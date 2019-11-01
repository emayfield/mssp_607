
# Using the from ___ import ___ syntax, we can write definitions of functions
# in one file, and then use that function in a different file. One common use for this 
# is to define your functions in one file, then include the series of function calls
# for an analysis in its own file, without being cluttered with definitions.

from build_states import build_states_csv


# Next, we'll move from the built-in libraries like CSV to a much more powerful,
# external library that will do a lot of bookkeeping for us.

import pandas as pd

def build_states_pandas(states_filename):
    states = pd.read_csv(states_filename)
    print(f"We created {len(states)} dictionaries.")
    return states

def describe_districts_with_pandas(df):
    # DataFrames have a convenient .shape attribute that quickly tells us
    # how many rows and columns were imported.
    rows, columns = df.shape
    print(f"Imported data has {rows} rows and {columns} columns.")

    print(f"The first five and last five rows are:")
    # The attribute .head quickly gives us a human-readable view of what is in the
    # file and 
    print(df.head)

def access_data_in_pandas_traditional(df):
    # Pandas allows you to make use of the standard Python syntax for 
    # dictionaries and lists, if you want to. The only key difference here is that
    # in Python you would write the row number first, then the column, if you had a
    # list of dictionaries. But in Pandas, you look up the column name first,
    # then the row number that you're interested in.

    # This code, for instance, will give you all of the values of the "name" column.
    print(df["name"])

    # We can then get the value of "name" for the first row
    print(df["name"][0])


def access_data_in_pandas_idiomatic(df):
    # The more optimized version of this code, though, is based on the .loc
    # attribute of dataframes. This has unique syntax but you can get used to it.
    # You give the row, then column number, separated by commas, in square brackets.
    # This syntax goes back to the Python standard of rows first, then columns.
    print(df.loc[0, 'name'])

    # To get all of the contents of a single row in pandas by row or column number, 
    # we use the .iloc attribute, and we use similar syntax to lists.

    # This, for instance, gets us the entire first row of the dataframe.
    # In fact, it's a little more convenient, since Pandas knows how to format the code
    # nicely for human consumption on the command line.
    print(df.iloc[0])

    # These tools can be combined to carve your data in interesting ways with 
    # the colon operator (:). For instance, we can get the first two columns of the 
    # three rows and first two columns of a dataset very easily:
    print(df.iloc[:3, :2])

    # If we leave the colon blank, it operates the same as a for loop, giving us each value.
    # We can use either iloc to slice data by numeric index, or loc to get the same subsets
    # using the name of the columns. The two lines below do the exact same thing:
    print(df.iloc[:, 1])
    print(df.loc[:, "state"])

    # If you want to grab multiple columns but they aren't necessarily adjacent, loc is more effective,
    # because you can pass in a list of all the columns you want to aggregate.
    print(df.loc[:, ['name', 'expenses']])

# Another key feature of .loc is that we can instead search for specific tests, and get just the
# rows that match the test we're evaluating.
def finding_subsets(df):
    original_rows, original_cols = df.shape

    # This line, for instance, returns a new dataframe that contains only the rows
    # that match a certain condition.
    over_ten_million = df.loc[df.local_revenue > 10000]
    new_rows, new_cols = over_ten_million.shape
    print(f"Out of {original_rows} rows, {new_rows} had local revenue over $10 million.")

    percent = new_rows / original_rows

    print(f"(that's {percent}%)")
    # Several students found this formatting already, but we can also format
    # numbers in strings to a certain number of significant digits using the 
    # fairly ugly :.f syntax.
    print(f"(that's {percent:.2f}%)")
    print(f"(that's {percent:.4f}%)")
    print(f"(that's {percent:.6f}%)")

if __name__ == "__main__":
    states_filename = "state_sizes.csv"
    build_states_csv(states_filename)

    states_df = build_states_pandas(states_filename)
    districts_df = pd.read_csv("district_statistics.csv")

#    describe_districts_with_pandas(districts_df)
#    access_data_in_pandas_traditional(districts_df)
#    access_data_in_pandas_idiomatic(districts_df)
    finding_subsets(districts_df)