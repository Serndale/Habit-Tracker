# this is a habit tracking project. needs to be able to add habits, view habits, mark them complete, and quit.
import sys
habits = []

while True: # main loop

    print('Habit Tracker') # main program options
    print('1. Add Habit')
    print('2. View Habits')
    print('3. Mark Habit Complete')
    print('4. Quit')

    choice = input('Choose an option: ') 
    if choice == '4':
        break # exit program


    if choice == '1': # input habit name and add to list
        habit_name = input('Enter habit name: ')
        habit = {
            "name": habit_name,
            "completed": False # habit is not completed when added
        }
        habits.append(habit)
        print('Habit added.')
    elif choice == '2': # view habits and completion status
        print('Your habits:')
        for habit in habits:
            print(habit["name"] + ' - ' + ('Completed' if habit['completed'] else 'Not Completed'))
    elif choice == '3': # menu for marking habits complete. shows habits and completion status to update.
        print('Your habits:')
        for habit in habits:
            print(habit['name'] + ' - ' + ('Completed' if habit['completed'] else 'Not Completed'))
        habit_name = input('Enter habit name to mark complete: ')
        for habit in habits:
            if habit['name'] == habit_name:
                habit['completed'] = True
                print('Habit marked complete.')
                