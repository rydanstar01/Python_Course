# Coding Exercise 6.1
# Please download the essay.txt file from the resources of this article. Then, create a program that reads that file and prints out its text. The first letter of each word in the output should be uppercase.

file = open('Coding_exercise_6_files\essay.txt', 'r')
essay = file.read()
file.close()
print(essay.title())
    




# Coding Exercise 6.2
# Write a program that reads the essay.txt file and returns the number of characters contained in the file.

file = open('Coding_exercise_6_files\essay.txt', 'r')
essay = file.read()
file.close()
print(f"The number of characters are: {len(essay)}")



# Coding Exercise 6.3
# Please download the members.txt file from the resources of this article.

# Then, create a program that, whenever executed, asks the user to enter a new member in the command line:
    # Add a new member: Solomon Right

# Then, the member is added to members.txt. In this case, the text file content would be:

# John Smith

# Sen Lakmi

# Sono Octonot

# Solomon Right


file = open("Coding_exercise_6_files\members.txt", "r")
members = file.readlines()
file.close()
member = input("Add a new member: ") + "\n"
members.append(member)
file = open("Coding_exercise_6_files\members.txt", "w")
file.writelines(members)
file.close()



# Coding Exercise 6.4
# Create a program that generates multiple text files by iterating over the filenames list. The text Hello should be written inside each generated text file.

filenames = ['doc.txt', 'mock.txt', 'rock.txt']
content = 'Hello'

for filename in filenames:
    file = open(f"Coding_exercise_6_files\{filename}", "w")
    file.write(content)
    file.close()



# Coding Exercise 6.5
# Please download the three text files a.txt, b.txt, and c.txt from the resources. Then, create a program that reads each text file and prints out the content of each in the command line. The expected output would be like the following:
    # I am a.
    # I am b.
    # I am c.

filenames = ['a.txt', 'b.txt', 'c.txt']
for filename in filenames:
    file = open(f"Coding_exercise_6_files/{filename}", "r")
    display = file.read()
    file.close()
    print(display)





# Resources for this lecture
# essay.txt
# members.txt
# a.txt
# b.txt
# c.txt