from functions import get_todos, write_todos
import time

while True:
    now = time.strftime("%b %d, %Y %H:%M:%S")
    print("It is", now)
    
    # Get user input and strip the space characters from it
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    
        # Add a todo 
    if user_action.startswith('add'):
        todo = user_action[4:] 
        
        # Open and read the file. Store the contents as a list using readlines
        todos = get_todos()

        # Append contents to the list
        todos.append(todo + "\n")

        # Open and write the file. Write the contents of the list using writelines in the file
        write_todos(todos)

    # Display the todos
    elif user_action.startswith('show'):

        todos = get_todos()

        # Using List Comprehensions
        # new_todos = [item.strip('\n') for item in todos]

        # Show the items of the list with index. Capitalize the string and also strip '\n' from each item
        for index, item in enumerate(todos):
            item = item.strip('\n').title()
            print(f"{index + 1}-{item}")

    # Edit the contents of the todo
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:]) - 1

            todos = get_todos()

            new_todo = input("Enter the new todo: ")
            todos[number] = new_todo

            write_todos(todos)
            print(todos[number])

        except ValueError:
            print("Your command is not valid.")
            continue

    # Delete the todo
    elif user_action.startswith('complete'):
        try:
            del_number = int(user_action[8:]) - 1
            
            todos = get_todos()
            
            todo_to_remove = todos[del_number].strip('\n')

            # pop method is used to delete an item using the index
            todos.pop(del_number)

            write_todos(todos)

            message = f"TODO: {todo_to_remove} was removed from the list"
            print(message)
        
        except IndexError:
            print("Your command is not valid.")
            continue

    # Stop the program
    elif user_action.startswith('exit'):
        break
    
    else:
        print("Command not valid.")
        break


print('Bye!')