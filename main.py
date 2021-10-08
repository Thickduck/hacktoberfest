# A simple password safe's structure.


# First off, your variables should be at the topmost.

username = str(input('Your username: '))
crt_user = 'Thickduck'
crt_pass = 'abcd1234'

# prints an error message when called.
def error():
    print('You have entered the wrong password! ')

# prints a simple welcome message if called.
def correct():
    print('Welcome, ' + username)

# prints an username error message if called.
def user_error():
    print('No such username exists! ')

# prints a simple hello message if called.
def user_correct():
    print('Hello, ' + username)


# Then, comes our if statements.

# Here, I'm checking if the input of username is equal to the correct username.
# You can use an array of username and passwords and make it work with some if statement tweaking.
if username == crt_user:
    user_correct()

    # this variable is to be only called when the above if statement is satisfied.
    passinput = str(input('Your password here, ' + username + ': '))

    if passinput == crt_pass:
        correct()


    else:
        error()

else:
    user_error()