

courseMaterial = [
    {}
]

usersList = [
	{'id': 100, 'username': 'Admin', 'password': 'password1', 'role': 'admin', 'isActive': False},
    {'id': 200, 'username': 'Instructor', 'password': 'password2', 'role': 'instructor', 'isActive': False},
    {'id': 300, 'username': 'Student', 'password': 'password3', 'role': 'student', 'isActive': False},
]

accessLevel = ''

#Checks username and password against the users list of dictionaries
def userLogin():
    #Stores user inputs as username and password
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    
    #Iterates through the users list to find a username and password match
    for user_entry in range(len(usersList)):                                            #len used to return user_entry as int
        
        #Welcomes the user and sets isActive to True if inputs match with dict
        if username == usersList[user_entry]['username'] and password == usersList[user_entry]['password']:
            print(f"Welcome {username}")
            usersList[user_entry]['isActive'] = True
            break
    else:
        print("Incorrect username or password")

#Authenticates and delegates access based on the role of the user that has logged in
def userAuth():
    #Declares accessLevel variable as global to be modified from within this function
    global accessLevel

    #Iterates through the users list to determine the role of the active user, sets accessLevel accordingly
    for user_entry in range(len(usersList)):
        if usersList[user_entry]['isActive'] == True:
            if usersList[user_entry]['role'] == 'admin':
                print("Admin-level access granted")
                accessLevel = 'admin'
            if usersList[user_entry]['role'] == 'instructor':
                print("Instructor-level access granted")
                accessLevel = 'instructor'
            if usersList[user_entry]['role'] == 'student':
                print("Student-level access granted")
                accessLevel = 'student'

def coursesAndGrades():
    "ex"

def editCoursesAndGrades():
    "ex"

def editCourseAdmin():
    "ex"

def uploadAssignments():
    "ex"

def notifyStudent():
    "ex"

#Main function for the learning platform access system
def systemLoop():
    print("Learning Platform Access System")
    userLogin()
    userAuth()
    print("Please choose from the following options:")
    print(accessLevel)

systemLoop()
#References
# https://stackoverflow.com/questions/52765473/how-do-i-check-for-a-user-name-and-associated-password-in-a-list-of-dictionaries
