
# This creates a list
teams_list = ["phillies", "sixers"]

# Phillies
# - Play in Philadelphia
# - Play baseball
# - Mascot is "Phanatic"
# - Number of Players: 25

# This is an empty dictionary
phillies = {}

phillies["city"] = "Philadelphia"
phillies["sport"] = "Baseball"


# This creates a dictionary
phillies = {}

# This loops over a range of values
for i in range(10):
    print(i)

# The same syntax can be used to loop over all the keys in a dictionary.
for key in phillies:
    value = phillies[key]
    print(f"We know the value of {key}. It has the value: {value}")


phillies = {
    "sport"      : "Baseball",
    "city"       : "Philadelphia",
    "mascot"     : "Phanatic",
    "num_players": 25,
    "nickname": "Phillies"
}

# This deletes the old value (25) and replaces it with a new value (50).
phillies["num_players"] = 50


yankees = {
    "city": "New York",
    "sport" : "Baseball",
    "num_players": 25,
    "nickname": "Yankees"
}

# Dictionaries can be objects in lists, and you can loop over them in a nested for loop.
teams = [phillies, yankees]
for team in teams:
    nickname = team["nickname"]
    city = team["city"]
    for key in team:
        print(f"      We know the key {key} for team {city}. It is: {team[key]}")
        print("   ---We finished the inner for loop---")
    print("---We finished the outer for loop---")






