

usersList = [
	{'id': 100, 'username': 'Admin', 'password': 'password1', 'role': 'admin', 'isActive': False},
    {'id': 200, 'username': 'Instructor', 'password': 'password2', 'role': 'instructor', 'isActive': False},
    {'id': 300, 'username': 'Instructor2', 'password': 'password2', 'role': 'instructor', 'isActive': False},
    {'id': 400, 'username': 'Instructor3', 'password': 'password2', 'role': 'instructor', 'isActive': False},
    {'id': 500, 'username': 'Student', 'password': 'password3', 'role': 'student', 'isActive': False, 'notification': ''},
    {'id': 600, 'username': 'Student2', 'password': 'password3', 'role': 'student', 'isActive': False, 'notification': ''},
]

courseMaterial = [
    {'Course': 'Science', 'Grade': 85},
    {'Course': 'Math', 'Grade': 75},
    {'Course': 'English', 'Grade': 95},
]

studentAssignments = [
    {},
    {},
    {},
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

#Prints courses and grades to the user
def viewCoursesAndGrades():
    for entry in range(len(courseMaterial)):
        #Prints based on the value of 'Course' and 'Grade' from list of dicts
        print(f" {courseMaterial[entry]['Course']}: {courseMaterial[entry]['Grade']}")

def editCoursesAndGrades():
    "ex"

def editCourseAdmin():
    "ex"

def uploadAssignments():
    "ex"

#End goal of function is to display students and provide option to input a value for key 'notification' in usersList
def notifyStudent():
    for user_entry in range(len(usersList)):
        if usersList[user_entry]['role'] == 'student':
            print(f" {usersList[user_entry]['username']}")


#Main function for the learning platform access system
def systemLoop():
    print("Learning Platform Access System")
    userLogin()
    userAuth()
    
    if accessLevel == 'admin':
        print("Admin Options: ")
    elif accessLevel == 'instructor':
        print("Instructor Options: ")
    elif accessLevel == 'student':
        print("Student Options: ")
        print("[1] - View Courses and Grades")
        print("[2] - Upload Assignment")
        print("[3] - View Notifications")
        optionSelect = input("Please select an option: ")
        if optionSelect == "1":
            viewCoursesAndGrades()
        elif optionSelect == "2":
            print("Upload Assignment")
        elif optionSelect == "3":
            print("Notification goes here")
    else:
        print("Authentication failed, please retry")
    
    #print(accessLevel)

systemLoop()
#References
# https://stackoverflow.com/questions/52765473/how-do-i-check-for-a-user-name-and-associated-password-in-a-list-of-dictionaries
