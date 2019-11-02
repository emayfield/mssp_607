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
    parens_pattern = "(1(-|\s))?\(?(\d{3})\)?(-|\s)(\d{3})(-|\s)(\d{4})"
    match = re.search(parens_pattern, num)
    if match:
        groups = match.groups()
        area_code = groups[2]
        print(area_code)

if __name__ == "__main__":
    test_numbers = ["412-268-2000", "1-412-268-2000", "(412) 268 2000", "911", "999", "14122682000"]
    for number in test_numbers:
        allowed = complicated_us_phone_number(number)
        print(f"{number} is allowed? {allowed}")
        find_area_code(number)