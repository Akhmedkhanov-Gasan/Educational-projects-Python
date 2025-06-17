import time

from functions import get_todos, write_todos

print(time.strftime("Date: %b %d, %Y %H:%M:%S"))
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:] 

        todos = get_todos()

        todos.append(todo + "\n")

        write_todos(todos)

    elif user_action.startswith('show'):

        todos = get_todos()

        for index, item in enumerate(todos):
            clean = item.rstrip("\n")
            row = f"{index + 1}-{clean}"

            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1
            
            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            write_todos(todos)
        except ValueError:
            print(f'You fucking command "{user_action}" is not valid, you fucking idiot!')
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print(f'You fucking FUCK! There is no fucking task with number {number}')
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid.")  


print("Fuck off!")
