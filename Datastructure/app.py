# ---- app.py ----

# This file contains the entry point to your tasks

# and the logic to manage it



from task import todo_list, create_task, delete_task, delete_all_tasks, mark_as_finished  # import other functions as well

from account import accounts, add_account, login # import the function as well


if __name__ == "__main__":

    name = raw_input("Enter your name: ")
    password = raw_input("Enter your password: ")
    if login(name, password):
        pass
    else:
        print( 'User does not exist, we are creating your account\n')
        add_account(name, password)
        login(name, password)
   
    while True:

        print('\n***************************************')
        x = """Select Option:
                1. create a task

                2. delete a task 

                3. delete all tasks

                4. Mark a task as finished
                
                5. close the program
            """
        print(x)
        selection = raw_input("option ")

#Write code that implements the selected option

        if selection == '1':
            if len(todo_list) < 1:
                # for a in range(1):
                title = raw_input("Enter title: ")
                description = raw_input("Enter desciption: ")
                state = raw_input("Enter state to mark it as finished(finished): ")
                if title =='':
                    print("task cannot be empty")
                if description =='':
                    print("description cannot be empty") 
                if state == '':
                    print("state cannot")
                else:
                    create_task(title)

                
              

               
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
        
    
