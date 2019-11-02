# For this section of the class we're going to use the re library,
# which is part of the Python standard library.
import re

def check_american_zip(code):
    # First, make sure the code to test is in string format, so even
    # if we receive a number to test, it'll work.
    code = str(code)

    # Regular expression patterns are defined as strings. 
    # Some common strings to search for include:
    # \d is any number character, 0-9
    # \w is any alphabetical character, A-Z, uppercase or lowercase
    # \s is any space character, including tabs or spaces or other blanks.
    #
    # The following pattern looks for any series of five digits in a row.
    zip_pattern = "\d\d\d\d\d"

    # When we want to create a regular expression pattern we call the re.compile()
    # function, which takes as input a string and returns an object matching
    # the pattern that the string represents.
    zip_regex = re.compile(zip_pattern)

    # To test whether a pattern matches a string at least once, we call .search()
    zip_exists = re.search(zip_regex, code)

    return zip_exists
    
    # .search() - find the first occurrence
    # .findall() - find all occurrences
    # 

def check_uk_post(code):
    # UK post codes are in the format:
    # - one or two letters
    # - one or two numbers
    # - optionally, a space
    # - one number
    # - two letters
    #
    # If you know exactly how many are supposed to show up, you can
    # give the acceptable range with curly braces {x,y}
    post_pattern = "\w{1,2}\d{1,2}\s?\d\w\w?"

    # This pattern is identical because it uses a quantifier:
    # * zero or more of the previous character
    # + one or more of the previous character
    # ? exactly zero or one of the previous character
    post_pattern = "\w\w?\d\d?\s?\d\w\w?"

    post_regex = re.compile(post_pattern)
    post_exists = re.search(post_regex, code)
    return post_exists


if __name__ == "__main__":
    test_strings = ["19104", "25255", "A99 9ZZ", "Pennsylvania"]
    for code in test_strings:
        us = check_american_zip(code)
        uk = check_uk_post(code)
        if us:
            print(f"US ZIP code: {code}")
        elif uk:
            print(f"UK postcode: {code}")
        else:
            print(f"Not a known format: {code}")