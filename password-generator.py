from time import sleep
import random
import string

def randomizer(length):
    count = 0
    pw = ""
    while count < length:
        a =  random.choice(string.ascii_letters)
        pw = pw + str(a)
        count += 1

    return pw

print("Hello, this application can generate strong and secure passwords for you!")
sleep(1)
print("Start by typing in one of the 3 numbers according to your preferences.")
sleep(0.2)
print("""
    1 -> short password with 4 characters
    2 -> mid password with 8 characters
    3 -> long password with 14 characters
    """)
sleep(0.8)
user_input = input("Your Choice:" )

if user_input == "1" or "2" or "3":
    if user_input == "1":
        print("Your generated password is: " + randomizer(4))
    if user_input == "2":
        print("Your generated password is: " + randomizer(8))
    if user_input == "3":
        print("Your generated password is: " + randomizer(14))
else:
    print("No valid input!")

print("")

