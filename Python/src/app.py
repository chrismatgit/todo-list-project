# ---- app.py ----

# This file contains the entry point to your tasks

# and the logic to manage it



from task import todo_list, create_task, delete_task, delete_all_tasks, mark_as_finished  # import other functions as well

from account import accounts, add_account, login # import the function as well





if __name__ == "__main__":

    """

        Allow a person to input a name and a password



        E.g

    """
    """

        Let the person sign in. If there details do not exist,

        create an account for them



        E.g 

    """
    
    name = raw_input("Enter your name: ")
    password = raw_input("Enter your password: ")
    if login(name, password):
        pass
    else:
        print( 'User does not exist, we are creating your account\n')
        add_account(name, password)
        login(name, password)






    """

        Provide options:

            1. creating a task

            2. deleting a task 

            3. deleting all tasks

            4. Marking a task finished



        E.g

    """

    while 1:

        print('\n***************************************')
        print("""Select Option:
                1. create a task

                2. delete a task 

                3. delete all tasks

                4. Mark a task as finished
                
                5. close the program
            """)
        selection = raw_input("option ")



#Write code that implements the selected option

        if selection == '1':
            if len(todo_list) < 1:
                task = raw_input('\nEnter the first task name: ')
            else:
                task = raw_input('\nEnter the next task name: ')
            if task == '':
                print('\n task name can not be empty')
            else:
                create_task(task)
        elif selection == '2':
            task_to_delete = raw_input('\nEnter a task name to delete: ')
            delete_task(task_to_delete)
        elif selection == '3':
            delete_all_tasks()
        elif selection == '4':
            task_finished = raw_input('\nEnter a finished task name: ')
            mark_as_finished(task_finished)
        elif selection == '5':
            break
        else:
            print('\nSelected option must be 1, 2 , 3 , 4 or 5')
        
    
