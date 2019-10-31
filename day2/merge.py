# This function takes two lists as input.
# Creates a new list with only the items that appear in BOTH of the two lists.
# The function returns the list of overlaps as output.
def merge_lists(list_a, list_b):
    merged_list = []
    for item in list_a:
        if item in list_b:
            merged_list.append(item)

    return merged_list
    

animals = ["pigs", "pandas", "cubs"]
sports_teams = ["cubs", "phillies"]
    

animals_and_sports_teams = merge_lists(animals, sports_teams)

print(f"The combined list is {len(animals_and_sports_teams)} items long.")
print(f"The first item in the combined list is {animals_and_sports_teams[0]}")