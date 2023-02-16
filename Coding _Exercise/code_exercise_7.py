# Coding Exercise 7.1
# names = ["john smith", "jay santi", "eva kuki"]

# Extend the code above so the code capitalizes all the names and the surnames of the list and then prints the new list.

# The output of your code should be as below:

# ['John Smith', 'Jay Santi', 'Eva Kuki']
# Solution

names = ["john smith", "jay santi", "eva kuki"]

names = [name.title() for name in names]
print(names)



# Coding Exercise 7.2
# usernames = ["john 1990", "alberta1970", "magnola2000"]

# Extend the code above so the code prints out a list containing the number of characters for each username.

# The output of your code should be as below:

# [9, 11, 11]
# Solution

usernames = ["john 1990", "alberta1970", "magnola2000"]

len_username = [len(username) for username in usernames]
print(len_username)

# Coding Exercise 7.3
# user_entries = ['10', '19.1', '20']
# Extend the code above so the code prints out a list containing the same items as floats.

# The output of your code should be as below:

# [10.0, 19.1, 20.0]
# Solution

user_entries = ['10', '19.1', '20']

user_entries = [float(user_entry) for user_entry in user_entries]
print(user_entries)

# Coding Exercise 7.4
# user_entries = ['10', '19.1', '20']
# Extend the code above so the code prints out the sum of the numbers.

# The output of your code should be as below:

# 49.1
# Hint: Use the sum() function. The function gets a list of numbers as input and produces the sum of all numbers. For more info, try help(sum).

# Solution

user_entries = ['10', '19.1', '20']

new_entries = [ float(user_entry) for user_entry in user_entries]
print(sum(new_entries))
