import re

# US phone number format that should be accepted:
# 111-222-3333 (exactly ten digits), separated by dashes
# Area code: 3 digits
# Then three more digits
# Then four more digits
# No restrictions on the numbers inside
def us_phone_number(num):
    us_pattern = "\d{3}-\d{3}-\d{4}"
    us_pattern = "\d\d\d-\d\d\d-\d\d\d\d"


    # (412) 268-2000
    us_pattern_complex = "\(\d{3}\) \d{3}-\d{4}"


    # \d? means exactly zero or one times that a digit appears
    # \d+ means at least one time, or more in a row
    # \d* optional, can be zero, or can be any number of digits

    us_pattern_options = f"(\+?1 )?({us_pattern}|{us_pattern_complex})"

    us_regex = re.compile(us_pattern_options)
    us_exists = re.search(us_regex, num)

    us_exists_findall = re.findall(us_regex, num)
    print(us_exists_findall)


    return us_exists

# UK phone number format that should be accepted:
# 011 222 3333, separated by *spaces*
# Area code: Starts with 0, then from two to five more digits
# Then up to seven more digits
def uk_phone_number(num):
    uk_pattern_simple = "0\d{2,5} \d{4,7}"
    uk_pattern_complex = "0\d{2,5} (\d{4,7}|\d{3}\s\d{4})"

    uk_regex = re.compile(uk_pattern_complex)
    uk_exists = re.search(uk_regex, num)
    return uk_exists

def find_country(num):
    if us_phone_number(num):
        return "US"
    elif uk_phone_number(num):
        return "UK"
    else:
        return "Unknown"

if __name__ == "__main__":
    test_numbers = ["215-898-5000", "412-268-2000", "011865 2700000",
                    "011 666 6555", "1555 5555555", "(412) 268-2000",
                    "+1 412-268-2000", "+1 (412) 268-2000",
                    "+55 412-268-2000"]
    for number in test_numbers:
        country_name = find_country(number)
        print(f"Phone number {number} is from the following country: {country_name}")