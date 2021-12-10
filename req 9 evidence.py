import random
import string


def random_username():  # function that creates a random username when called
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits  # what characters are available to be used
    size = random.randint(1, 2)  # what range the username can fall between
    return firstName + lastName.join(random.choice(chars) for x in range(size))

# because of how complex my random username generator is, its very unlikely that it will generate a username that is
# identical to one that is already in the system, therefore I have created this separate file to showcase that req 9
# code actually works


allUserDetails = [["firstname", "lastname", "role", "dept", "username", "hidden password", "viewable password"],
                   ["test", "test", "test", "test", "test", "test", "test"],
                  ["test", "test", "test", "test", "test", "test", "test"],
                   ["test", "test", "test", "test", "test", "test", "test"],
                   ["test", "test", "test", "test", "test", "test", "test"],
                  ["test", "test", "test", "test", "test", "test", "test"],
                  ["test", "test", "test", "test", "JacobF91", "test", "test"]]
autoUsername = []

firstName = input("Please enter first name: ")
lastName = input("Please enter second name: ")
autoUsername.append("JacobF91")  # for illustration purposes I have set this first username to match the already
# existing username in the allUserDetails 2D list, that way you can see that req 9 does work

# The for loop iterates through allUserDetails looking for duplicates at element position 4, if it finds a username that
# matches the current autoUserName then it prompts the admin, prints a message and generates a new one, else if no match
# is found it prints a message saying the username is provisionally generated and ok

for duplicate in allUserDetails:
    if duplicate[4] == autoUsername[-1]:
        print("\nGenerating new username and checking database")
        print("\nUsername already exists generating new")
        print("\nDuplicate username = ", autoUsername[-1])
        del autoUsername[-1]
        autoUsername.append(random_username())
        print("New username = ", autoUsername[-1])
else:
    print("\nUsername provisionally generated Checked and OK!")

