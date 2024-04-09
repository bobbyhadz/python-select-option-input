# Using user input to select an option from a list in Python

options = ['python', 'js', 'ts']

user_input = ''

input_message = "Pick an option:\n"

for index, item in enumerate(options):
    input_message += f'{index+1}) {item}\n'

input_message += 'Your choice: '

while user_input.lower() not in options:
    user_input = input(input_message)

print('You picked: ' + user_input)