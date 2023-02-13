username = input("Enter username:")

if len(username) < 10:
    print("Username contains less than 10 characters.")
else:
    print("Username contains 10 characters or more.")
'''The program first prompts the user to enter a username using the input() function,
 which stores the entered value in the username variable. 
 The len() function is then used to determine the length of the string stored in username.'''
