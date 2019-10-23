#Simple calculator to do basic arithmetic operations
while True:
    print('Options: ')
    print("Enter 'add' to add two numbers")
    print("Enter 'substract' to substract two numbers")
    print("Enter 'multiply' to multiply two numbers")
    print("Enter 'divide' to divide two numbers")
    print("Enter 'quit' to finish the program")
    user_input = input(': ')

    if user_input == 'quit':
        break
    elif user_input == 'add':
        num_1 = float(input('Please enter the first number: '))
        num_2 = float(input('Please enter the second number: '))
        print(f'The result is {num_1 + num_2}')
    elif user_input == 'substract':
        num_1 = float(input('Please enter the first number: '))
        num_2 = float(input('Please enter the second number: '))
        print(f'The result is {num_1 - num_2}')
    elif user_input == 'multiply':
        num_1 = float(input('Please enter the first number: '))
        num_2 = float(input('Please enter the second number: '))
        print(f'The result is {num_1 * num_2}')
    elif user_input == 'divide':
        num_1 = float(input('Please enter the first number: '))
        num_2 = float(input('Please enter the second number: '))
        print(f'The result is {num_1 / num_2}')
    else:
        print('Invalid input. Please read the instructions')
        continue