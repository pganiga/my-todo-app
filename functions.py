
def display_todo(ins):
    for index, items in enumerate(ins):
        items = items.capitalize()
        formatted = f"{index + 1}.{items}"
    # print(index,'.',items)
        print(formatted)


def read_files():
    with open('files/ToDo.txt', 'r') as filer:
        todo_es = filer.readlines()
    return todo_es


def write_file(todo_arg, file_name="ToDo.txt"):
    """This function is to write todo items to todo.txt file"""
    with open('files/' + file_name + '', 'w') as file_w:
        file_w.writelines(todo_arg)
