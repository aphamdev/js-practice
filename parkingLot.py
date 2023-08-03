# Given two strings of up to 100 characters each, yesterday and today,
# complete the function num_same_spaces to return the number of parking
#  spaces that were occupied both yesterday and today.

# Constraints:

# 1 <= len(yesterday) <= 100
# len(yesterday) == len(today)
# Example:

# Here are two strings that you need to compare. Underneath the two strings are stars that show where the same parking space was filled on both mornings


def num_same_spaces(yesterday, today):
    total_spaces_filled = 0
    for i in range(len(yesterday)):
        if yesterday[i] == today[i] and today[i] == "C":
            total_spaces_filled += 1
    return total_spaces_filled
