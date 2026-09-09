
users = {}

def sign_up():
    username = input ("choose your username:")
    if username in users:
        print("this username is already exist choose anoter one!")
    else:

        password = input ("choose your password:")
        users [username] = password


def login ():
    username = input("enter ypur username:")
    
    while username in users:
        password = input("enter your pass:")
        if password == users[username]:
            print ("match found, welcome")

            break
        else:
            print("your entered password is wrong, re_enter your password")
    else:
        print ("your entered username is wrong, try again:")