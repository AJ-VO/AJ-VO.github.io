from utils import *

# Python3 code to demonstrate working of
# Append items at beginning of dictionary
# Using update()

# initializing dictionary
test_dict = {"Gfg" : 5, "is" : 3, "best" : 10}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing update dictionary
updict = {"pre1" : 4, "pre2" : 8}

# update() on new dictionary to get desired order
updict.update(test_dict)

# printing result
print("The required dictionary : " + str(updict))
print("END/////////")

with open("jsons/results.json", "r", encoding='utf8') as fp:
    resultDATA = json.load(fp)

match_data = {}
match_data["winner"] = 76
match_data["loser"] = 33

match_data.append(resultDATA)
print(match_data)