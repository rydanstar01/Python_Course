# Coding Exercise 2.1
# Create a program that prompts the user to input their name once. Then, the program prints out the name once with the first letter capitalized.

name = ''
while len(name) == 0:
    name = input("Enter your name: ")
    print("Name entered is: ", name.title())

# Coding Exercise 2.2
# Create a program that prompts the user to input their name once. Then, the program repeatedly prints out the name with the first letter capitalized.

name = input("Enter your name: ")
while True:
    print(name.title())

# Coding Exercise 2.3
# Create a program that prompts the user to input their name repeatedly. Then, the program repeatedly prints out the name with the first letter capitalized.

while True:
    name = input("Enter your name: ")
    print(name.capitalize())

