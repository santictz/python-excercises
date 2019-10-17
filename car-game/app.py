# This program is a simulator for a car engine. User can ask for help
# It will run in a while loop until user inputs quit
command = ""
while True:
    command = input('>').lower()
    if command == 'help':
        print('start - to start the car\nstop - to stop the car\nquit - to exit')
    elif command == 'start':
        print('Car started... ready to go!')
    elif command == 'stop':
        print('Car stopped')
    elif command == 'quit':
        break
    else:
        print('I do not understand that...')