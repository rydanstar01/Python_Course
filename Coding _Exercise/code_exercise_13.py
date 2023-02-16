# Coding Exercise 13.1
# Define a function that has two parameters, year_of_birth and current_year . The current_year parameter should be a default parameter with the current year as a default value.

# The function should calculate and return the age of the user given the year of birth and the current year.

# Note: It is enough to define the function for this exercise -no need to call it.

# Solution

# def calculate_age(birth_year, current_year=2023 ):
#     age = current_year - birth_year
#     return age



# Coding Exercise 13.2
# Your task for this exercise is to use the function you created in exercise 1. Then, below the function definition, get the year of birth from the user using an input function and then call and print the defined function to get the user's age as output. Here is how the program should behave:

# What is your year of birth? 1902
# 121

# Solution

# birth_year = int(input("What is your year of birth? "))
# age = calculate_age(birth_year)
# print(age)


# Coding Exercise 13.3
# Extend the program you wrote in exercise 2 by printing a message to the user instead of their age if their age is greater than 120. Feel free to print any message that you like.

# Solution

# if age > 120:
#     print("You are above 120")
# else:
#     print("You are below 120")

# Coding Exercise 13.4
# Write a program that gets a list of names from the user and returns the number of names given. You are encouraged to use a function. Here is how the program would work:

# Enter the names separated by commas (no spaces): john,jay,mary
# 3

# Solution

def name_parser(name_list):
    names = name_list.split(",")
    length = len(names)
    return length

name_list = input("Enter the names separated by commas (no spaces): ")
print(name_parser(name_list))