import re

# US phone number format that should be accepted:
# 111-222-3333 (exactly ten digits), separated by dashes
# Area code: 3 digits
# Then three more digits
# Then four more digits
# No restrictions on the numbers inside
def us_phone_number(num):
    return False

# UK phone number format that should be accepted:
# 011 222 3333, separated by *spaces*
# Area code: Starts with 0, then from two to five more digits
# Then up to seven more digits
def uk_phone_number(num):
    return False

def find_country(num):
    if us_phone_number(num):
        return "US"
    elif uk_phone_number(num):
        return "UK"
    else:
        return "Unknown"

if __name__ == "__main__":
    test_numbers = ["215-898-5000", "412-268-2000", "011865 270000"]
    for number in test_numbers:
        country_name = find_country(number)
        print(f"Phone number {number} is from the following country: {country_name}")