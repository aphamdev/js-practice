# Please complete the following function that takes a list of dictionaries and a key. The function should return
# a list of the same length as the input. For each position in the returned list,
#  it should have a True value if the corresponding dictionary value in the input list
#   has the indicated key. Otherwise, the position in the list should have False.




def key_in_dict(list_of_dicts, key):
    return [key in d for d in list_of_dicts]
