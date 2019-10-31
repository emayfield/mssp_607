# Yesterday we wrote the following function that finds objects
# that exist in both of two lists
def find_overlap(list_a, list_b):
    overlap_list = []
    for item in list_a:
        if item in list_b:
            overlap_list.append(item)
 
    print(overlap_list)
    return overlap_list

# Now write a new function that contains all the objects in both lists
# but does not contain duplicates.
def merge_without_duplicates(list_a, list_b):
    
    # These two variables now point to the same object.
    # Changes to combined_list will also affect list_a.
    combined_list = list_a

    # This creates a duplicate copy of the contents of list_a.
    # If you change combined_list, it will not affect list_a.
    combined_list = list_a.copy()
    
    # This does the same duplication as the .copy() method above.
    combined_list = []
    for i in list_a:
        combined_list.append(i)

    for i in list_b:
        if i not in list_a:
            combined_list.append(i)
    return combined_list



animals = ["lions", "tigers", "bears", "cubs"]
teams = ["phillies", "eagles", "flyers", "sixers", "cubs"]


combined_list = merge_without_duplicates(animals, teams)

print(f"The combined list is {combined_list}")
print(f"The animals list is {animals}")