import string
import random
from functools import reduce

loginAttempts = 1  # login attempt counter for admin login
records = 0  # used for view user menu records counter
showRecords = 0  # used for view user menu records counter for viewable passwords

#  user details lists
autoUsername = []  # used to hold auto generated username later on
hiddenPassword = []  # used to hold auto generated hidden password later on
users = []  # 1d list to place user details
allUserDetails = []  # 2d list for non asterisked passwords


def main_menu():  # function for main menu
    print(":: Main Menu ::")
    print("1. Create New User")
    print("2. View User")
    print("3. Update User")
    print("4. Quit")


def new_user_menu():  # function for the new user menu
    print("\n::New User Menu::")
    print("-" * 17)


def user_role():  # function for role selection menu
    print("\nSelect role for the user: ")
    print("1. User")
    print("2. Admin")


def department():  # function for the department selection menu
    print("\nSelect department for the user: ")
    print("1. Administration")
    print("2. Operation")
    print("3. Technology")


def dept_summary():  # function for the user profile
    print("\n:: User Profile Summary ::")
    print("-" * 25)
    print("First Name: ", users[-4])
    print("Last Name: ", users[-3])
    print("User Role: ", users[-2])
    print("User Department:", users[-1], "\n")


def view_user():  # function for view user menu
    print("\n:: View User ::")
    print("\nList of Users")
    print("-" * 15)


def update_user():
    print("\n:: Update User ::")
    print("-" * 17)
    print("\nWhich field would you like to update?\n")
    print("1. First Name")
    print("2. Last Name")
    print("3. Role")
    print("4. Department")


def random_password():  # function that creates a random password when called
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits  # what characters are available to be used
    size = random.randint(8, 8)  # what range the password can fall between
    return ''.join(random.choice(chars) for x in range(size))


def random_username():  # function that creates a random username when called
    chars = string.ascii_lowercase + string.digits  # what characters are available to be used
    size = random.randint(1, 2)  # what range the username can fall between
    return firstName.lower() + lastName.lower().join(random.choice(chars) for x in range(size))


# ------------------------------------------------ REQUIREMENT 1 ------------------------------------------------------#
print(" :: Welcome to User Management System :: ")  # initial login message
print("-" * 42)  # initial login message
userName = input("Username : ")  # asking for admin username
userPassword = input("Password : ")  # asking for admin password

# ------------------------------------------------ REQUIREMENT 2 ------------------------------------------------------#
while userName != "admin" or userPassword != "123":  # while loop to check username and password
    if loginAttempts <= 2:  # if login attempts are 2 or less user is given another chance to enter username & password
        print("Attempt : ", loginAttempts)
        print("Invalid username and password!\n")
        userName = input("Username : ")
        userPassword = input("Password : ")
        loginAttempts += 1  # increments login attempt counter each time incorrect details entered
    else:  # if login attempts reach 3 attempts account locks
        print("Account has been blocked")
        quit()

# ------------------------------------------------ REQUIREMENT 3 ------------------------------------------------------#
print("\nSuccessfully logged in\n")  # if details are correct prints this statement
main_menu()  # initial main menu print
mainSelection = input("\nSelect a menu - input a number: ")  # main menu selection from user

# ------------------------------------------------ REQUIREMENT 4 ------------------------------------------------------#
while mainSelection != ("1", "2", "3", "4"):  # loops while main selection isn't expected digits
    if not mainSelection.isdigit():  # checking that main menu selection is a digit
        mainSelection = input("\nYou have entered a non digit value, Select again: ")  # prompting reentry

# ------------------------------------------------ REQUIREMENT 5 ------------------------------------------------------#
    elif mainSelection == "1":  # create new user menu code block
        new_user_menu()  # new user menu
        firstName = input("Input First name: ")  # asking user to input first name
        users.append(firstName)  # adding user input into the visibleUser list
        lastName = input("Input Last Name: ")  # asking user to input last name
        users.append(lastName)  # adding user input into the visibleUser list

# ------------------------------------------------ REQUIREMENT 9 ------------------------------------------------------#
        autoUsername.append((random_username()))  # calling function to generate a username and add to autoUsername list
        if autoUsername[-1] in users:  # checking if username already exists
            print("\nGenerating new username and checking database")
            print("\nUsername already exists generating new")  # stating username already exists
            print("\nDuplicate username = ", autoUsername[-1])
            del autoUsername[-1]  # deleting the last element in autoUsername that was just created
            autoUsername.append(random_username())  # generating new username
        else:
            print("\nUsername provisionally generated Checked and OK!")  # will pretty much always print this due to
            # username generation complexity

# ------------------------------------------------ REQUIREMENT 6 ------------------------------------------------------#
        user_role()  # prints user role menu
        roleSelect = input("Enter here: ")  # asking user for input for role selection
        while roleSelect != "1" and roleSelect != "2":  # while loop to check correct selection
            print("Unrecognised Input!\n")
            user_role()
            roleSelect = input("enter here: ")  # asking user for reentry
        if roleSelect == "1":
            users.append("User")
        elif roleSelect == "2":
            users.append("Admin")

        department()  # prints department menu
        deptSelect = input("Enter here: ")  # asking user for department selection
        while deptSelect != "1" and deptSelect != "2" and deptSelect != "3":  # while loop to check correct selection
            print("Unrecognised Input!\n")
            department()
            deptSelect = input("enter here: ")  # asking user for reentry

# ------------------------------------------------ REQUIREMENT 7 ------------------------------------------------------#
        if deptSelect == "1":
            users.append("Administration")
            dept_summary()
        elif deptSelect == "2":  # Operation Department if statement
            users.append("Operation")
            dept_summary()
        elif deptSelect == "3":  # Technology department If statement
            users.append("Technology")
            dept_summary()
# ------------------------------------------------ REQUIREMENT 8 ------------------------------------------------------#
        userConfirm = input("Press 1 to proceed with username and password creation or any to quit: ")
        while userConfirm != "1":
            print("Details deleted")
            users = []  # emptying all the appended details that have just been created
            main_menu()  # printing main menu
            mainSelection = input("\nSelect a menu - input a number: ")  # asking user for entry
            break
# ------------------------------------------------ REQUIREMENT 10 -----------------------------------------------------#
        else:
            print("\nGenerating username and password .....\n")
            users.append(autoUsername[-1])  # Last username generated added to visibleUsers
            tempPass = random_password()  # random password generated and held in temporary variable tempPass
            passConvert = list(tempPass)  # converting tempPass to a list passConvert
            passConvert[0:5] = "*****"  # slicing first 5 digits of passConvert and replacing with asterisks
            asteriskPass = "".join(passConvert)  # joining passConvert to a new variable asteriskPass
            hiddenPassword.append(asteriskPass)  # appending new variable to hiddenPassword list
            print("Generated username: ", autoUsername[-1])  # printing the last userName generated
            print("Generated password: ", hiddenPassword[-1])  # printing the last password generated but hidden
            users.append(hiddenPassword[-1])  # appending hiddenPassword to hiddenUsers list
            users.append(tempPass)  # temp password appended to visibleUsers before its altered
            allUserDetails.append(users)  # creation of 2D list
            print("\nUser account has been successfully saved \n")
            users = []  # emptying list
            main_menu()  # printing the main menu
            mainSelection = input("\nSelect a menu - input a number: ")  # asking user for main menu input

# ------------------------------------------------ REQUIREMENT 11 -----------------------------------------------------#
    elif mainSelection == "2":
        view_user()  # prints the view user menu
        print("\nThere is/are ", len(allUserDetails), "records\n")
        records += 1
        print("-" * 35)
        for row in range(len(allUserDetails)):
            print("Record: ", records)
            records += 1
            s = (f"""\
Name          : {allUserDetails[row][0]} {allUserDetails[row][1]}
Role          : {allUserDetails[row][2]}
Department    : {allUserDetails[row][3]}
Username      : {allUserDetails[row][4]}
Password      : {allUserDetails[row][5]}""")

            maxlen = reduce(lambda x, y: max(x, len(y)), s.split("\n"), 0)
            print(f"{s}\n{'-' * 35} \n")
        records = 0
        print()
        revealPasswords = input("""\nPress 999 to see the user passwords - (Warning user password view should get
    permissions from super admin!) Press 1 to return to Main Menu: """)
        # asking user if they want to reveal or return

# ------------------------------------------------ REQUIREMENT 12 -----------------------------------------------------#
        while revealPasswords != ("999", "1"):  # loops while main selection isn't expected digits
            if not revealPasswords.isdigit():  # checking that main menu selection is a digit
                revealPasswords = input("You have entered a non digit value, Select again: ")  # prompting reentry
            elif revealPasswords == "999":
                print("\nThere is/are ", len(allUserDetails), "records\n")
                showRecords += 1
                print("-" * 35)
                for row in range(len(allUserDetails)):
                    print("Record: ", showRecords)
                    showRecords += 1
                    s = (f"""\
Name          : {allUserDetails[row][0]} {allUserDetails[row][1]}
Role          : {allUserDetails[row][2]}
Department    : {allUserDetails[row][3]}
Username      : {allUserDetails[row][4]}
Password      : {allUserDetails[row][6]}""")

                    maxlen = reduce(lambda x, y: max(x, len(y)), s.split("\n"), 0)
                    print(f"{s}\n{'-' * 35}\n")

                showRecords = 0
                print()
                main_menu()
                mainSelection = input("\nSelect a menu - input a number: ")  # main menu selection from user
                break
            elif revealPasswords == "1":
                print()
                main_menu()
                mainSelection = input("\nSelect a menu - input a number: ")  # main menu selection from user
                break
            else:
                revealPasswords = input(("Select either 999 to view passwords !Super Admin! only or press 1 to"
                                         "return to Main Menu: "))

# ------------------------------------------------ REQUIREMENT 13 -----------------------------------------------------#
    elif mainSelection == "3":
        print("\n:: User Search :: ")
        print("-" * 17)
        searchUser = input("\nInput username to edit (press 1 to return to Main Menu): ").lower()

# ------------------------------------------------ REQUIREMENT 14 -----------------------------------------------------#
        while searchUser != "1":
            if (searchUser in sublist for sublist in allUserDetails):
                print("\nUser not found")

            for x in allUserDetails:
                if x[4] == searchUser:
                    print()
                    print(searchUser, "found in the list")
                    update_user()
                    updateSelection = input("\nInput number of field or press any to return to Menu 3: ")

# ------------------------------------------------ REQUIREMENT 15 -----------------------------------------------------#
                    if updateSelection == "1":
                        newFirstName = input("\nInput new First Name: ")
                        x[0] = newFirstName
                        print("\nUpdate Successful")
                        goAgain = input("\nPress 1 to update the same user again, press any to search new user: ")
                        if goAgain == "1":
                            update_user()
                            updateSelection = input("\nInput number of field or press any to return to Menu 3: ")
                        if goAgain != "1":
                            continue

                    if updateSelection == "2":
                        newLastName = input("\nInput new Last Name: ")
                        x[1] = newLastName
                        print("\nUpdate Successful")
                        goAgain = input("\nPress 1 to update the same user again, press any to search new user: ")
                        if goAgain == "1":
                            update_user()
                            updateSelection = input("\nInput number of field or press any to return to Menu 3: ")
                        if goAgain != "1":
                            continue

                    if updateSelection == "3":
                        print("\nSelect Role for the selected User")
                        print("1: User")
                        print("2: Admin")
                        newRole = input("\nInput number of field: ")
                        if newRole == "1":
                            x[2] = "User"
                            print("\nUpdate Successful")
                        if newRole == "2":
                            x[2] = "Admin"
                            print("\nUpdate Successful")
                        goAgain = input("\nPress 1 to update the same user again, press any to search new user: ")
                        if goAgain == "1":
                            update_user()
                            updateSelection = input("\nInput number of field or press any to return to Menu 3: ")
                        if goAgain != "1":
                            continue

                    if updateSelection == "4":
                        print("\nSelect Department for the selected User")
                        print("1: Administration")
                        print("2: Operation")
                        print("3: Technology")
                        newDepartment = input("\nInput number of field: ")
                        if newDepartment == "1":
                            x[3] = "Administration"
                            print("\nUpdate Successful")
                        if newDepartment == "2":
                            x[3] = "Operation"
                            print("\nUpdate Successful")
                        if newDepartment == "3":
                            x[3] = "Technology"
                            print("\nUpdate Successful")
                        goAgain = input("\nPress 1 to update the same user again, press any to search new user: ")
                        if goAgain == "1":
                            update_user()
                            updateSelection = input("\nInput number of field or press any to return to Menu 3: ")
                        if goAgain != "1":
                            continue
            else:
                break
        else:
            print()
            main_menu()
            mainSelection = input("\nSelect a menu - input a number: ")  # main menu selection from user

    elif mainSelection == "4":
        print("\nYou have logged out")  # self explanatory but when user choose 4 on the main menu, the program finishes
        quit()  # quit function to close program

# -------------------------------------------------REQUIREMENT 4 ------------------------------------------------------#
    else:
        print("\nThere is no menu ", mainSelection, "\n")  # telling the user that their specific entry isn't an option
        main_menu()  # printing the main menu again
        mainSelection = input("\nSelect a menu - input a number: ")  # asking user for re-entry


