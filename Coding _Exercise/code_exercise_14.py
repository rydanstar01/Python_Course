# Coding Exercise 14.1
# Create a function that finds out the state of water (i.e., gas, liquid, solid) given the temperature. In other words, the function has a temperature parameter and returns either "Gas", "Liquid" or "Solid" as a string depending on the temperature. The function should be written in a separate file from the command line interface file. The output should look like in the screenshot below:
# Enter water temperature: -12
# Solid


# Let's run it one more time. Here is another example:
# Enter water temperature: 100
# Gas

# Note: To check if a value is between two values, you can use elif 0 < x < 100:

# Solution
from Coding_exercise_14_files.check_state import check_state

temp = float(input("Enter water temperatue: "))
check_state(temp)

# Coding Exercise 14.2
# In coding exercise 1, we hardcoded the values 0 and 100. It is better to change them to constants in the script where the function is defined. Therefore, your task is to modify the script from exercise 1 by creating two global variables/constants in that file, one variable associated with 0 and another associated with 100. Then, use those variables in the function instead of the values.

# Solution

# Refer check_state.py. We have created solid, gas as 2 global variables