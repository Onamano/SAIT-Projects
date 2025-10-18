users = [
    {'username': 'Admin', 'password': 'password1', 'role': 'admin'},
    {'username': 'Instructor', 'password': 'password2', 'role': 'instructor'},
    {'username': 'Student', 'password': 'password3', 'role': 'student'},
]

#Checks username and password against the users list of dictionaries
def userLogin():
    #Stores user inputs as username and password
    username = input("Please enter your username:")
    password = input('Please enter your password:')
    
    #Iterates through the users list to find a username and password match
    for user_entry in range(len(users)):                                            #len used to return user_entry as int
        if username == users[user_entry]['username']:
            if password == users[user_entry]['password']:
                print(f"Welcome {username}")
                break
            else:
                print("Incorrect username or password")
                break
        else:
            print("Incorrect username or password")
            break

def userAuth(users):
    "ex"

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

userLogin()
