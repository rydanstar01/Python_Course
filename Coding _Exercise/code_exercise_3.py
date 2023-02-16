# Coding Exercise 3.1
# Create a program that does the following:

# 1. Prompts the user to input the country they are from.

# 2. If the user enters the word USA, the program prints out Hello.

# 3. If the user enters the word  India, the program prints out Namaste.

# 4. If the user enters the word Germany, the program prints out Hallo.

# Note: Strings are case-sensitive in Python, meaning germany and Germany are treated as two different strings.

while True:
    user_prompt = input("Which country are you from: ")
    user_prompt = user_prompt
    match user_prompt:
        case 'Usa' | 'usa':
            print("Hello")
        case 'India' | 'india':
            print("Namaste")
        case "Germany" | 'germany':
            print("Hallo")
        case 'exit':
            break






# Coding Exercise 3.2
# ingredients = ["john smith", "sen plakay", "dora ngacely"]
# Copy-paste the above line into your IDE and write a for-loop below that line that makes the program produce the following output:
# John Smith
# Sen Plakey
# Dora Ngacely
# Tip:  Use the str.title() method to convert strings to Title Case.

ingredients = ["john smith", "sen plakay", "dora ngacely"]
for item in ingredients:
    print(item.title())

