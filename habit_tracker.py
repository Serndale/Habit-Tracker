# this is a habit tracking project. needs to be able to add habits, view habits, mark them complete, and quit.
import sys
habits = []

while True:

    print('Habit Tracker')
    print('1. Add Habit')
    print('2. View Habits')
    print('3. Mark Habit Complete')
    print('4. Quit')

    choice = input('Choose an option: ')
    if choice == '4':
        break


    if choice == '1':
        habit_name = input('Enter habit name: ')
        habits = habits + [habit_name]
        print('Habit added.')
    elif choice == '2':
        print('Your habits:')
        for habit_name in habits:
            print(habit_name)
    
