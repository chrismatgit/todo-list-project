# --- tasks.py ---

# This file contains code that manages your todo_list

todo_list = []


def print_tasks():
    print('---------------------\nTasks list:')
    position = 0
    for i in todo_list:
        position += 1
        print(position, i)
    print('---------------------\n')
# Write a function creates a task





def create_task(task):

    """

    Adds the task (string value) to todo_list

    """
    todo_list.append(task)
    print('Task "'+task+'" created successfully\n')
    print_tasks()
    return True


def delete_task(task):

    """

    Removes the specified task from the todo_list

    """
    if task == '':
        print('Task to delete can not be empty')
        return False
    else:
        todo_list.remove(task)
        print('Task "'+task+'" deleted successfully\n')
        print_tasks()
        return True



# Write a function that marks a task finished





def mark_as_finished(task):

    """

    Append the string label '[finished]' at the end of the task 

    if it does not already have the label appended.

    It should remain in the todo_list

    """
    key = 0
    found = False
    for i in todo_list:
        if i == task:
            todo_list[key] = task+' [finished]'
            found = True
            print('Task:' + todo_list[key]+'\n')
            break
        key += 1
    if not found or task == '':
        print('Task "'+task+'" not found in todo list\n')
    else:
        print_tasks()

        



# Write a function deletes all tasks





def delete_all_tasks():

    """

    Empty the the todo_lsit

    """
    for i in todo_list:
       todo_list.remove(i)
    if len(todo_list) > 0:
        delete_all_tasks()
    else:
        print('All tasks deleted successfully\n')
        print_tasks()
        return True


