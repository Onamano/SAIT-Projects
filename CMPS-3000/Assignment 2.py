
userList = [
	{'id': 100, 'username': 'Mike', 'password': 'P@ssw0rd', 'role': 'Administrator', 'subActive': True, 'loggedIn': False},
    {'id': 101, 'username': 'Ben', 'password': 'P@ssw0rd', 'role': 'Administrator', 'subActive': True, 'loggedIn': False},
    {'id': 102, 'username': 'Joe', 'password': 'P@ssw0rd', 'role': 'Viewer', 'subActive': True, 'loggedIn': False},
    {'id': 103, 'username': 'Adam', 'password': 'P@ssw0rd', 'role': 'Editor', 'subActive': True, 'loggedIn': False},
    {'id': 104, 'username': 'Timmy', 'password': 'P@ssw0rd', 'role': 'Viewer', 'subActive': True, 'loggedIn': False},
    {'id': 105, 'username': 'Rhonda', 'password': 'P@ssw0rd', 'role': 'Editor', 'subActive': True, 'loggedIn': False},
    {'id': 106, 'username': 'Deborah', 'password': 'P@ssw0rd', 'role': 'Viewer', 'subActive': True, 'loggedIn': False},
    {'id': 107, 'username': 'Rebecca', 'password': 'P@ssw0rd', 'role': 'Editor', 'subActive': True, 'loggedIn': False},
    {'id': 108, 'username': 'Frank', 'password': 'P@ssw0rd', 'role': 'Viewer', 'subActive': False, 'loggedIn': False},
    {'id': 109, 'username': 'Sally', 'password': 'P@ssw0rd', 'role': 'Editor', 'subActive': False, 'loggedIn': False},
    
]

accessLevel = ''

#Checks username and password against the users list of dictionaries
def userLogin():
    #Stores user inputs as username and password
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    
    #Iterates through the users list to find a username and password match
    for user_entry in range(len(userList)):
        if username == userList[user_entry]['username'] and password == userList[user_entry]['password']:
            print(f"Welcome {username}")
            userList[user_entry]['loggedIn'] = True
            break
    else:
        print("Incorrect username or password")

#Authenticates and delegates access based on the role of the user that has logged in
def userAuth():
    #Declares accessLevel variable as global to be modified from within this function
    global accessLevel

    #Iterates through the users list to determine the role of the active user, sets accessLevel accordingly
    for user_entry in range(len(userList)):
        if userList[user_entry]['subActive'] == True and userList[user_entry]['loggedIn'] == True:
            if userList[user_entry]['role'] == 'Administrator':
                accessLevel = 'admin'
                break
            elif userList[user_entry]['role'] == 'Editor':
                accessLevel = 'editor'
                break
            elif userList[user_entry]['role'] == 'Viewer':
                accessLevel = 'viewer'
                break
            else:
                print('Subscription expired, please contact system administrator to renew.')

#Main function for the learning platform access system
def systemLoop():
    #Loop to continue execution of program
    while True:
        print("Smart Notification System")
        print("[1] - Log In")
        print("[2] - Exit")
        loginOrExit = input("Please select an option: ")
        if loginOrExit == "1":
            userLogin()
            userAuth()
            if accessLevel == 'admin':
                #Continuously loops through options until logout
                while True:
                    print("Your role is: Administrator")
                    print("Permissions granted: Settings enabled")
                    break
            elif accessLevel == 'editor':
                #Continuously loops through options until logout
                while True:
                    print("Your role is: Editor")
                    print("Permissions granted: Editor license enabled")
                    break
            elif accessLevel == 'viewer':
                #Continuously loops through options until logout
                while True:
                    print("Your role is: Viewer")
                    print("Permissions granted: Viewer license enabled")
                    break
            else:
                print("Authentication failed, please retry")
        #Exits while loop, ending execution
        elif loginOrExit == "2":
            break

systemLoop()

#References
# https://stackoverflow.com/questions/52765473/how-do-i-check-for-a-user-name-and-associated-password-in-a-list-of-dictionaries
# CMPS Course materials
