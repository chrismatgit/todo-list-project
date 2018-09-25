# --- tasks.py ---

# This file contains code that manages your todo_list

todo_list = []


def print_tasks(task):
    print('---------------------\nTasks list:')
    position = 0
    for todo in todo_list:
        position += 1
        print(position, todo)
    print('---------------------\n')

    task ={
            'title': 'given title',
            'description': 'given description',
            'state':'finished'

        }
# Write a function creates a task
def create_task(task):

    """
    Adds the task (string value) to todo_list
    """
    # for todo in todo_list:
    #     if todo['title'] in todo_list:
    #         return "The task with the title {} already exists".format(todo['title'])  
     
    todo_list.append(task)
    print_tasks(task)
    print('Task "'+task+'" created successfully\n')
    return True
   

def delete_task(task):

    """
    Removes the specified task from the todo_list
    """
    if task == '':
        print('Task to delete can not be empty')
        return False
    else:
        # for task in todo_list:
        #     if task['title'] is not '':
                todo_list.remove(task)
                print('Task "'+task+'" deleted successfully\n')
                print_tasks(task)
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
        print_tasks(task)


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
        print_tasks(task)
        return True


