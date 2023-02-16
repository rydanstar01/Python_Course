# Coding Exercise 12.1
# Create a function that converts liters to cubic meters knowing that 1000 liters make 1 cubic meter.

# Solution

# def convert(litres):
#     cubic_metres = litres / 1000
#     return cubic_metres

# litres = float(input("Enter litres: "))

# print(f"Cubic meters: {convert(litres)}")


# Coding Exercise 12.2
# Create a script that asks the user to enter a password. Then create a function that checks the strength of the user password. The function should return Strong Password if all of the following conditions are true:

# Eight or more characters

# At least one uppercase letter.

# At least one digit.

# Here is what happens when the user provides a password that satisfies all three conditions:


# And if the user enters a password that breaks one of the three conditions, the program returns Weak Password:


# Note:  You can use the code we developed in the Bonus Example on Day 9.  For your convenience, you can find the code we developed in that video attached to the lecture resources of this article.

# Solution

def password_checker(password):
    result = {}
    if len(password) >= 8:
        result["length"] = True
    else:
        result["length"] = False

    digit = False
    for i in password:
        if i.isdigit():
            digit = True
    result["digits"] = digit

    uppercase = False
    for i in password:
        if i.isupper():
            uppercase = True

    result["upper-case"] = uppercase

    if all(result.values()):
        return "Strong Password"
    else:
        return "Weak Password"


password = input("Enter new password: ")
print(password_checker(password))



# Resources for this lecture
# bonus9.py