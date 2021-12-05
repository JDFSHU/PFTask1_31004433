import random
import string


def random_username():  # function that creates a random password when called
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits  # what characters are available to be used
    size = random.randint(1, 2)  # what range the password can fall between
    return firstName + lastName.join(random.choice(chars) for x in range(size))

# because of how complex my random username generator is, its very unlikely that it will generate a username that is
# identical to one that is already in the system, therefore I have created this seperate file to showcase that req 9
# code actually works


firstName = input("Please enter first name: ")
lastName = input("Please enter second name: ")

users = ["JacobF91"]
autoUsername = ["JacobF91"]

if autoUsername[-1] in users:
    print("\nGenerating new username and checking database")
    print("\nUsername already exists generating new")
    print("\nDuplicate username = ", autoUsername[-1])
    del autoUsername[-1]
    autoUsername.append(random_username())

    print("New username = ", autoUsername)
else:
    print("\nUsername provisionally generated Checked and OK!")
