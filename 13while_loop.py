print('enter a no. to check if that is even or odd')

user_input = ""
while user_input !='q':

    user_input= (input('enter a no. or q for quit:'))
    if user_input.isdigit():
        if int( user_input) % 2 == 0:
            print('yes no. isn even')
        else:
            print('no. is odd')