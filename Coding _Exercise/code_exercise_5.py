# Coding Exercise 5.1
# filenames = ['document', 'report', 'presentation']

# Copy-paste the above list in a .py file and extend the code, so it prints out the output below:

# 0-Document.txt
# 1-Report.txt
# 2-Presentation.txt

filenames = ['document', 'report', 'presentation']
for index, item in enumerate(filenames):
    result = f"{index}-{item.capitalize()}.txt"
    print(result)



# Coding Exercise 5.2
# ips = ['100.122.133.105', '100.122.133.111']

# Copy-paste the ips list in a .py file and extend the program so it:

# 1. Prompts the user to input an index (e.g, 0 or 1).

# 2. Returns the IP address that has that index.

# Here is how the program would behave when executed:
# Enter the index of the IP you want: 1
# You chose 100.122.133.111

ips = ['100.122.133.105', '100.122.133.111']
prompt = int(input("Enter the index of the IP you want: ")) - 1
print(f"You chose {ips[prompt]}")


