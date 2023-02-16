# Coding Exercise 11.1
# The code below is incomplete. It should calculate and print out the maximum value of the grades list. Please complete the function and then call it.

# def get_max():
#     grades = [9.6, 9.2, 9.7]
# The output of your code should be:
# 9.7

# Hint: You can use the max(list) function to find the maximal value of a list.
# Solution

def get_max():
    grades = [9.6, 9.2, 9.7]
    max_value = max(grades)
    return max_value

print(get_max())




# Coding Exercise 11.2
# The function we wrote in exercise 1 returned 9.7.  Change the function so this time it returns Max: 9.7, Min: 9.2 where 9.7 is the maximum and 9.2 is the minimum.

# Solution


def get_max():
    grades = [9.6, 9.2, 9.7]
    max_value_local = max(grades)
    return max_value_local

def get_min():
    grades = [9.6, 9.2, 9.7]
    min_value_local = min(grades)
    return min_value_local

max_value = get_max()
min_value = get_min()

print(f"Max: {max_value}, Min: {min_value}")