usersList = [
	{'username': 'Admin', 'password': 'password1', 'role': 'admin', 'isActive': False},
    {'username': 'Instructor', 'password': 'password2', 'role': 'instructor', 'isActive': False},
    {'username': 'Student', 'password': 'password3', 'role': 'student', 'isActive': False},
]

courseMaterial = [
    {'Course': 'Science [1]', 'Grade': 85, 'Instructor': None},
    {'Course': 'Math [2]', 'Grade': 75, 'Instructor': None},
    {'Course': 'English [3]', 'Grade': 95, 'Instructor': None},
]

studentAssignments = [
    {'Assignment 1': ''},
    {'Assignment 2': ''},
    {'Assignment 3': ''},
]

accessLevel = ''

#Checks username and password against the users list of dictionaries
def userLogin():
    #Stores user inputs as username and password
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    
    #Iterates through the users list to find a username and password match
    for user_entry in range(len(usersList)):
        
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
            elif usersList[user_entry]['role'] == 'instructor':
                print("Instructor-level access granted")
                accessLevel = 'instructor'
            elif usersList[user_entry]['role'] == 'student':
                print("Student-level access granted")
                accessLevel = 'student'

#Prints courses, grades, and the course instructor to the user
def viewCoursesAndGrades():
    for entry in range(len(courseMaterial)):
        #Prints based on the value of 'Course' and 'Grade' from list of dicts
        print(f" {courseMaterial[entry]['Course']}: {courseMaterial[entry]['Grade']} - Current Instructor: {courseMaterial[entry]['Instructor']}")

#Takes user input as integer to assign as the student's grade for the specified course
def editGrades():
    for entry in range(len(courseMaterial)):
        print(f" {courseMaterial[entry]['Course']}: {courseMaterial[entry]['Grade']}")
    course = input("Select the course you wish to set a grade for: ")
    if course == "1":
        courseGrade  = input("Enter the course grade: ")
        courseMaterial[0]['Grade'] = courseGrade
    elif course == "2":
        courseGrade  = input("Enter the course grade: ")
        courseMaterial[1]['Grade'] = courseGrade
    elif course == "3":
        courseGrade  = input("Enter the course grade: ")
        courseMaterial[2]['Grade'] = courseGrade

#Takes user input to assign a course instructor
def editCourseAdmin():
    for entry in range(len(courseMaterial)):
        print(f" {courseMaterial[entry]['Course']} - Current Instructor: {courseMaterial[entry]['Instructor']}")
    course = input("Select the course you wish to set an instructor for: ")
    if course == "1":
        courseInstructor  = input("Enter the instructor's username: ")
        courseMaterial[0]['Instructor'] = courseInstructor
    elif course == "2":
        courseInstructor  = input("Enter the instructor's username: ")
        courseMaterial[1]['Instructor'] = courseInstructor
    elif course == "3":
        courseInstructor  = input("Enter the instructor's username: ")
        courseMaterial[2]['Instructor'] = courseInstructor

#Takes user input and assigns as value to specified key in studentAssignments
def uploadAssignments():
    for entry in range(len(studentAssignments)):
        print(f" {studentAssignments[entry]}")
    assignment = input("Select the assignment you wish to upload: ")
    if assignment == "1":
        upload = input("Enter your assignment: ")
        studentAssignments[0]['Assignment 1'] = upload
    elif assignment == "2":
        upload = input("Enter your assignment: ")
        studentAssignments[1]['Assignment 2'] = upload
    elif assignment == "3":
        upload = input("Enter your assignment: ")
        studentAssignments[2]['Assignment 3'] = upload

#Prints that x number of assignments have been graded to student based on the courseMaterial list length
def notifyStudent():
    print(f"You have {len(courseMaterial)} new grades to view!")

#Main function for the learning platform access system
def systemLoop():
    #Loop to continue execution of program
    while True:
        print("Learning Platform Access System")
        print("[1] - Log In")
        print("[2] - Exit")
        loginOrExit = input("Please select an option: ")
        if loginOrExit == "1":
            userLogin()
            userAuth()
            if accessLevel == 'admin':
                #Continuously loops through options until logout
                while True:
                    print("Admin Options: ")
                    print("[1] - View Courses and Grades")
                    print("[2] - Edit Courses")
                    print("[3] - Edit Grades")
                    print("[4] - Log Out")
                    optionSelect = input("Please select an option: ")
                    if optionSelect == "1":
                        viewCoursesAndGrades()
                    elif optionSelect == "2":
                        editCourseAdmin()
                    elif optionSelect == "3":
                        editGrades()
                    elif optionSelect == "4":
                        print("Logging out...")
                        usersList[0]['isActive'] = False
                        break
            elif accessLevel == 'instructor':
                #Continuously loops through options until logout
                while True:
                    print("Instructor Options: ")
                    print("[1] - View Courses and Grades")
                    print("[2] - Edit Grades")
                    print("[3] - Log Out")
                    optionSelect = input("Please select an option: ")
                    if optionSelect == "1":
                        viewCoursesAndGrades()
                    elif optionSelect == "2":
                        editGrades()
                    elif optionSelect == "3":
                        print("Logging out...")
                        usersList[1]['isActive'] = False
                        break
            elif accessLevel == 'student':
                #Continuously loops through options until logout
                while True:
                    print("Student Options: ")
                    print("[1] - View Courses and Grades")
                    print("[2] - Upload Assignment")
                    print("[3] - View Notifications")
                    print("[4] - Log Out")
                    optionSelect = input("Please select an option: ")
                    if optionSelect == "1":
                        viewCoursesAndGrades()
                    elif optionSelect == "2":
                        uploadAssignments()
                    elif optionSelect == "3":
                        notifyStudent()
                    elif optionSelect == "4":
                        print("Logging out...")
                        usersList[2]['isActive'] = False
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
