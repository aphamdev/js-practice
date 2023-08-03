# You're given two sorted lists. Your job is to write a
#  function that merges those two sorted lists into one big sorted list.


def merge_sorted_lists(list1, list2):
    for x in list2:
        list1.append(x)
    return sorted(list1)
