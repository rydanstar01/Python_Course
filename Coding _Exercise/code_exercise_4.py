# Coding Exercise 4.1

# Create a program that:
# 1. Prompts the user to input a (dollar) amount.
# 2. Calculates the corresponding amount in euros, given an exchange rate of 0.95.
# 3. Prints out the amount in euros, as shown in the screenshot below.

# For example
# How many dollars have you got? 100
# The amount in euros is:
# 95.0

dollars = int(input("How many dollars have you got? "))
euros = dollars * 0.95
print(euros)




# Coding Exercise 4.2
# The list below represents the ranking of three athletes. John won 1st place, Sen got 2nd, and Lisa the 3rd.
# ranking = ['John', 'Sen', 'Lisa']

# Create a program that:
# 1. Contains the above list.
# 2. Prompts the user to input a rank number.
# 3. Returns the person who has the given rank.

# For example:
# Enter rank number: 2
# Sen


ranking = ['John', 'Sen', 'Lisa']
rank_name = int(input("Enter rank number: ")) - 1
print(ranking[rank_name])

# Coding Exercise 4.3
# We have the same list:
# ranking = ['John', 'Sen', 'Lisa']

# This time you need to create a program that:
# 1. Contains the above list.
# 2 Prompts the user to input the person's name.
# 3. Returns the rank that person has.

# For example:
# Enter a name: Sen
# 2

ranking = ['John', 'Sen', 'Lisa']
rank_number = input("Ener a name: ")
print(ranking.index(rank_number) + 1)