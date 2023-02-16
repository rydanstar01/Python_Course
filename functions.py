FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Read a text file and gets the list of to-do items.
    """
    with open(filepath, 'r') as file_local:
            todos_local  = file_local.readlines()
    return todos_local

# help(get_todos)

def write_todos( todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in a text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

# help(write_todos)