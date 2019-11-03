import re
# US phone number format that should be accepted:
# 111-222-3333 (exactly ten digits), separated by dashes
# Area code: 3 digits
# Then three more digits
# Then four more digits
# No restrictions on the numbers inside
#
# This new version also makes several new allowances:
# - You can either use dashes or spaces between the last seven digits
# - You can add parentheses around area codes, optionally
# - x11 numbers is accepted as a valid number
# - International country code (1) is allowed but optional
#
# The following syntax allows us to do that:
# Creating a group of values (a|b), in parentheses separated by a pipe,
# allows *either* a *or* b to appear in that position. 
def complicated_us_phone_number(num):
    parens_pattern = "(1(-|\s))?\(?\d{3}\)?(-|\s)\d{3}(-|\s)\d{4}"
    emergency_pattern = "\d11"
    combined_pattern = f"{parens_pattern}|{emergency_pattern}"
    match = re.search(combined_pattern, num)
    if match:
        return True
    else:
        return False

# This function knows the ordering of groups in a regex and looks specifically for
# the third value captured in parentheses, which we know will be the area code, if
# a full phone number is found at all.
def find_area_code(num):
    # Regular expressions can be written all in one large line.
    parens_pattern = "(1(-|\s))?(\(?\d{3}\)?)(-|\s)(\d{3})(-|\s)(\d{4})"
    
    # Or you can define them piece by piece, then aggregate them together.
    country_code = "(1(-|\s))?"
    area_code = "(\(?\d{3}\)?)(-|\s)"
    phone_number = "(\d{3})(-|\s)(\d{4})"

    emergency_number = "911"

    full_pattern = f"({emergency_number}|{country_code}{area_code}{phone_number})"

    # Either way, you can use .search() to find the first occurrence, or 
    # .findall() to get a list of all the appearances
    match = re.search(parens_pattern, num)
    if match:
        # All the subsections of your regular expression that are grouped
        # in parentheses are "captured" and are available in a list by calling
        # .groups(). If you want to find the area code in the string above, for instance,
        # you can get groups[2].
        groups = match.groups()
        print(groups)
        area_code = groups[2]
        print(area_code)
        return area_code




if __name__ == "__main__":
    test_numbers = ["412-268-2000", "1-412-268-2000", "(412) 268 2000", "911", "999", "14122682000"]
    for number in test_numbers:
        allowed = complicated_us_phone_number(number)
        print(f"{number} is allowed? {allowed}")
        area_code = find_area_code(number)
        print(f"{area_code} is the area code.")
